# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clusterspecgen.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='clusterspecgen.proto',
  package='clusterspecgen',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x63lusterspecgen.proto\x12\x0e\x63lusterspecgen\"^\n\tContainer\x12\x13\n\x0b\x63ontainerId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x0f\n\x07jobName\x18\x04 \x01(\t\x12\x11\n\ttaskIndex\x18\x05 \x01(\t\"H\n\x18RegisterContainerRequest\x12,\n\tcontainer\x18\x01 \x01(\x0b\x32\x19.clusterspecgen.Container\"\x18\n\x16RegisterContainerReply\"\x17\n\x15GetClusterSpecRequest\"E\n\x13GetClusterSpecReply\x12.\n\x0b\x63lusterSpec\x18\x01 \x03(\x0b\x32\x19.clusterspecgen.Container2\xd5\x01\n\x0e\x43lusterSpecGen\x12\x65\n\x11RegisterContainer\x12(.clusterspecgen.RegisterContainerRequest\x1a&.clusterspecgen.RegisterContainerReply\x12\\\n\x0eGetClusterSpec\x12%.clusterspecgen.GetClusterSpecRequest\x1a#.clusterspecgen.GetClusterSpecReplyB@\n!io.hops.tensorflow.clusterspecgenB\x13\x43lusterSpecGenProtoP\x01\xa2\x02\x03\x43SGb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='clusterspecgen.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='containerId', full_name='clusterspecgen.Container.containerId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='clusterspecgen.Container.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='clusterspecgen.Container.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jobName', full_name='clusterspecgen.Container.jobName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='taskIndex', full_name='clusterspecgen.Container.taskIndex', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=134,
)


_REGISTERCONTAINERREQUEST = _descriptor.Descriptor(
  name='RegisterContainerRequest',
  full_name='clusterspecgen.RegisterContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='clusterspecgen.RegisterContainerRequest.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=208,
)


_REGISTERCONTAINERREPLY = _descriptor.Descriptor(
  name='RegisterContainerReply',
  full_name='clusterspecgen.RegisterContainerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=234,
)


_GETCLUSTERSPECREQUEST = _descriptor.Descriptor(
  name='GetClusterSpecRequest',
  full_name='clusterspecgen.GetClusterSpecRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=259,
)


_GETCLUSTERSPECREPLY = _descriptor.Descriptor(
  name='GetClusterSpecReply',
  full_name='clusterspecgen.GetClusterSpecReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clusterSpec', full_name='clusterspecgen.GetClusterSpecReply.clusterSpec', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=330,
)

_REGISTERCONTAINERREQUEST.fields_by_name['container'].message_type = _CONTAINER
_GETCLUSTERSPECREPLY.fields_by_name['clusterSpec'].message_type = _CONTAINER
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['RegisterContainerRequest'] = _REGISTERCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['RegisterContainerReply'] = _REGISTERCONTAINERREPLY
DESCRIPTOR.message_types_by_name['GetClusterSpecRequest'] = _GETCLUSTERSPECREQUEST
DESCRIPTOR.message_types_by_name['GetClusterSpecReply'] = _GETCLUSTERSPECREPLY

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINER,
  __module__ = 'clusterspecgen_pb2'
  # @@protoc_insertion_point(class_scope:clusterspecgen.Container)
  ))
_sym_db.RegisterMessage(Container)

RegisterContainerRequest = _reflection.GeneratedProtocolMessageType('RegisterContainerRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERCONTAINERREQUEST,
  __module__ = 'clusterspecgen_pb2'
  # @@protoc_insertion_point(class_scope:clusterspecgen.RegisterContainerRequest)
  ))
_sym_db.RegisterMessage(RegisterContainerRequest)

RegisterContainerReply = _reflection.GeneratedProtocolMessageType('RegisterContainerReply', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERCONTAINERREPLY,
  __module__ = 'clusterspecgen_pb2'
  # @@protoc_insertion_point(class_scope:clusterspecgen.RegisterContainerReply)
  ))
_sym_db.RegisterMessage(RegisterContainerReply)

GetClusterSpecRequest = _reflection.GeneratedProtocolMessageType('GetClusterSpecRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTERSPECREQUEST,
  __module__ = 'clusterspecgen_pb2'
  # @@protoc_insertion_point(class_scope:clusterspecgen.GetClusterSpecRequest)
  ))
_sym_db.RegisterMessage(GetClusterSpecRequest)

GetClusterSpecReply = _reflection.GeneratedProtocolMessageType('GetClusterSpecReply', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTERSPECREPLY,
  __module__ = 'clusterspecgen_pb2'
  # @@protoc_insertion_point(class_scope:clusterspecgen.GetClusterSpecReply)
  ))
_sym_db.RegisterMessage(GetClusterSpecReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.hops.tensorflow.clusterspecgenB\023ClusterSpecGenProtoP\001\242\002\003CSG'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class ClusterSpecGenStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.RegisterContainer = channel.unary_unary(
          '/clusterspecgen.ClusterSpecGen/RegisterContainer',
          request_serializer=RegisterContainerRequest.SerializeToString,
          response_deserializer=RegisterContainerReply.FromString,
          )
      self.GetClusterSpec = channel.unary_unary(
          '/clusterspecgen.ClusterSpecGen/GetClusterSpec',
          request_serializer=GetClusterSpecRequest.SerializeToString,
          response_deserializer=GetClusterSpecReply.FromString,
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
            request_deserializer=RegisterContainerRequest.FromString,
            response_serializer=RegisterContainerReply.SerializeToString,
        ),
        'GetClusterSpec': grpc.unary_unary_rpc_method_handler(
            servicer.GetClusterSpec,
            request_deserializer=GetClusterSpecRequest.FromString,
            response_serializer=GetClusterSpecReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'clusterspecgen.ClusterSpecGen', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaClusterSpecGenServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def RegisterContainer(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetClusterSpec(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaClusterSpecGenStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def RegisterContainer(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    RegisterContainer.future = None
    def GetClusterSpec(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetClusterSpec.future = None


  def beta_create_ClusterSpecGen_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('clusterspecgen.ClusterSpecGen', 'GetClusterSpec'): GetClusterSpecRequest.FromString,
      ('clusterspecgen.ClusterSpecGen', 'RegisterContainer'): RegisterContainerRequest.FromString,
    }
    response_serializers = {
      ('clusterspecgen.ClusterSpecGen', 'GetClusterSpec'): GetClusterSpecReply.SerializeToString,
      ('clusterspecgen.ClusterSpecGen', 'RegisterContainer'): RegisterContainerReply.SerializeToString,
    }
    method_implementations = {
      ('clusterspecgen.ClusterSpecGen', 'GetClusterSpec'): face_utilities.unary_unary_inline(servicer.GetClusterSpec),
      ('clusterspecgen.ClusterSpecGen', 'RegisterContainer'): face_utilities.unary_unary_inline(servicer.RegisterContainer),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_ClusterSpecGen_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('clusterspecgen.ClusterSpecGen', 'GetClusterSpec'): GetClusterSpecRequest.SerializeToString,
      ('clusterspecgen.ClusterSpecGen', 'RegisterContainer'): RegisterContainerRequest.SerializeToString,
    }
    response_deserializers = {
      ('clusterspecgen.ClusterSpecGen', 'GetClusterSpec'): GetClusterSpecReply.FromString,
      ('clusterspecgen.ClusterSpecGen', 'RegisterContainer'): RegisterContainerReply.FromString,
    }
    cardinalities = {
      'GetClusterSpec': cardinality.Cardinality.UNARY_UNARY,
      'RegisterContainer': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'clusterspecgen.ClusterSpecGen', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)