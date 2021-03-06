#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
cimport cython as __cython
from cython.operator cimport dereference as deref
from libcpp.memory cimport make_unique, unique_ptr, shared_ptr

cimport thrift.py3.types
from thrift.py3.types cimport (
    reset_field as __reset_field,
    StructFieldsSetter as __StructFieldsSetter
)

from thrift.py3.types cimport const_pointer_cast


@__cython.auto_pickle(False)
cdef class __MyStruct_FieldsSetter(__StructFieldsSetter):

    @staticmethod
    cdef __MyStruct_FieldsSetter create(_module_types.cMyStruct* struct_cpp_obj):
        cdef __MyStruct_FieldsSetter __fbthrift_inst = __MyStruct_FieldsSetter.__new__(__MyStruct_FieldsSetter)
        __fbthrift_inst._struct_cpp_obj = struct_cpp_obj
        __fbthrift_inst._setters[__cstring_view(<const char*>"MyIntField")] = __MyStruct_FieldsSetter._set_field_0
        __fbthrift_inst._setters[__cstring_view(<const char*>"MyStringField")] = __MyStruct_FieldsSetter._set_field_1
        return __fbthrift_inst

    cdef void set_field(__MyStruct_FieldsSetter self, const char* name, object value) except *:
        cdef __cstring_view cname = __cstring_view(name)
        cdef cumap[__cstring_view, __MyStruct_FieldsSetterFunc].iterator found = self._setters.find(cname)
        if found == self._setters.end():
            raise TypeError(f"invalid field name {name.decode('utf-8')}")
        deref(found).second(self, value)

    cdef void _set_field_0(self, __fbthrift_value) except *:
        # for field MyIntField
        if __fbthrift_value is None:
            __reset_field[_module_types.cMyStruct](deref(self._struct_cpp_obj), 0)
            return
        if not isinstance(__fbthrift_value, int):
            raise TypeError(f'MyIntField is not a { int !r}.')
        __fbthrift_value = <cint64_t> __fbthrift_value
        deref(self._struct_cpp_obj).MyIntField_ref().assign(__fbthrift_value)
        deref(self._struct_cpp_obj).__isset.MyIntField = True

    cdef void _set_field_1(self, __fbthrift_value) except *:
        # for field MyStringField
        if __fbthrift_value is None:
            __reset_field[_module_types.cMyStruct](deref(self._struct_cpp_obj), 1)
            return
        if not isinstance(__fbthrift_value, str):
            raise TypeError(f'MyStringField is not a { str !r}.')
        deref(self._struct_cpp_obj).MyStringField_ref().assign(cmove(bytes_to_string(__fbthrift_value.encode('utf-8'))))
        deref(self._struct_cpp_obj).__isset.MyStringField = True

