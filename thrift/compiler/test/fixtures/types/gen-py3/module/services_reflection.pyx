#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from thrift.py3.reflection cimport (
  MethodSpec as __MethodSpec,
  ArgumentSpec as __ArgumentSpec,
  NumberType as __NumberType,
)

import folly.iobuf as __iobuf

cimport include.types as _include_types

cimport module.types as _module_types


cdef __InterfaceSpec get_reflection__SomeService(bint for_clients):
    cdef __InterfaceSpec spec = __InterfaceSpec.create(
        name="SomeService",
        annotations={
        },
    )
    spec.add_method(
        __MethodSpec.create(
            name="bounce_map",
            arguments=(
                __ArgumentSpec.create(
                    name="m",
                    type=_module_types.std_unordered_map__Map__i32_string,
                    kind=__NumberType.NOT_A_NUMBER,
                    annotations={
                    },
                ),
            ),
            result=_module_types.std_unordered_map__Map__i32_string,
            result_kind=__NumberType.NOT_A_NUMBER,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    spec.add_method(
        __MethodSpec.create(
            name="binary_keyed_map",
            arguments=(
                __ArgumentSpec.create(
                    name="r",
                    type=_module_types.List__i64,
                    kind=__NumberType.NOT_A_NUMBER,
                    annotations={
                    },
                ),
            ),
            result=_module_types.Map__binary_i64,
            result_kind=__NumberType.NOT_A_NUMBER,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    return spec
