# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import clusterspecgen_pb2 as clusterspecgen__pb2


class ClusterSpecGenStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterContainer = channel.unary_unary(
        '/clusterspecgen.ClusterSpecGen/RegisterContainer',
        request_serializer=clusterspecgen__pb2.RegisterContainerRequest.SerializeToString,
        response_deserializer=clusterspecgen__pb2.RegisterContainerReply.FromString,
        )
    self.GetClusterSpec = channel.unary_unary(
        '/clusterspecgen.ClusterSpecGen/GetClusterSpec',
        request_serializer=clusterspecgen__pb2.GetClusterSpecRequest.SerializeToString,
        response_deserializer=clusterspecgen__pb2.GetClusterSpecReply.FromString,
        )


class ClusterSpecGenServicer(object):

  def RegisterContainer(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetClusterSpec(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClusterSpecGenServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterContainer': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterContainer,
          request_deserializer=clusterspecgen__pb2.RegisterContainerRequest.FromString,
          response_serializer=clusterspecgen__pb2.RegisterContainerReply.SerializeToString,
      ),
      'GetClusterSpec': grpc.unary_unary_rpc_method_handler(
          servicer.GetClusterSpec,
          request_deserializer=clusterspecgen__pb2.GetClusterSpecRequest.FromString,
          response_serializer=clusterspecgen__pb2.GetClusterSpecReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'clusterspecgen.ClusterSpecGen', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))