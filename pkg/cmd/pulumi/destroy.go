// Copyright 2016-2024, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"context"
	"errors"
	"fmt"
	"os"

	mapset "github.com/deckarep/golang-set/v2"

	"github.com/spf13/cobra"

	"github.com/pulumi/pulumi/pkg/v3/backend"
	"github.com/pulumi/pulumi/pkg/v3/backend/display"
	cmdBackend "github.com/pulumi/pulumi/pkg/v3/cmd/pulumi/backend"
	"github.com/pulumi/pulumi/pkg/v3/cmd/pulumi/cmd"
	"github.com/pulumi/pulumi/pkg/v3/cmd/pulumi/config"
	"github.com/pulumi/pulumi/pkg/v3/cmd/pulumi/metadata"
	cmdStack "github.com/pulumi/pulumi/pkg/v3/cmd/pulumi/stack"
	"github.com/pulumi/pulumi/pkg/v3/engine"
	"github.com/pulumi/pulumi/pkg/v3/resource/deploy"
	"github.com/pulumi/pulumi/pkg/v3/resource/graph"
	"github.com/pulumi/pulumi/pkg/v3/resource/stack"
	pkgWorkspace "github.com/pulumi/pulumi/pkg/v3/workspace"
	"github.com/pulumi/pulumi/sdk/v3/go/common/apitype"
	"github.com/pulumi/pulumi/sdk/v3/go/common/env"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/cmdutil"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
	"github.com/pulumi/pulumi/sdk/v3/go/common/workspace"
)

func newDestroyCmd() *cobra.Command {
	var debug bool
	var remove bool
	var stackName string

	var message string
	var execKind string
	var execAgent string

	// Flags for remote operations.
	remoteArgs := RemoteArgs{}

	// Flags for engine.UpdateOptions.
	var jsonDisplay bool
	var diffDisplay bool
	var eventLogPath string
	var parallel int32
	var previewOnly bool
	var refresh string
	var showConfig bool
	var showReplacementSteps bool
	var showSames bool
	var skipPreview bool
	var suppressOutputs bool
	var suppressProgress bool
	var suppressPermalink string
	var yes bool
	var targets *[]string
	var targetDependents bool
	var excludeProtected bool
	var continueOnError bool

	use, cmdArgs := "destroy", cmdutil.NoArgs
	if remoteSupported() {
		use, cmdArgs = "destroy [url]", cmdutil.MaximumNArgs(1)
	}

	cmd := &cobra.Command{
		Use:        use,
		Aliases:    []string{"down", "dn"},
		SuggestFor: []string{"delete", "kill", "remove", "rm", "stop"},
		Short:      "Destroy all existing resources in the stack",
		Long: "Destroy all existing resources in the stack, but not the stack itself\n" +
			"\n" +
			"Deletes all the resources in the selected stack.  The current state is\n" +
			"loaded from the associated state file in the workspace.  After running to completion,\n" +
			"all of this stack's resources and associated state are deleted.\n" +
			"\n" +
			"The stack itself is not deleted. Use `pulumi stack rm` or the \n" +
			"`--remove` flag to delete the stack and its config file.\n" +
			"\n" +
			"Warning: this command is generally irreversible and should be used with great care.",
		Args: cmdArgs,
		Run: cmd.RunCmdFunc(func(cmd *cobra.Command, args []string) error {
			ctx := cmd.Context()

			// Destroy is always permitted to fall back to looking for secrets providers in state, since we explicitly
			// want to support use cases where a user is trying to destroy a stack they no longer have configuration for.
			ssml := cmdStack.SecretsManagerLoader{FallbackToState: true}

			ws := pkgWorkspace.Instance

			// Remote implies we're skipping previews.
			if remoteArgs.remote {
				skipPreview = true
			}

			yes = yes || skipPreview || env.SkipConfirmations.Value()
			interactive := cmdutil.Interactive()
			if !interactive && !yes && !previewOnly {
				return errors.New("--yes or --skip-preview or --preview-only " +
					"must be passed in to proceed when running in non-interactive mode")
			}

			opts, err := updateFlagsToOptions(interactive, skipPreview, yes, previewOnly)
			if err != nil {
				return err
			}

			displayType := display.DisplayProgress
			if diffDisplay {
				displayType = display.DisplayDiff
			}

			opts.Display = display.Options{
				Color:                cmdutil.GetGlobalColorization(),
				ShowConfig:           showConfig,
				ShowReplacementSteps: showReplacementSteps,
				ShowSameResources:    showSames,
				SuppressOutputs:      suppressOutputs,
				SuppressProgress:     suppressProgress,
				IsInteractive:        interactive,
				Type:                 displayType,
				EventLogPath:         eventLogPath,
				Debug:                debug,
				JSONDisplay:          jsonDisplay,
			}

			// we only suppress permalinks if the user passes true. the default is an empty string
			// which we pass as 'false'
			if suppressPermalink == "true" {
				opts.Display.SuppressPermalink = true
			} else {
				opts.Display.SuppressPermalink = false
			}

			if remoteArgs.remote {
				err = validateUnsupportedRemoteFlags(false, nil, false, "", jsonDisplay, nil,
					nil, refresh, showConfig, false, showReplacementSteps, showSames, false,
					suppressOutputs, "default", targets, nil, nil,
					targetDependents, "", cmdStack.ConfigFile)
				if err != nil {
					return err
				}

				var url string
				if len(args) > 0 {
					url = args[0]
				}

				if errResult := validateRemoteDeploymentFlags(url, remoteArgs); errResult != nil {
					return errResult
				}

				return runDeployment(ctx, ws, cmd, opts.Display, apitype.Destroy, stackName, url, remoteArgs)
			}

			isDIYBackend, err := cmdBackend.IsDIYBackend(ws, opts.Display)
			if err != nil {
				return err
			}

			// by default, we are going to suppress the permalink when using DIY backends
			// this can be re-enabled by explicitly passing "false" to the `suppress-permalink` flag
			if suppressPermalink != "false" && isDIYBackend {
				opts.Display.SuppressPermalink = true
			}

			s, err := cmdStack.RequireStack(
				ctx,
				ws,
				cmdBackend.DefaultLoginManager,
				stackName,
				cmdStack.LoadOnly,
				opts.Display,
			)
			if err != nil {
				return err
			}

			proj, root, err := ws.ReadProject()
			if err != nil && errors.Is(err, workspace.ErrProjectNotFound) {
				logging.Warningf("failed to find current Pulumi project, continuing with an empty project"+
					"using stack %v from backend %v", s.Ref().Name(), s.Backend().Name())
				projectName, has := s.Ref().Project()
				if !has {
					// If the stack doesn't have a project name (legacy diy) then leave this blank, as
					// we used to.
					projectName = ""
				}
				proj = &workspace.Project{
					Name: tokens.PackageName(projectName),
				}
				root = ""
			} else if err != nil {
				return err
			}

			getConfig := config.GetStackConfiguration
			if stackName != "" {
				// `pulumi destroy --stack <stack>` can be run outside of the project directory.
				// The config may be missing, fallback on the latest configuration in the backend.
				getConfig = config.GetStackConfigurationOrLatest
			}
			cfg, sm, err := getConfig(ctx, ssml, s, proj)
			if err != nil {
				return fmt.Errorf("getting stack configuration: %w", err)
			}

			m, err := metadata.GetUpdateMetadata(message, root, execKind, execAgent, false, cfg, cmd.Flags())
			if err != nil {
				return fmt.Errorf("gathering environment metadata: %w", err)
			}

			decrypter, err := sm.Decrypter()
			if err != nil {
				return fmt.Errorf("getting stack decrypter: %w", err)
			}
			encrypter, err := sm.Encrypter()
			if err != nil {
				return fmt.Errorf("getting stack encrypter: %w", err)
			}

			stackName := s.Ref().Name().String()
			configError := workspace.ValidateStackConfigAndApplyProjectConfig(
				ctx,
				stackName,
				proj,
				cfg.Environment,
				cfg.Config,
				encrypter,
				decrypter)
			if configError != nil {
				return fmt.Errorf("validating stack config: %w", configError)
			}

			refreshOption, err := getRefreshOption(proj, refresh)
			if err != nil {
				return err
			}

			if len(*targets) > 0 && excludeProtected {
				return errors.New("You cannot specify --target and --exclude-protected")
			}

			var protectedCount int
			targetUrns := *targets
			if excludeProtected {
				contract.Assertf(len(targetUrns) == 0, "Expected no target URNs, got %d", len(targetUrns))
				targetUrns, protectedCount, err = handleExcludeProtected(ctx, s)
				if err != nil {
					return err
				} else if protectedCount > 0 && len(targetUrns) == 0 {
					if !jsonDisplay {
						fmt.Printf("There were no unprotected resources to destroy. There are still %d"+
							" protected resources associated with this stack.\n", protectedCount)
					}
					// We need to return now. Otherwise the update will conclude
					// we tried to destroy everything and error for trying to
					// destroy a protected resource.
					return nil
				}
			}

			opts.Engine = engine.UpdateOptions{
				Parallel:                  parallel,
				Debug:                     debug,
				Refresh:                   refreshOption,
				Targets:                   deploy.NewUrnTargets(targetUrns),
				TargetDependents:          targetDependents,
				UseLegacyDiff:             env.EnableLegacyDiff.Value(),
				UseLegacyRefreshDiff:      env.EnableLegacyRefreshDiff.Value(),
				DisableProviderPreview:    env.DisableProviderPreview.Value(),
				DisableResourceReferences: env.DisableResourceReferences.Value(),
				DisableOutputValues:       env.DisableOutputValues.Value(),
				Experimental:              env.Experimental.Value(),
				ContinueOnError:           continueOnError,
			}

			_, destroyErr := s.Destroy(ctx, backend.UpdateOperation{
				Proj:               proj,
				Root:               root,
				M:                  m,
				Opts:               opts,
				StackConfiguration: cfg,
				SecretsManager:     sm,
				SecretsProvider:    stack.DefaultSecretsProvider,
				Scopes:             backend.CancellationScopes,
			})

			if destroyErr == nil && protectedCount > 0 && !jsonDisplay {
				fmt.Printf("All unprotected resources were destroyed. There are still %d protected resources"+
					" associated with this stack.\n", protectedCount)
			} else if destroyErr == nil && len(*targets) == 0 {
				if !jsonDisplay && !remove && !previewOnly {
					fmt.Printf("The resources in the stack have been deleted, but the history and configuration "+
						"associated with the stack are still maintained. \nIf you want to remove the stack "+
						"completely, run `pulumi stack rm %s`.\n", s.Ref())
				} else if remove {
					_, err = s.Remove(ctx, false)
					if err != nil {
						return err
					}
					// Remove also the stack config file.
					if _, path, detectErr := workspace.DetectProjectStackPath(s.Ref().Name().Q()); detectErr == nil {
						if detectErr = os.Remove(path); detectErr != nil && !os.IsNotExist(detectErr) {
							return detectErr
						} else if !jsonDisplay {
							fmt.Printf("The resources in the stack have been deleted, and the history and " +
								"configuration removed.\n")
						}
					}
				}
			} else if destroyErr == context.Canceled {
				return errors.New("destroy cancelled")
			}
			return destroyErr
		}),
	}

	cmd.PersistentFlags().BoolVarP(
		&debug, "debug", "d", false,
		"Print detailed debugging output during resource operations")
	cmd.PersistentFlags().BoolVar(
		&remove, "remove", false,
		"Remove the stack and its config file after all resources in the stack have been deleted")
	cmd.PersistentFlags().StringVarP(
		&stackName, "stack", "s", "",
		"The name of the stack to operate on. Defaults to the current stack")
	cmd.PersistentFlags().StringVar(
		&cmdStack.ConfigFile, "config-file", "",
		"Use the configuration values in the specified file rather than detecting the file name")
	cmd.PersistentFlags().StringVarP(
		&message, "message", "m", "",
		"Optional message to associate with the destroy operation")

	targets = cmd.PersistentFlags().StringArrayP(
		"target", "t", []string{},
		"Specify a single resource URN to destroy. All resources necessary to destroy this target will also be destroyed."+
			" Multiple resources can be specified using: --target urn1 --target urn2."+
			" Wildcards (*, **) are also supported")
	cmd.PersistentFlags().BoolVar(
		&targetDependents, "target-dependents", false,
		"Allows destroying of dependent targets discovered but not specified in --target list")
	cmd.PersistentFlags().BoolVar(&excludeProtected, "exclude-protected", false, "Do not destroy protected resources."+
		" Destroy all other resources.")

	// Flags for engine.UpdateOptions.
	cmd.PersistentFlags().BoolVar(
		&diffDisplay, "diff", false,
		"Display operation as a rich diff showing the overall change")
	cmd.Flags().BoolVarP(
		&jsonDisplay, "json", "j", false,
		"Serialize the destroy diffs, operations, and overall output as JSON")
	cmd.PersistentFlags().Int32VarP(
		&parallel, "parallel", "p", defaultParallel,
		"Allow P resource operations to run in parallel at once (1 for no parallelism).")
	cmd.PersistentFlags().BoolVar(
		&previewOnly, "preview-only", false,
		"Only show a preview of the destroy, but don't perform the destroy itself")
	cmd.PersistentFlags().StringVarP(
		&refresh, "refresh", "r", "",
		"Refresh the state of the stack's resources before this update")
	cmd.PersistentFlags().Lookup("refresh").NoOptDefVal = "true"
	cmd.PersistentFlags().BoolVar(
		&showConfig, "show-config", false,
		"Show configuration keys and variables")
	cmd.PersistentFlags().BoolVar(
		&showReplacementSteps, "show-replacement-steps", false,
		"Show detailed resource replacement creates and deletes instead of a single step")
	cmd.PersistentFlags().BoolVar(
		&showSames, "show-sames", false,
		"Show resources that don't need to be updated because they haven't changed, alongside those that do")
	cmd.PersistentFlags().BoolVarP(
		&skipPreview, "skip-preview", "f", false,
		"Do not calculate a preview before performing the destroy")
	cmd.PersistentFlags().BoolVar(
		&suppressOutputs, "suppress-outputs", false,
		"Suppress display of stack outputs (in case they contain sensitive values)")
	cmd.PersistentFlags().BoolVar(
		&suppressProgress, "suppress-progress", false,
		"Suppress display of periodic progress dots")
	cmd.PersistentFlags().StringVar(
		&suppressPermalink, "suppress-permalink", "",
		"Suppress display of the state permalink")
	cmd.Flag("suppress-permalink").NoOptDefVal = "false"
	cmd.PersistentFlags().BoolVar(
		&continueOnError, "continue-on-error", env.ContinueOnError.Value(),
		"Continue to perform the destroy operation despite the occurrence of errors "+
			"(can also be set with PULUMI_CONTINUE_ON_ERROR env var)")

	cmd.PersistentFlags().BoolVarP(
		&yes, "yes", "y", false,
		"Automatically approve and perform the destroy after previewing it")

	// Remote flags
	remoteArgs.applyFlags(cmd)

	if env.DebugCommands.Value() {
		cmd.PersistentFlags().StringVar(
			&eventLogPath, "event-log", "",
			"Log events to a file at this path")
	}

	// internal flags
	cmd.PersistentFlags().StringVar(&execKind, "exec-kind", "", "")
	// ignore err, only happens if flag does not exist
	_ = cmd.PersistentFlags().MarkHidden("exec-kind")
	cmd.PersistentFlags().StringVar(&execAgent, "exec-agent", "", "")
	// ignore err, only happens if flag does not exist
	_ = cmd.PersistentFlags().MarkHidden("exec-agent")

	return cmd
}

// separateProtected returns a list or unprotected and protected resources respectively. This allows
// us to safely destroy all resources in the unprotected list without invalidating any resource in
// the protected list. Protection is contravarient: A < B where A: Protected => B: Protected, A < B
// where B: Protected !=> A: Protected.
//
// A
// B: Parent = A
// C: Parent = A, Protect = True
// D: Parent = C
//
// -->
//
// Unprotected: B, D
// Protected: A, C
//
// We rely on the fact that `resources` is topologically sorted with respect to its dependencies.
// This function understands that providers live outside this topological sort.
func separateProtected(resources []*resource.State) (
	/*unprotected*/ []*resource.State /*protected*/, []*resource.State,
) {
	dg := graph.NewDependencyGraph(resources)
	transitiveProtected := mapset.NewSet[*resource.State]()
	for _, r := range resources {
		if r.Protect {
			rProtected := dg.TransitiveDependenciesOf(r)
			rProtected.Add(r)
			transitiveProtected = transitiveProtected.Union(rProtected)
		}
	}
	allResources := mapset.NewSet(resources...)
	return allResources.Difference(transitiveProtected).ToSlice(), transitiveProtected.ToSlice()
}

// Returns the number of protected resources that remain. Appends all unprotected resources to `targetUrns`.
func handleExcludeProtected(ctx context.Context, s backend.Stack) ([]string, int, error) {
	// Get snapshot
	snapshot, err := s.Snapshot(ctx, stack.DefaultSecretsProvider)
	if err != nil {
		return nil, 0, err
	} else if snapshot == nil {
		return nil, 0, errors.New("Failed to find the stack snapshot. Are you in a stack?")
	}
	unprotected, protected := separateProtected(snapshot.Resources)
	targetUrns := make([]string, len(unprotected))
	for i, r := range unprotected {
		targetUrns[i] = string(r.URN)
	}
	return targetUrns, len(protected), nil
}
