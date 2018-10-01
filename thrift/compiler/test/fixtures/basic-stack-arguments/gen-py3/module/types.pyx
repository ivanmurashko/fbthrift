#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
cimport cython as __cython
from cpython.bytes cimport PyBytes_AsStringAndSize
from cpython.object cimport PyTypeObject, Py_LT, Py_LE, Py_EQ, Py_NE, Py_GT, Py_GE
from libcpp.memory cimport shared_ptr, make_shared, unique_ptr, make_unique
from libcpp.string cimport string
from libcpp cimport bool as cbool
from libcpp.iterator cimport inserter as cinserter
from cpython cimport bool as pbool
from libc.stdint cimport int8_t, int16_t, int32_t, int64_t, uint32_t
from cython.operator cimport dereference as deref, preincrement as inc, address as ptr_address
import thrift.py3.types
cimport thrift.py3.types
cimport thrift.py3.exceptions
from thrift.py3.types import NOTSET as __NOTSET
from thrift.py3.types cimport (
    translate_cpp_enum_to_python,
    SetMetaClass as __SetMetaClass,
    constant_shared_ptr,
)
cimport thrift.py3.std_libcpp as std_libcpp
from thrift.py3.serializer import Protocol as __Protocol
cimport thrift.py3.serializer as serializer
from thrift.py3.serializer import deserialize, serialize
import folly.iobuf as __iobuf
from folly.optional cimport cOptional

import sys
import itertools
from collections import Sequence, Set, Mapping, Iterable
import warnings
import builtins as _builtins

cdef object __MyEnumEnumInstances = None  # Set[MyEnum]
cdef object __MyEnumEnumMembers = {}      # Dict[str, MyEnum]
cdef object __MyEnumEnumUniqueValues = dict()    # Dict[int, MyEnum]

@__cython.internal
@__cython.auto_pickle(False)
cdef class __MyEnumMeta(type):
    def __call__(cls, value):
        cdef int cvalue
        if isinstance(value, cls) and value in __MyEnumEnumInstances:
            return value
        if isinstance(value, int):
            cvalue = value
            if cvalue == 0:
                return MyEnum.MyValue1
            elif cvalue == 1:
                return MyEnum.MyValue2

        raise ValueError(f'{value} is not a valid MyEnum')

    def __getitem__(cls, name):
        return __MyEnumEnumMembers[name]

    def __dir__(cls):
        return ['__class__', '__doc__', '__members__', '__module__',
        'MyValue1',
        'MyValue2',
        ]

    def __iter__(cls):
        return iter(__MyEnumEnumUniqueValues.values())

    def __reversed__(cls):
        return reversed(iter(cls))

    def __contains__(cls, item):
        if not isinstance(item, cls):
            return False
        return item in __MyEnumEnumInstances

    def __len__(cls):
        return len(__MyEnumEnumInstances)


cdef __MyEnum_unique_instance(int value, str name):
    inst = __MyEnumEnumUniqueValues.get(value)
    if inst is None:
        inst = __MyEnumEnumUniqueValues[value] = MyEnum.__new__(MyEnum, value, name)
    __MyEnumEnumMembers[name] = inst
    return inst


@__cython.final
cdef class MyEnum(thrift.py3.types.CompiledEnum):
    MyValue1 = __MyEnum_unique_instance(0, "MyValue1")
    MyValue2 = __MyEnum_unique_instance(1, "MyValue2")
    __members__ = thrift.py3.types.MappingProxyType(__MyEnumEnumMembers)

    def __cinit__(self, value, name):
        if __MyEnumEnumInstances is not None:
            raise TypeError('For Safty we have disabled __new__')
        self.value = value
        self.name = name
        self.__hash = hash(name)
        self.__str = f"MyEnum.{name}"
        self.__repr = f"<{self.__str}: {value}>"

    def __repr__(self):
        return self.__repr

    def __str__(self):
        return self.__str

    def __int__(self):
        return self.value

    def __eq__(self, other):
        if not isinstance(other, MyEnum):
            warnings.warn(f"comparison not supported between instances of { MyEnum } and {type(other)}", RuntimeWarning, stacklevel=2)
            return False
        return self is other

    def __hash__(self):
        return self.__hash

    def __reduce__(self):
        return MyEnum, (self.value,)


__SetMetaClass(<PyTypeObject*> MyEnum, <PyTypeObject*> __MyEnumMeta)
__MyEnumEnumInstances = set(__MyEnumEnumUniqueValues.values())


cdef inline cMyEnum MyEnum_to_cpp(MyEnum value):
    cdef int cvalue = value.value
    if cvalue == 0:
        return MyEnum__MyValue1
    elif cvalue == 1:
        return MyEnum__MyValue2

cdef cMyStruct _MyStruct_defaults = cMyStruct()

cdef class MyStruct(thrift.py3.types.Struct):

    def __init__(
        MyStruct self, *,
        MyIntField=None,
        str MyStringField=None
    ):
        if MyIntField is not None:
            if not isinstance(MyIntField, int):
                raise TypeError(f'MyIntField is not a { int !r}.')
            MyIntField = <int64_t> MyIntField

        self._cpp_obj = move(MyStruct._make_instance(
          NULL,
          NULL,
          MyIntField,
          MyStringField,
        ))

    def __call__(
        MyStruct self,
        MyIntField=__NOTSET,
        MyStringField=__NOTSET
    ):
        ___NOTSET = __NOTSET  # Cheaper for larger structs
        cdef bint[2] __isNOTSET  # so make_instance is typed

        changes = False
        if MyIntField is ___NOTSET:
            __isNOTSET[0] = True
            MyIntField = None
        else:
            changes = True
        if MyStringField is ___NOTSET:
            __isNOTSET[1] = True
            MyStringField = None
        else:
            changes = True

        if not changes:
            return self

        if MyIntField is not None:
            if not isinstance(MyIntField, int):
                raise TypeError(f'MyIntField is not a { int !r}.')
            MyIntField = <int64_t> MyIntField

        if MyStringField is not None:
            if not isinstance(MyStringField, str):
                raise TypeError(f'MyStringField is not a { str !r}.')

        inst = <MyStruct>MyStruct.__new__(MyStruct)
        inst._cpp_obj = move(MyStruct._make_instance(
          self._cpp_obj.get(),
          __isNOTSET,
          MyIntField,
          MyStringField,
        ))
        return inst

    @staticmethod
    cdef unique_ptr[cMyStruct] _make_instance(
        cMyStruct* base_instance,
        bint* __isNOTSET,
        object MyIntField ,
        str MyStringField 
    ) except *:
        cdef unique_ptr[cMyStruct] c_inst
        if base_instance:
            c_inst = make_unique[cMyStruct](deref(base_instance))
        else:
            c_inst = make_unique[cMyStruct]()

        if base_instance:
            # Convert None's to default value. (or unset)
            if not __isNOTSET[0] and MyIntField is None:
                deref(c_inst).MyIntField = _MyStruct_defaults.MyIntField
                deref(c_inst).__isset.MyIntField = False
                pass

            if not __isNOTSET[1] and MyStringField is None:
                deref(c_inst).MyStringField = _MyStruct_defaults.MyStringField
                deref(c_inst).__isset.MyStringField = False
                pass

        if MyIntField is not None:
            deref(c_inst).MyIntField = MyIntField
            deref(c_inst).__isset.MyIntField = True
        if MyStringField is not None:
            deref(c_inst).MyStringField = thrift.py3.types.move(thrift.py3.types.bytes_to_string(MyStringField.encode('utf-8')))
            deref(c_inst).__isset.MyStringField = True
        # in C++ you don't have to call move(), but this doesn't translate
        # into a C++ return statement, so you do here
        return move_unique(c_inst)

    def __iter__(self):
        yield 'MyIntField', self.MyIntField
        yield 'MyStringField', self.MyStringField

    def __bool__(self):
        return True or True

    @staticmethod
    cdef create(shared_ptr[cMyStruct] cpp_obj):
        inst = <MyStruct>MyStruct.__new__(MyStruct)
        inst._cpp_obj = move_shared(cpp_obj)
        return inst

    @property
    def MyIntField(self):

        return deref(self._cpp_obj).MyIntField

    @property
    def MyStringField(self):

        return (<bytes>deref(self._cpp_obj).MyStringField).decode('UTF-8')


    def __hash__(MyStruct self):
        if not self.__hash:
            self.__hash = hash((
            self.MyIntField,
            self.MyStringField,
            ))
        return self.__hash

    def __repr__(MyStruct self):
        return f'MyStruct(MyIntField={repr(self.MyIntField)}, MyStringField={repr(self.MyStringField)})'
    def __copy__(MyStruct self):
        cdef shared_ptr[cMyStruct] cpp_obj = make_shared[cMyStruct](
            deref(self._cpp_obj)
        )
        return MyStruct.create(move_shared(cpp_obj))

    def __richcmp__(self, other, op):
        cdef int cop = op
        if not (
                isinstance(self, MyStruct) and
                isinstance(other, MyStruct)):
            if cop == Py_EQ:  # different types are never equal
                return False
            elif cop == Py_NE:  # different types are always notequal
                return True
            else:
                return NotImplemented

        cdef cMyStruct cself = deref((<MyStruct>self)._cpp_obj)
        cdef cMyStruct cother = deref((<MyStruct>other)._cpp_obj)
        if cop == Py_EQ:
            return cself == cother
        elif cop == Py_NE:
            return not (cself == cother)
        elif cop == Py_LT:
            return cself < cother
        elif cop == Py_LE:
            return cself <= cother
        elif cop == Py_GT:
            return cself > cother
        elif cop == Py_GE:
            return cself >= cother
        else:
            return NotImplemented

    cdef __iobuf.IOBuf _serialize(MyStruct self, proto):
        cdef __iobuf.cIOBufQueue queue = __iobuf.cIOBufQueue(__iobuf.cacheChainLength())
        cdef cMyStruct* cpp_obj = self._cpp_obj.get()
        if proto is __Protocol.COMPACT:
            with nogil:
                serializer.CompactSerialize[cMyStruct](deref(cpp_obj), &queue, serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.BINARY:
            with nogil:
                serializer.BinarySerialize[cMyStruct](deref(cpp_obj), &queue, serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.JSON:
            with nogil:
                serializer.JSONSerialize[cMyStruct](deref(cpp_obj), &queue, serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.COMPACT_JSON:
            with nogil:
                serializer.CompactJSONSerialize[cMyStruct](deref(cpp_obj), &queue, serializer.SHARE_EXTERNAL_BUFFER)
        return __iobuf.from_unique_ptr(queue.move())

    cdef uint32_t _deserialize(MyStruct self, const __iobuf.cIOBuf* buf, proto) except? 0:
        cdef uint32_t needed
        self._cpp_obj = make_shared[cMyStruct]()
        cdef cMyStruct* cpp_obj = self._cpp_obj.get()
        if proto is __Protocol.COMPACT:
            with nogil:
                needed = serializer.CompactDeserialize[cMyStruct](buf, deref(cpp_obj), serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.BINARY:
            with nogil:
                needed = serializer.BinaryDeserialize[cMyStruct](buf, deref(cpp_obj), serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.JSON:
            with nogil:
                needed = serializer.JSONDeserialize[cMyStruct](buf, deref(cpp_obj), serializer.SHARE_EXTERNAL_BUFFER)
        elif proto is __Protocol.COMPACT_JSON:
            with nogil:
                needed = serializer.CompactJSONDeserialize[cMyStruct](buf, deref(cpp_obj), serializer.SHARE_EXTERNAL_BUFFER)
        return needed

    def __reduce__(self):
        return (deserialize, (MyStruct, serialize(self)))


