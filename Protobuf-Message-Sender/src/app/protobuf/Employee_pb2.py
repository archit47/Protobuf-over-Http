# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/Employee.proto

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
  name='protobuf/Employee.proto',
  package='',
  serialized_pb=_b('\n\x17protobuf/Employee.proto\"e\n\x08\x45mployee\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x65mail\x18\x03 \x02(\t\x12\x14\n\x0cphone_number\x18\x04 \x01(\t\x12\x1a\n\x0cisBOEmployee\x18\x05 \x01(\x08:\x04true')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EMPLOYEE = _descriptor.Descriptor(
  name='Employee',
  full_name='Employee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Employee.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Employee.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Employee.email', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='Employee.phone_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isBOEmployee', full_name='Employee.isBOEmployee', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['Employee'] = _EMPLOYEE

Employee = _reflection.GeneratedProtocolMessageType('Employee', (_message.Message,), dict(
  DESCRIPTOR = _EMPLOYEE,
  __module__ = 'protobuf.Employee_pb2'
  # @@protoc_insertion_point(class_scope:Employee)
  ))
_sym_db.RegisterMessage(Employee)


# @@protoc_insertion_point(module_scope)
