# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import text_pb2 as text__pb2


class TextServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendText1 = channel.unary_unary(
                '/TextService/sendText1',
                request_serializer=text__pb2.TextRequest1.SerializeToString,
                response_deserializer=text__pb2.TextResponse1.FromString,
                )
        self.sendText2 = channel.unary_unary(
                '/TextService/sendText2',
                request_serializer=text__pb2.TextRequest2.SerializeToString,
                response_deserializer=text__pb2.TextResponse2.FromString,
                )


class TextServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendText1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendText2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendText1': grpc.unary_unary_rpc_method_handler(
                    servicer.sendText1,
                    request_deserializer=text__pb2.TextRequest1.FromString,
                    response_serializer=text__pb2.TextResponse1.SerializeToString,
            ),
            'sendText2': grpc.unary_unary_rpc_method_handler(
                    servicer.sendText2,
                    request_deserializer=text__pb2.TextRequest2.FromString,
                    response_serializer=text__pb2.TextResponse2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendText1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextService/sendText1',
            text__pb2.TextRequest1.SerializeToString,
            text__pb2.TextResponse1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendText2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextService/sendText2',
            text__pb2.TextRequest2.SerializeToString,
            text__pb2.TextResponse2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)