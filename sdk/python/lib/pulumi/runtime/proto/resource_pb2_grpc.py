# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import callback_pb2 as pulumi_dot_callback__pb2
from . import provider_pb2 as pulumi_dot_provider__pb2
from . import resource_pb2 as pulumi_dot_resource__pb2


class ResourceMonitorStub(object):
    """ResourceMonitor is the interface a source uses to talk back to the planning monitor orchestrating the execution.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SupportsFeature = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/SupportsFeature',
                request_serializer=pulumi_dot_resource__pb2.SupportsFeatureRequest.SerializeToString,
                response_deserializer=pulumi_dot_resource__pb2.SupportsFeatureResponse.FromString,
                )
        self.Invoke = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/Invoke',
                request_serializer=pulumi_dot_resource__pb2.ResourceInvokeRequest.SerializeToString,
                response_deserializer=pulumi_dot_provider__pb2.InvokeResponse.FromString,
                )
        self.StreamInvoke = channel.unary_stream(
                '/pulumirpc.ResourceMonitor/StreamInvoke',
                request_serializer=pulumi_dot_resource__pb2.ResourceInvokeRequest.SerializeToString,
                response_deserializer=pulumi_dot_provider__pb2.InvokeResponse.FromString,
                )
        self.Call = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/Call',
                request_serializer=pulumi_dot_resource__pb2.ResourceCallRequest.SerializeToString,
                response_deserializer=pulumi_dot_provider__pb2.CallResponse.FromString,
                )
        self.ReadResource = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/ReadResource',
                request_serializer=pulumi_dot_resource__pb2.ReadResourceRequest.SerializeToString,
                response_deserializer=pulumi_dot_resource__pb2.ReadResourceResponse.FromString,
                )
        self.RegisterResource = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/RegisterResource',
                request_serializer=pulumi_dot_resource__pb2.RegisterResourceRequest.SerializeToString,
                response_deserializer=pulumi_dot_resource__pb2.RegisterResourceResponse.FromString,
                )
        self.RegisterResourceOutputs = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/RegisterResourceOutputs',
                request_serializer=pulumi_dot_resource__pb2.RegisterResourceOutputsRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RegisterStackTransform = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/RegisterStackTransform',
                request_serializer=pulumi_dot_callback__pb2.Callback.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RegisterPackage = channel.unary_unary(
                '/pulumirpc.ResourceMonitor/RegisterPackage',
                request_serializer=pulumi_dot_resource__pb2.RegisterPackageRequest.SerializeToString,
                response_deserializer=pulumi_dot_resource__pb2.RegisterPackageResponse.FromString,
                )


class ResourceMonitorServicer(object):
    """ResourceMonitor is the interface a source uses to talk back to the planning monitor orchestrating the execution.
    """

    def SupportsFeature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamInvoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadResource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterResource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterResourceOutputs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterStackTransform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPackage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceMonitorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SupportsFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.SupportsFeature,
                    request_deserializer=pulumi_dot_resource__pb2.SupportsFeatureRequest.FromString,
                    response_serializer=pulumi_dot_resource__pb2.SupportsFeatureResponse.SerializeToString,
            ),
            'Invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Invoke,
                    request_deserializer=pulumi_dot_resource__pb2.ResourceInvokeRequest.FromString,
                    response_serializer=pulumi_dot_provider__pb2.InvokeResponse.SerializeToString,
            ),
            'StreamInvoke': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamInvoke,
                    request_deserializer=pulumi_dot_resource__pb2.ResourceInvokeRequest.FromString,
                    response_serializer=pulumi_dot_provider__pb2.InvokeResponse.SerializeToString,
            ),
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=pulumi_dot_resource__pb2.ResourceCallRequest.FromString,
                    response_serializer=pulumi_dot_provider__pb2.CallResponse.SerializeToString,
            ),
            'ReadResource': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadResource,
                    request_deserializer=pulumi_dot_resource__pb2.ReadResourceRequest.FromString,
                    response_serializer=pulumi_dot_resource__pb2.ReadResourceResponse.SerializeToString,
            ),
            'RegisterResource': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterResource,
                    request_deserializer=pulumi_dot_resource__pb2.RegisterResourceRequest.FromString,
                    response_serializer=pulumi_dot_resource__pb2.RegisterResourceResponse.SerializeToString,
            ),
            'RegisterResourceOutputs': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterResourceOutputs,
                    request_deserializer=pulumi_dot_resource__pb2.RegisterResourceOutputsRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RegisterStackTransform': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterStackTransform,
                    request_deserializer=pulumi_dot_callback__pb2.Callback.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RegisterPackage': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPackage,
                    request_deserializer=pulumi_dot_resource__pb2.RegisterPackageRequest.FromString,
                    response_serializer=pulumi_dot_resource__pb2.RegisterPackageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pulumirpc.ResourceMonitor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ResourceMonitor(object):
    """ResourceMonitor is the interface a source uses to talk back to the planning monitor orchestrating the execution.
    """

    @staticmethod
    def SupportsFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/SupportsFeature',
            pulumi_dot_resource__pb2.SupportsFeatureRequest.SerializeToString,
            pulumi_dot_resource__pb2.SupportsFeatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/Invoke',
            pulumi_dot_resource__pb2.ResourceInvokeRequest.SerializeToString,
            pulumi_dot_provider__pb2.InvokeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamInvoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pulumirpc.ResourceMonitor/StreamInvoke',
            pulumi_dot_resource__pb2.ResourceInvokeRequest.SerializeToString,
            pulumi_dot_provider__pb2.InvokeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/Call',
            pulumi_dot_resource__pb2.ResourceCallRequest.SerializeToString,
            pulumi_dot_provider__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/ReadResource',
            pulumi_dot_resource__pb2.ReadResourceRequest.SerializeToString,
            pulumi_dot_resource__pb2.ReadResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterResource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/RegisterResource',
            pulumi_dot_resource__pb2.RegisterResourceRequest.SerializeToString,
            pulumi_dot_resource__pb2.RegisterResourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterResourceOutputs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/RegisterResourceOutputs',
            pulumi_dot_resource__pb2.RegisterResourceOutputsRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterStackTransform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/RegisterStackTransform',
            pulumi_dot_callback__pb2.Callback.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterPackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pulumirpc.ResourceMonitor/RegisterPackage',
            pulumi_dot_resource__pb2.RegisterPackageRequest.SerializeToString,
            pulumi_dot_resource__pb2.RegisterPackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
