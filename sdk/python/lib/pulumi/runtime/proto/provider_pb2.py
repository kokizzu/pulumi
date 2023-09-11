# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pulumi/provider.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import plugin_pb2 as pulumi_dot_plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import source_pb2 as pulumi_dot_source__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pulumi/provider.proto\x12\tpulumirpc\x1a\x13pulumi/plugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x13pulumi/source.proto\"#\n\x10GetSchemaRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\"#\n\x11GetSchemaResponse\x12\x0e\n\x06schema\x18\x01 \x01(\t\"\xf4\x01\n\x10\x43onfigureRequest\x12=\n\tvariables\x18\x01 \x03(\x0b\x32*.pulumirpc.ConfigureRequest.VariablesEntry\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\racceptSecrets\x18\x03 \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x04 \x01(\x08\x12\x18\n\x10sends_old_inputs\x18\x05 \x01(\x08\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"s\n\x11\x43onfigureResponse\x12\x15\n\racceptSecrets\x18\x01 \x01(\x08\x12\x17\n\x0fsupportsPreview\x18\x02 \x01(\x08\x12\x17\n\x0f\x61\x63\x63\x65ptResources\x18\x03 \x01(\x08\x12\x15\n\racceptOutputs\x18\x04 \x01(\x08\"\x92\x01\n\x19\x43onfigureErrorMissingKeys\x12\x44\n\x0bmissingKeys\x18\x01 \x03(\x0b\x32/.pulumirpc.ConfigureErrorMissingKeys.MissingKey\x1a/\n\nMissingKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x80\x01\n\rInvokeRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructJ\x04\x08\x03\x10\x07R\x08providerR\x07versionR\x0f\x61\x63\x63\x65ptResourcesR\x11pluginDownloadURL\"d\n\x0eInvokeResponse\x12\'\n\x06return\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"\xef\x05\n\x0b\x43\x61llRequest\x12\x0b\n\x03tok\x18\x01 \x01(\t\x12%\n\x04\x61rgs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x44\n\x0f\x61rgDependencies\x18\x03 \x03(\x0b\x32+.pulumirpc.CallRequest.ArgDependenciesEntry\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x19\n\x11pluginDownloadURL\x18\r \x01(\t\x12\x44\n\x0fpluginChecksums\x18\x10 \x03(\x0b\x32+.pulumirpc.CallRequest.PluginChecksumsEntry\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\r\n\x05stack\x18\x07 \x01(\t\x12\x32\n\x06\x63onfig\x18\x08 \x03(\x0b\x32\".pulumirpc.CallRequest.ConfigEntry\x12\x18\n\x10\x63onfigSecretKeys\x18\t \x03(\t\x12\x0e\n\x06\x64ryRun\x18\n \x01(\x08\x12\x10\n\x08parallel\x18\x0b \x01(\x05\x12\x17\n\x0fmonitorEndpoint\x18\x0c \x01(\t\x12\x14\n\x0corganization\x18\x0e \x01(\t\x12\x31\n\x0esourcePosition\x18\x0f \x01(\x0b\x32\x19.pulumirpc.SourcePosition\x1a$\n\x14\x41rgumentDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a\x63\n\x14\x41rgDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.pulumirpc.CallRequest.ArgumentDependencies:\x02\x38\x01\x1a\x36\n\x14PluginChecksumsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x02\n\x0c\x43\x61llResponse\x12\'\n\x06return\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12K\n\x12returnDependencies\x18\x02 \x03(\x0b\x32/.pulumirpc.CallResponse.ReturnDependenciesEntry\x12)\n\x08\x66\x61ilures\x18\x03 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\x1a\"\n\x12ReturnDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a\x65\n\x17ReturnDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.pulumirpc.CallResponse.ReturnDependencies:\x02\x38\x01\"\x93\x01\n\x0c\x43heckRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12%\n\x04olds\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\nrandomSeed\x18\x05 \x01(\x0cJ\x04\x08\x04\x10\x05R\x0esequenceNumber\"c\n\rCheckResponse\x12\'\n\x06inputs\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x17.pulumirpc.CheckFailure\"0\n\x0c\x43heckFailure\x12\x10\n\x08property\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xb8\x01\n\x0b\x44iffRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\rignoreChanges\x18\x05 \x03(\t\x12+\n\nold_inputs\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xaf\x01\n\x0cPropertyDiff\x12*\n\x04kind\x18\x01 \x01(\x0e\x32\x1c.pulumirpc.PropertyDiff.Kind\x12\x11\n\tinputDiff\x18\x02 \x01(\x08\"`\n\x04Kind\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\x0f\n\x0b\x41\x44\x44_REPLACE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x12\n\x0e\x44\x45LETE_REPLACE\x10\x03\x12\n\n\x06UPDATE\x10\x04\x12\x12\n\x0eUPDATE_REPLACE\x10\x05\"\xfa\x02\n\x0c\x44iffResponse\x12\x10\n\x08replaces\x18\x01 \x03(\t\x12\x0f\n\x07stables\x18\x02 \x03(\t\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\x03 \x01(\x08\x12\x34\n\x07\x63hanges\x18\x04 \x01(\x0e\x32#.pulumirpc.DiffResponse.DiffChanges\x12\r\n\x05\x64iffs\x18\x05 \x03(\t\x12?\n\x0c\x64\x65tailedDiff\x18\x06 \x03(\x0b\x32).pulumirpc.DiffResponse.DetailedDiffEntry\x12\x17\n\x0fhasDetailedDiff\x18\x07 \x01(\x08\x1aL\n\x11\x44\x65tailedDiffEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.pulumirpc.PropertyDiff:\x02\x38\x01\"=\n\x0b\x44iffChanges\x12\x10\n\x0c\x44IFF_UNKNOWN\x10\x00\x12\r\n\tDIFF_NONE\x10\x01\x12\r\n\tDIFF_SOME\x10\x02\"k\n\rCreateRequest\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x0f\n\x07preview\x18\x04 \x01(\x08\"I\n\x0e\x43reateResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"|\n\x0bReadRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06inputs\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"p\n\x0cReadResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06inputs\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xdc\x01\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12%\n\x04olds\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04news\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x05 \x01(\x01\x12\x15\n\rignoreChanges\x18\x06 \x03(\t\x12\x0f\n\x07preview\x18\x07 \x01(\x08\x12+\n\nold_inputs\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\"=\n\x0eUpdateResponse\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"f\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03urn\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\"\x86\x08\n\x10\x43onstructRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05stack\x18\x02 \x01(\t\x12\x37\n\x06\x63onfig\x18\x03 \x03(\x0b\x32\'.pulumirpc.ConstructRequest.ConfigEntry\x12\x0e\n\x06\x64ryRun\x18\x04 \x01(\x08\x12\x10\n\x08parallel\x18\x05 \x01(\x05\x12\x17\n\x0fmonitorEndpoint\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0e\n\x06parent\x18\t \x01(\t\x12\'\n\x06inputs\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12M\n\x11inputDependencies\x18\x0b \x03(\x0b\x32\x32.pulumirpc.ConstructRequest.InputDependenciesEntry\x12=\n\tproviders\x18\r \x03(\x0b\x32*.pulumirpc.ConstructRequest.ProvidersEntry\x12\x14\n\x0c\x64\x65pendencies\x18\x0f \x03(\t\x12\x18\n\x10\x63onfigSecretKeys\x18\x10 \x03(\t\x12\x14\n\x0corganization\x18\x11 \x01(\t\x12\x0f\n\x07protect\x18\x0c \x01(\x08\x12\x0f\n\x07\x61liases\x18\x0e \x03(\t\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\x12 \x03(\t\x12\x42\n\x0e\x63ustomTimeouts\x18\x13 \x01(\x0b\x32*.pulumirpc.ConstructRequest.CustomTimeouts\x12\x13\n\x0b\x64\x65letedWith\x18\x14 \x01(\t\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\x15 \x01(\x08\x12\x15\n\rignoreChanges\x18\x16 \x03(\t\x12\x18\n\x10replaceOnChanges\x18\x17 \x03(\t\x12\x16\n\x0eretainOnDelete\x18\x18 \x01(\x08\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1a@\n\x0e\x43ustomTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\t\x12\x0e\n\x06update\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\t\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aj\n\x16InputDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.pulumirpc.ConstructRequest.PropertyDependencies:\x02\x38\x01\x1a\x30\n\x0eProvidersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xab\x02\n\x11\x43onstructResponse\x12\x0b\n\x03urn\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12N\n\x11stateDependencies\x18\x03 \x03(\x0b\x32\x33.pulumirpc.ConstructResponse.StateDependenciesEntry\x1a$\n\x14PropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\x1ak\n\x16StateDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.pulumirpc.ConstructResponse.PropertyDependencies:\x02\x38\x01\"\x8c\x01\n\x17\x45rrorResourceInitFailed\x12\n\n\x02id\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07reasons\x18\x03 \x03(\t\x12\'\n\x06inputs\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\" \n\x11GetMappingRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"4\n\x12GetMappingResponse\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x32\xb6\t\n\x10ResourceProvider\x12H\n\tGetSchema\x12\x1b.pulumirpc.GetSchemaRequest\x1a\x1c.pulumirpc.GetSchemaResponse\"\x00\x12\x42\n\x0b\x43heckConfig\x12\x17.pulumirpc.CheckRequest\x1a\x18.pulumirpc.CheckResponse\"\x00\x12?\n\nDiffConfig\x12\x16.pulumirpc.DiffRequest\x1a\x17.pulumirpc.DiffResponse\"\x00\x12H\n\tConfigure\x12\x1b.pulumirpc.ConfigureRequest\x1a\x1c.pulumirpc.ConfigureResponse\"\x00\x12?\n\x06Invoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x12G\n\x0cStreamInvoke\x12\x18.pulumirpc.InvokeRequest\x1a\x19.pulumirpc.InvokeResponse\"\x00\x30\x01\x12\x39\n\x04\x43\x61ll\x12\x16.pulumirpc.CallRequest\x1a\x17.pulumirpc.CallResponse\"\x00\x12<\n\x05\x43heck\x12\x17.pulumirpc.CheckRequest\x1a\x18.pulumirpc.CheckResponse\"\x00\x12\x39\n\x04\x44iff\x12\x16.pulumirpc.DiffRequest\x1a\x17.pulumirpc.DiffResponse\"\x00\x12?\n\x06\x43reate\x12\x18.pulumirpc.CreateRequest\x1a\x19.pulumirpc.CreateResponse\"\x00\x12\x39\n\x04Read\x12\x16.pulumirpc.ReadRequest\x1a\x17.pulumirpc.ReadResponse\"\x00\x12?\n\x06Update\x12\x18.pulumirpc.UpdateRequest\x1a\x19.pulumirpc.UpdateResponse\"\x00\x12<\n\x06\x44\x65lete\x12\x18.pulumirpc.DeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\tConstruct\x12\x1b.pulumirpc.ConstructRequest\x1a\x1c.pulumirpc.ConstructResponse\"\x00\x12:\n\x06\x43\x61ncel\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x12;\n\x06\x41ttach\x12\x17.pulumirpc.PluginAttach\x1a\x16.google.protobuf.Empty\"\x00\x12K\n\nGetMapping\x12\x1c.pulumirpc.GetMappingRequest\x1a\x1d.pulumirpc.GetMappingResponse\"\x00\x42\x34Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pulumi.provider_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/pulumi/pulumi/sdk/v3/proto/go;pulumirpc'
  _CONFIGUREREQUEST_VARIABLESENTRY._options = None
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_options = b'8\001'
  _CALLREQUEST_ARGDEPENDENCIESENTRY._options = None
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_options = b'8\001'
  _CALLREQUEST_PLUGINCHECKSUMSENTRY._options = None
  _CALLREQUEST_PLUGINCHECKSUMSENTRY._serialized_options = b'8\001'
  _CALLREQUEST_CONFIGENTRY._options = None
  _CALLREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._options = None
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_options = b'8\001'
  _DIFFRESPONSE_DETAILEDDIFFENTRY._options = None
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_CONFIGENTRY._options = None
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._options = None
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_options = b'8\001'
  _CONSTRUCTREQUEST_PROVIDERSENTRY._options = None
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_options = b'8\001'
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._options = None
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_options = b'8\001'
  _GETSCHEMAREQUEST._serialized_start=137
  _GETSCHEMAREQUEST._serialized_end=172
  _GETSCHEMARESPONSE._serialized_start=174
  _GETSCHEMARESPONSE._serialized_end=209
  _CONFIGUREREQUEST._serialized_start=212
  _CONFIGUREREQUEST._serialized_end=456
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_start=408
  _CONFIGUREREQUEST_VARIABLESENTRY._serialized_end=456
  _CONFIGURERESPONSE._serialized_start=458
  _CONFIGURERESPONSE._serialized_end=573
  _CONFIGUREERRORMISSINGKEYS._serialized_start=576
  _CONFIGUREERRORMISSINGKEYS._serialized_end=722
  _CONFIGUREERRORMISSINGKEYS_MISSINGKEY._serialized_start=675
  _CONFIGUREERRORMISSINGKEYS_MISSINGKEY._serialized_end=722
  _INVOKEREQUEST._serialized_start=725
  _INVOKEREQUEST._serialized_end=853
  _INVOKERESPONSE._serialized_start=855
  _INVOKERESPONSE._serialized_end=955
  _CALLREQUEST._serialized_start=958
  _CALLREQUEST._serialized_end=1709
  _CALLREQUEST_ARGUMENTDEPENDENCIES._serialized_start=1469
  _CALLREQUEST_ARGUMENTDEPENDENCIES._serialized_end=1505
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_start=1507
  _CALLREQUEST_ARGDEPENDENCIESENTRY._serialized_end=1606
  _CALLREQUEST_PLUGINCHECKSUMSENTRY._serialized_start=1608
  _CALLREQUEST_PLUGINCHECKSUMSENTRY._serialized_end=1662
  _CALLREQUEST_CONFIGENTRY._serialized_start=1664
  _CALLREQUEST_CONFIGENTRY._serialized_end=1709
  _CALLRESPONSE._serialized_start=1712
  _CALLRESPONSE._serialized_end=2026
  _CALLRESPONSE_RETURNDEPENDENCIES._serialized_start=1889
  _CALLRESPONSE_RETURNDEPENDENCIES._serialized_end=1923
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_start=1925
  _CALLRESPONSE_RETURNDEPENDENCIESENTRY._serialized_end=2026
  _CHECKREQUEST._serialized_start=2029
  _CHECKREQUEST._serialized_end=2176
  _CHECKRESPONSE._serialized_start=2178
  _CHECKRESPONSE._serialized_end=2277
  _CHECKFAILURE._serialized_start=2279
  _CHECKFAILURE._serialized_end=2327
  _DIFFREQUEST._serialized_start=2330
  _DIFFREQUEST._serialized_end=2514
  _PROPERTYDIFF._serialized_start=2517
  _PROPERTYDIFF._serialized_end=2692
  _PROPERTYDIFF_KIND._serialized_start=2596
  _PROPERTYDIFF_KIND._serialized_end=2692
  _DIFFRESPONSE._serialized_start=2695
  _DIFFRESPONSE._serialized_end=3073
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_start=2934
  _DIFFRESPONSE_DETAILEDDIFFENTRY._serialized_end=3010
  _DIFFRESPONSE_DIFFCHANGES._serialized_start=3012
  _DIFFRESPONSE_DIFFCHANGES._serialized_end=3073
  _CREATEREQUEST._serialized_start=3075
  _CREATEREQUEST._serialized_end=3182
  _CREATERESPONSE._serialized_start=3184
  _CREATERESPONSE._serialized_end=3257
  _READREQUEST._serialized_start=3259
  _READREQUEST._serialized_end=3383
  _READRESPONSE._serialized_start=3385
  _READRESPONSE._serialized_end=3497
  _UPDATEREQUEST._serialized_start=3500
  _UPDATEREQUEST._serialized_end=3720
  _UPDATERESPONSE._serialized_start=3722
  _UPDATERESPONSE._serialized_end=3783
  _DELETEREQUEST._serialized_start=3785
  _DELETEREQUEST._serialized_end=3887
  _CONSTRUCTREQUEST._serialized_start=3890
  _CONSTRUCTREQUEST._serialized_end=4920
  _CONSTRUCTREQUEST_PROPERTYDEPENDENCIES._serialized_start=4613
  _CONSTRUCTREQUEST_PROPERTYDEPENDENCIES._serialized_end=4649
  _CONSTRUCTREQUEST_CUSTOMTIMEOUTS._serialized_start=4651
  _CONSTRUCTREQUEST_CUSTOMTIMEOUTS._serialized_end=4715
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_start=1664
  _CONSTRUCTREQUEST_CONFIGENTRY._serialized_end=1709
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_start=4764
  _CONSTRUCTREQUEST_INPUTDEPENDENCIESENTRY._serialized_end=4870
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_start=4872
  _CONSTRUCTREQUEST_PROVIDERSENTRY._serialized_end=4920
  _CONSTRUCTRESPONSE._serialized_start=4923
  _CONSTRUCTRESPONSE._serialized_end=5222
  _CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES._serialized_start=4613
  _CONSTRUCTRESPONSE_PROPERTYDEPENDENCIES._serialized_end=4649
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_start=5115
  _CONSTRUCTRESPONSE_STATEDEPENDENCIESENTRY._serialized_end=5222
  _ERRORRESOURCEINITFAILED._serialized_start=5225
  _ERRORRESOURCEINITFAILED._serialized_end=5365
  _GETMAPPINGREQUEST._serialized_start=5367
  _GETMAPPINGREQUEST._serialized_end=5399
  _GETMAPPINGRESPONSE._serialized_start=5401
  _GETMAPPINGRESPONSE._serialized_end=5453
  _RESOURCEPROVIDER._serialized_start=5456
  _RESOURCEPROVIDER._serialized_end=6662
# @@protoc_insertion_point(module_scope)
