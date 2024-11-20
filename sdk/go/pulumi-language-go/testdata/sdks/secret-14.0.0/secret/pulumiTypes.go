// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package secret

import (
	"context"
	"reflect"

	"example.com/pulumi-secret/sdk/go/v14/secret/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type Data struct {
	Private string `pulumi:"private"`
	Public  string `pulumi:"public"`
}

// DataInput is an input type that accepts DataArgs and DataOutput values.
// You can construct a concrete instance of `DataInput` via:
//
//	DataArgs{...}
type DataInput interface {
	pulumi.Input

	ToDataOutput() DataOutput
	ToDataOutputWithContext(context.Context) DataOutput
}

type DataArgs struct {
	Private pulumi.StringInput `pulumi:"private"`
	Public  pulumi.StringInput `pulumi:"public"`
}

func (DataArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*Data)(nil)).Elem()
}

func (i DataArgs) ToDataOutput() DataOutput {
	return i.ToDataOutputWithContext(context.Background())
}

func (i DataArgs) ToDataOutputWithContext(ctx context.Context) DataOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataOutput)
}

type DataOutput struct{ *pulumi.OutputState }

func (DataOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Data)(nil)).Elem()
}

func (o DataOutput) ToDataOutput() DataOutput {
	return o
}

func (o DataOutput) ToDataOutputWithContext(ctx context.Context) DataOutput {
	return o
}

func (o DataOutput) Private() pulumi.StringOutput {
	return o.ApplyT(func(v Data) string { return v.Private }).(pulumi.StringOutput)
}

func (o DataOutput) Public() pulumi.StringOutput {
	return o.ApplyT(func(v Data) string { return v.Public }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataInput)(nil)).Elem(), DataArgs{})
	pulumi.RegisterOutputType(DataOutput{})
}
