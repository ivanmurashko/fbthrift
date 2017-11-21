#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.string cimport string
from libcpp cimport bool as cbool
from cpython cimport bool as pbool
from libc.stdint cimport int8_t, int16_t, int32_t, int64_t
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap, pair as cpair
from thrift.py3.exceptions cimport cTException
cimport thrift.py3.exceptions
cimport thrift.py3.types
cimport module0.types
cimport module1.types




cdef extern from "src/gen-cpp2/module2_types_custom_protocol.h" namespace "module2":
    # Forward Declaration
    cdef cppclass cStruct "module2::Struct"
    # Forward Declaration
    cdef cppclass cBigStruct "module2::BigStruct"

cdef extern from "src/gen-cpp2/module2_types.h" namespace "module2":
    cdef cppclass cStruct__isset "module2::Struct::__isset":
        bint first
        bint second

    cdef cppclass cStruct "module2::Struct":
        cStruct() except +
        cStruct(const cStruct&) except +
        bint operator==(cStruct&)
        module0.types.cStruct first
        module1.types.cStruct second
        cStruct__isset __isset

    cdef cppclass cBigStruct__isset "module2::BigStruct::__isset":
        bint s
        bint id

    cdef cppclass cBigStruct "module2::BigStruct":
        cBigStruct() except +
        cBigStruct(const cBigStruct&) except +
        bint operator==(cBigStruct&)
        cStruct s
        int32_t id
        cBigStruct__isset __isset


cdef extern from "<utility>" namespace "std" nogil:
    cdef shared_ptr[cStruct] move(unique_ptr[cStruct])
    cdef shared_ptr[cStruct] move_shared "std::move"(shared_ptr[cStruct])
    cdef unique_ptr[cStruct] move_unique "std::move"(unique_ptr[cStruct])
    cdef shared_ptr[cBigStruct] move(unique_ptr[cBigStruct])
    cdef shared_ptr[cBigStruct] move_shared "std::move"(shared_ptr[cBigStruct])
    cdef unique_ptr[cBigStruct] move_unique "std::move"(unique_ptr[cBigStruct])

cdef extern from "<memory>" namespace "std" nogil:
    cdef shared_ptr[const cStruct] const_pointer_cast "std::const_pointer_cast<const module2::Struct>"(shared_ptr[cStruct])
    cdef shared_ptr[const cBigStruct] const_pointer_cast "std::const_pointer_cast<const module2::BigStruct>"(shared_ptr[cBigStruct])

# Forward Definition of the cython struct
cdef class Struct(thrift.py3.types.Struct)

cdef class Struct(thrift.py3.types.Struct):
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cStruct] _cpp_obj
    cdef module0.types.Struct __first
    cdef module1.types.Struct __second

    @staticmethod
    cdef unique_ptr[cStruct] _make_instance(
        cStruct* base_instance,
        object first,
        object second
    ) except *

    @staticmethod
    cdef create(shared_ptr[cStruct])

# Forward Definition of the cython struct
cdef class BigStruct(thrift.py3.types.Struct)

cdef class BigStruct(thrift.py3.types.Struct):
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cBigStruct] _cpp_obj
    cdef Struct __s

    @staticmethod
    cdef unique_ptr[cBigStruct] _make_instance(
        cBigStruct* base_instance,
        object s,
        object id
    ) except *

    @staticmethod
    cdef create(shared_ptr[cBigStruct])




cdef extern from "src/gen-cpp2/module2_constants.h" namespace "module2":
    cdef cStruct cc2 "module2::module2_constants::c2"()
