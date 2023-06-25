# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/storeforward.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmeshtastic/storeforward.proto\x12\nmeshtastic\"\xea\x06\n\x0fStoreAndForward\x12\x37\n\x02rr\x18\x01 \x01(\x0e\x32+.meshtastic.StoreAndForward.RequestResponse\x12\x37\n\x05stats\x18\x02 \x01(\x0b\x32&.meshtastic.StoreAndForward.StatisticsH\x00\x12\x36\n\x07history\x18\x03 \x01(\x0b\x32#.meshtastic.StoreAndForward.HistoryH\x00\x12:\n\theartbeat\x18\x04 \x01(\x0b\x32%.meshtastic.StoreAndForward.HeartbeatH\x00\x12\x0f\n\x05\x65mpty\x18\x05 \x01(\x08H\x00\x1a\xcd\x01\n\nStatistics\x12\x16\n\x0emessages_total\x18\x01 \x01(\r\x12\x16\n\x0emessages_saved\x18\x02 \x01(\r\x12\x14\n\x0cmessages_max\x18\x03 \x01(\r\x12\x0f\n\x07up_time\x18\x04 \x01(\r\x12\x10\n\x08requests\x18\x05 \x01(\r\x12\x18\n\x10requests_history\x18\x06 \x01(\r\x12\x11\n\theartbeat\x18\x07 \x01(\x08\x12\x12\n\nreturn_max\x18\x08 \x01(\r\x12\x15\n\rreturn_window\x18\t \x01(\r\x1aI\n\x07History\x12\x18\n\x10history_messages\x18\x01 \x01(\r\x12\x0e\n\x06window\x18\x02 \x01(\r\x12\x14\n\x0clast_request\x18\x03 \x01(\r\x1a.\n\tHeartbeat\x12\x0e\n\x06period\x18\x01 \x01(\r\x12\x11\n\tsecondary\x18\x02 \x01(\r\"\x89\x02\n\x0fRequestResponse\x12\t\n\x05UNSET\x10\x00\x12\x10\n\x0cROUTER_ERROR\x10\x01\x12\x14\n\x10ROUTER_HEARTBEAT\x10\x02\x12\x0f\n\x0bROUTER_PING\x10\x03\x12\x0f\n\x0bROUTER_PONG\x10\x04\x12\x0f\n\x0bROUTER_BUSY\x10\x05\x12\x12\n\x0eROUTER_HISTORY\x10\x06\x12\x10\n\x0cROUTER_STATS\x10\x07\x12\x10\n\x0c\x43LIENT_ERROR\x10@\x12\x12\n\x0e\x43LIENT_HISTORY\x10\x41\x12\x10\n\x0c\x43LIENT_STATS\x10\x42\x12\x0f\n\x0b\x43LIENT_PING\x10\x43\x12\x0f\n\x0b\x43LIENT_PONG\x10\x44\x12\x10\n\x0c\x43LIENT_ABORT\x10jB\t\n\x07variantBj\n\x13\x63om.geeksville.meshB\x15StoreAndForwardProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')



_STOREANDFORWARD = DESCRIPTOR.message_types_by_name['StoreAndForward']
_STOREANDFORWARD_STATISTICS = _STOREANDFORWARD.nested_types_by_name['Statistics']
_STOREANDFORWARD_HISTORY = _STOREANDFORWARD.nested_types_by_name['History']
_STOREANDFORWARD_HEARTBEAT = _STOREANDFORWARD.nested_types_by_name['Heartbeat']
_STOREANDFORWARD_REQUESTRESPONSE = _STOREANDFORWARD.enum_types_by_name['RequestResponse']
StoreAndForward = _reflection.GeneratedProtocolMessageType('StoreAndForward', (_message.Message,), {

  'Statistics' : _reflection.GeneratedProtocolMessageType('Statistics', (_message.Message,), {
    'DESCRIPTOR' : _STOREANDFORWARD_STATISTICS,
    '__module__' : 'meshtastic.storeforward_pb2'
    # @@protoc_insertion_point(class_scope:meshtastic.StoreAndForward.Statistics)
    })
  ,

  'History' : _reflection.GeneratedProtocolMessageType('History', (_message.Message,), {
    'DESCRIPTOR' : _STOREANDFORWARD_HISTORY,
    '__module__' : 'meshtastic.storeforward_pb2'
    # @@protoc_insertion_point(class_scope:meshtastic.StoreAndForward.History)
    })
  ,

  'Heartbeat' : _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
    'DESCRIPTOR' : _STOREANDFORWARD_HEARTBEAT,
    '__module__' : 'meshtastic.storeforward_pb2'
    # @@protoc_insertion_point(class_scope:meshtastic.StoreAndForward.Heartbeat)
    })
  ,
  'DESCRIPTOR' : _STOREANDFORWARD,
  '__module__' : 'meshtastic.storeforward_pb2'
  # @@protoc_insertion_point(class_scope:meshtastic.StoreAndForward)
  })
_sym_db.RegisterMessage(StoreAndForward)
_sym_db.RegisterMessage(StoreAndForward.Statistics)
_sym_db.RegisterMessage(StoreAndForward.History)
_sym_db.RegisterMessage(StoreAndForward.Heartbeat)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\025StoreAndForwardProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _STOREANDFORWARD._serialized_start=46
  _STOREANDFORWARD._serialized_end=920
  _STOREANDFORWARD_STATISTICS._serialized_start=313
  _STOREANDFORWARD_STATISTICS._serialized_end=518
  _STOREANDFORWARD_HISTORY._serialized_start=520
  _STOREANDFORWARD_HISTORY._serialized_end=593
  _STOREANDFORWARD_HEARTBEAT._serialized_start=595
  _STOREANDFORWARD_HEARTBEAT._serialized_end=641
  _STOREANDFORWARD_REQUESTRESPONSE._serialized_start=644
  _STOREANDFORWARD_REQUESTRESPONSE._serialized_end=909
# @@protoc_insertion_point(module_scope)
