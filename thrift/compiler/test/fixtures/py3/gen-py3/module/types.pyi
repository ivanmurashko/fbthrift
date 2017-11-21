#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import NOTSET
from thrift.py3.serializer import Protocol
import typing as _typing

import sys
import itertools
from enum import Enum


class AnEnum(Enum):
    ONE: ...
    TWO: ...
    THREE: ...
    FOUR: ...
    value: int


# Forward Definitions for Structs
class SimpleException(thrift.py3.exceptions.Error): ...
class SimpleStruct(thrift.py3.types.Struct): ...
class ComplexStruct(thrift.py3.types.Struct): ...
# Forward Definitions for Containers
class List__i16(_typing.Sequence[int]): ...
class List__i32(_typing.Sequence[int]): ...
class List__i64(_typing.Sequence[int]): ...
class List__string(_typing.Sequence[str]): ...
class List__SimpleStruct(_typing.Sequence[SimpleStruct]): ...
class Set__i32(_typing.AbstractSet[int]): ...
class Set__string(_typing.AbstractSet[str]): ...
class Map__string_string(_typing.Mapping[str, str]): ...
class Map__string_SimpleStruct(_typing.Mapping[str, SimpleStruct]): ...
class Map__string_i16(_typing.Mapping[str, int]): ...
class List__List__i32(_typing.Sequence[_typing.Sequence[int]]): ...
class Map__string_i32(_typing.Mapping[str, int]): ...
class Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, int]]): ...
class List__Set__string(_typing.Sequence[_typing.AbstractSet[str]]): ...
class Map__string_List__SimpleStruct(_typing.Mapping[str, _typing.Sequence[SimpleStruct]]): ...
class List__List__string(_typing.Sequence[_typing.Sequence[str]]): ...
class List__Set__i32(_typing.Sequence[_typing.AbstractSet[int]]): ...
class List__Map__string_string(_typing.Sequence[_typing.Mapping[str, str]]): ...
class List__binary(_typing.Sequence[bytes]): ...
class Set__binary(_typing.AbstractSet[bytes]): ...
class List__AnEnum(_typing.Sequence[AnEnum]): ...
class Map__i32_double(_typing.Mapping[int, float]): ...
class List__Map__i32_double(_typing.Sequence[_typing.Mapping[int, float]]): ...


class SimpleException(thrift.py3.exceptions.Error):
    def __init__(
        self, *,
        err_code: int=None
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: SimpleException) -> bool: ...
    def __lt__(self, other: SimpleException) -> bool: ...

    @property
    def err_code(self) -> int: ...


class SimpleStruct(thrift.py3.types.Struct):
    def __init__(
        self, *,
        is_on: bool=None,
        tiny_int: int=None,
        small_int: int=None,
        nice_sized_int: int=None,
        big_int: int=None,
        real: float=None,
        smaller_real: float=None
    ) -> None: ...

    def __call__(
        self, *,
        is_on: _typing.Union[bool, NOTSET, None]=NOTSET,
        tiny_int: _typing.Union[int, NOTSET, None]=NOTSET,
        small_int: _typing.Union[int, NOTSET, None]=NOTSET,
        nice_sized_int: _typing.Union[int, NOTSET, None]=NOTSET,
        big_int: _typing.Union[int, NOTSET, None]=NOTSET,
        real: _typing.Union[float, NOTSET, None]=NOTSET,
        smaller_real: _typing.Union[float, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[SimpleStruct], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: SimpleStruct) -> bool: ...
    def __lt__(self, other: SimpleStruct) -> bool: ...

    @property
    def is_on(self) -> bool: ...
    @property
    def tiny_int(self) -> int: ...
    @property
    def small_int(self) -> int: ...
    @property
    def nice_sized_int(self) -> int: ...
    @property
    def big_int(self) -> int: ...
    @property
    def real(self) -> float: ...
    @property
    def smaller_real(self) -> float: ...


class ComplexStruct(thrift.py3.types.Struct):
    def __init__(
        self, *,
        structOne: SimpleStruct=None,
        structTwo: SimpleStruct=None,
        an_integer: int=None,
        name: str=None,
        an_enum: AnEnum=None,
        some_bytes: bytes=None
    ) -> None: ...

    def __call__(
        self, *,
        structOne: _typing.Union[SimpleStruct, NOTSET, None]=NOTSET,
        structTwo: _typing.Union[SimpleStruct, NOTSET, None]=NOTSET,
        an_integer: _typing.Union[int, NOTSET, None]=NOTSET,
        name: _typing.Union[str, NOTSET, None]=NOTSET,
        an_enum: _typing.Union[AnEnum, NOTSET, None]=NOTSET,
        some_bytes: _typing.Union[bytes, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[ComplexStruct], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: ComplexStruct) -> bool: ...
    def __lt__(self, other: ComplexStruct) -> bool: ...

    @property
    def structOne(self) -> SimpleStruct: ...
    @property
    def structTwo(self) -> SimpleStruct: ...
    @property
    def an_integer(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def an_enum(self) -> AnEnum: ...
    @property
    def some_bytes(self) -> bytes: ...


_List__i16T = _typing.TypeVar('_List__i16T', bound=_typing.Sequence[int])


class List__i16(_typing.Sequence[int]):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: int) -> int: ...
    def count(self, item: int) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> List__i16: ...
    def __radd__(self, other: _List__i16T) -> _List__i16T: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__i16: ...
    def __getitem__(self, index: int) -> int: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...
    def __contains__(self, item: int) -> bool: ...
    def __eq__(self, other: _typing.Sequence[int]) -> bool: ...


_List__i32T = _typing.TypeVar('_List__i32T', bound=_typing.Sequence[int])


class List__i32(_typing.Sequence[int]):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: int) -> int: ...
    def count(self, item: int) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> List__i32: ...
    def __radd__(self, other: _List__i32T) -> _List__i32T: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__i32: ...
    def __getitem__(self, index: int) -> int: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...
    def __contains__(self, item: int) -> bool: ...
    def __eq__(self, other: _typing.Sequence[int]) -> bool: ...


_List__i64T = _typing.TypeVar('_List__i64T', bound=_typing.Sequence[int])


class List__i64(_typing.Sequence[int]):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: int) -> int: ...
    def count(self, item: int) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> List__i64: ...
    def __radd__(self, other: _List__i64T) -> _List__i64T: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__i64: ...
    def __getitem__(self, index: int) -> int: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...
    def __contains__(self, item: int) -> bool: ...
    def __eq__(self, other: _typing.Sequence[int]) -> bool: ...


_List__stringT = _typing.TypeVar('_List__stringT', bound=_typing.Sequence[str])


class List__string(_typing.Sequence[str]):
    def __init__(self, items: _typing.Sequence[str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: str) -> int: ...
    def count(self, item: str) -> int: ...
    def __add__(self, other: _typing.Sequence[str]) -> List__string: ...
    def __radd__(self, other: _List__stringT) -> _List__stringT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__string: ...
    def __getitem__(self, index: int) -> str: ...
    def __reversed__(self) -> _typing.Iterator[str]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, item: str) -> bool: ...
    def __eq__(self, other: _typing.Sequence[str]) -> bool: ...


_List__SimpleStructT = _typing.TypeVar('_List__SimpleStructT', bound=_typing.Sequence[SimpleStruct])


class List__SimpleStruct(_typing.Sequence[SimpleStruct]):
    def __init__(self, items: _typing.Sequence[SimpleStruct]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: SimpleStruct) -> int: ...
    def count(self, item: SimpleStruct) -> int: ...
    def __add__(self, other: _typing.Sequence[SimpleStruct]) -> List__SimpleStruct: ...
    def __radd__(self, other: _List__SimpleStructT) -> _List__SimpleStructT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__SimpleStruct: ...
    def __getitem__(self, index: int) -> SimpleStruct: ...
    def __reversed__(self) -> _typing.Iterator[SimpleStruct]: ...
    def __iter__(self) -> _typing.Iterator[SimpleStruct]: ...
    def __contains__(self, item: SimpleStruct) -> bool: ...
    def __eq__(self, other: _typing.Sequence[SimpleStruct]) -> bool: ...


class Set__i32(_typing.AbstractSet[int]):
    def __init__(self, items: _typing.AbstractSet[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: _typing.AbstractSet[int]) -> bool: ...
    def __eq__(self, other: _typing.AbstractSet[int]) -> bool: ...
    def __contains__(self, item: int) -> bool: ...
    def __iter__(self) -> int): ...
    def __add__(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def __or__(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def __xor__(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def isdisjoint(self, other: _typing.AbstractSet[int]) -> bool: ...
    def union(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def intersection(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def difference(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def symmetric_difference(self, other: _typing.AbstractSet[int]) -> Set__i32: ...
    def issubset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[int]) -> bool: ...


class Set__string(_typing.AbstractSet[str]):
    def __init__(self, items: _typing.AbstractSet[str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: _typing.AbstractSet[str]) -> bool: ...
    def __eq__(self, other: _typing.AbstractSet[str]) -> bool: ...
    def __contains__(self, item: str) -> bool: ...
    def __iter__(self) -> str): ...
    def __add__(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def __or__(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def __xor__(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def isdisjoint(self, other: _typing.AbstractSet[str]) -> bool: ...
    def union(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def intersection(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def difference(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def symmetric_difference(self, other: _typing.AbstractSet[str]) -> Set__string: ...
    def issubset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[str]) -> bool: ...


class Map__string_string(_typing.Mapping[str, str]):
    def __init__(self, items: _typing.Mapping[str, str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, str]) -> bool: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: str=None) -> str: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[str]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, str]]: ...


class Map__string_SimpleStruct(_typing.Mapping[str, SimpleStruct]):
    def __init__(self, items: _typing.Mapping[str, SimpleStruct]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, SimpleStruct]) -> bool: ...
    def __getitem__(self, key: str) -> SimpleStruct: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: SimpleStruct=None) -> SimpleStruct: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[SimpleStruct]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, SimpleStruct]]: ...


class Map__string_i16(_typing.Mapping[str, int]):
    def __init__(self, items: _typing.Mapping[str, int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, int]) -> bool: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: int=None) -> int: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[int]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, int]]: ...


_List__List__i32T = _typing.TypeVar('_List__List__i32T', bound=_typing.Sequence[_typing.Sequence[int]])


class List__List__i32(_typing.Sequence[_typing.Sequence[int]]):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.Sequence[int]) -> int: ...
    def count(self, item: _typing.Sequence[int]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[int]]) -> List__List__i32: ...
    def __radd__(self, other: _List__List__i32T) -> _List__List__i32T: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__List__i32: ...
    def __getitem__(self, index: int) -> _typing.Sequence[int]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...
    def __contains__(self, item: _typing.Sequence[int]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.Sequence[int]]) -> bool: ...


class Map__string_i32(_typing.Mapping[str, int]):
    def __init__(self, items: _typing.Mapping[str, int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, int]) -> bool: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: int=None) -> int: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[int]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, int]]: ...


class Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, int]]):
    def __init__(self, items: _typing.Mapping[str, _typing.Mapping[str, int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, _typing.Mapping[str, int]]) -> bool: ...
    def __getitem__(self, key: str) -> _typing.Mapping[str, int]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: _typing.Mapping[str, int]=None) -> _typing.Mapping[str, int]: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[_typing.Mapping[str, int]]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Mapping[str, int]]]: ...


_List__Set__stringT = _typing.TypeVar('_List__Set__stringT', bound=_typing.Sequence[_typing.AbstractSet[str]])


class List__Set__string(_typing.Sequence[_typing.AbstractSet[str]]):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.AbstractSet[str]) -> int: ...
    def count(self, item: _typing.AbstractSet[str]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[str]]) -> List__Set__string: ...
    def __radd__(self, other: _List__Set__stringT) -> _List__Set__stringT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__Set__string: ...
    def __getitem__(self, index: int) -> _typing.AbstractSet[str]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...
    def __contains__(self, item: _typing.AbstractSet[str]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.AbstractSet[str]]) -> bool: ...


class Map__string_List__SimpleStruct(_typing.Mapping[str, _typing.Sequence[SimpleStruct]]):
    def __init__(self, items: _typing.Mapping[str, _typing.Sequence[SimpleStruct]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[str, _typing.Sequence[SimpleStruct]]) -> bool: ...
    def __getitem__(self, key: str) -> _typing.Sequence[SimpleStruct]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, default: _typing.Sequence[SimpleStruct]=None) -> _typing.Sequence[SimpleStruct]: ...
    def keys(self) -> _typing.Iterator[str]: ...
    def values(self) -> _typing.Iterator[_typing.Sequence[SimpleStruct]]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Sequence[SimpleStruct]]]: ...


_List__List__stringT = _typing.TypeVar('_List__List__stringT', bound=_typing.Sequence[_typing.Sequence[str]])


class List__List__string(_typing.Sequence[_typing.Sequence[str]]):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.Sequence[str]) -> int: ...
    def count(self, item: _typing.Sequence[str]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[str]]) -> List__List__string: ...
    def __radd__(self, other: _List__List__stringT) -> _List__List__stringT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__List__string: ...
    def __getitem__(self, index: int) -> _typing.Sequence[str]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[str]]: ...
    def __contains__(self, item: _typing.Sequence[str]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.Sequence[str]]) -> bool: ...


_List__Set__i32T = _typing.TypeVar('_List__Set__i32T', bound=_typing.Sequence[_typing.AbstractSet[int]])


class List__Set__i32(_typing.Sequence[_typing.AbstractSet[int]]):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.AbstractSet[int]) -> int: ...
    def count(self, item: _typing.AbstractSet[int]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[int]]) -> List__Set__i32: ...
    def __radd__(self, other: _List__Set__i32T) -> _List__Set__i32T: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__Set__i32: ...
    def __getitem__(self, index: int) -> _typing.AbstractSet[int]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...
    def __contains__(self, item: _typing.AbstractSet[int]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.AbstractSet[int]]) -> bool: ...


_List__Map__string_stringT = _typing.TypeVar('_List__Map__string_stringT', bound=_typing.Sequence[_typing.Mapping[str, str]])


class List__Map__string_string(_typing.Sequence[_typing.Mapping[str, str]]):
    def __init__(self, items: _typing.Sequence[_typing.Mapping[str, str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.Mapping[str, str]) -> int: ...
    def count(self, item: _typing.Mapping[str, str]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Mapping[str, str]]) -> List__Map__string_string: ...
    def __radd__(self, other: _List__Map__string_stringT) -> _List__Map__string_stringT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__Map__string_string: ...
    def __getitem__(self, index: int) -> _typing.Mapping[str, str]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Mapping[str, str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Mapping[str, str]]: ...
    def __contains__(self, item: _typing.Mapping[str, str]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.Mapping[str, str]]) -> bool: ...


_List__binaryT = _typing.TypeVar('_List__binaryT', bound=_typing.Sequence[bytes])


class List__binary(_typing.Sequence[bytes]):
    def __init__(self, items: _typing.Sequence[bytes]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: bytes) -> int: ...
    def count(self, item: bytes) -> int: ...
    def __add__(self, other: _typing.Sequence[bytes]) -> List__binary: ...
    def __radd__(self, other: _List__binaryT) -> _List__binaryT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__binary: ...
    def __getitem__(self, index: int) -> bytes: ...
    def __reversed__(self) -> _typing.Iterator[bytes]: ...
    def __iter__(self) -> _typing.Iterator[bytes]: ...
    def __contains__(self, item: bytes) -> bool: ...
    def __eq__(self, other: _typing.Sequence[bytes]) -> bool: ...


class Set__binary(_typing.AbstractSet[bytes]):
    def __init__(self, items: _typing.AbstractSet[bytes]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def __eq__(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def __contains__(self, item: bytes) -> bool: ...
    def __iter__(self) -> bytes): ...
    def __add__(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def __or__(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def __xor__(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def isdisjoint(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def union(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def intersection(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def difference(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def symmetric_difference(self, other: _typing.AbstractSet[bytes]) -> Set__binary: ...
    def issubset(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[bytes]) -> bool: ...


_List__AnEnumT = _typing.TypeVar('_List__AnEnumT', bound=_typing.Sequence[AnEnum])


class List__AnEnum(_typing.Sequence[AnEnum]):
    def __init__(self, items: _typing.Sequence[AnEnum]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: AnEnum) -> int: ...
    def count(self, item: AnEnum) -> int: ...
    def __add__(self, other: _typing.Sequence[AnEnum]) -> List__AnEnum: ...
    def __radd__(self, other: _List__AnEnumT) -> _List__AnEnumT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__AnEnum: ...
    def __getitem__(self, index: int) -> AnEnum: ...
    def __reversed__(self) -> _typing.Iterator[AnEnum]: ...
    def __iter__(self) -> _typing.Iterator[AnEnum]: ...
    def __contains__(self, item: AnEnum) -> bool: ...
    def __eq__(self, other: _typing.Sequence[AnEnum]) -> bool: ...


class Map__i32_double(_typing.Mapping[int, float]):
    def __init__(self, items: _typing.Mapping[int, float]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[int, float]) -> bool: ...
    def __getitem__(self, key: int) -> float: ...
    def __iter__(self) -> _typing.Iterator[int]: ...
    def __contains__(self, key: int) -> bool: ...
    def get(self, key: int, default: float=None) -> float: ...
    def keys(self) -> _typing.Iterator[int]: ...
    def values(self) -> _typing.Iterator[float]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[int, float]]: ...


_List__Map__i32_doubleT = _typing.TypeVar('_List__Map__i32_doubleT', bound=_typing.Sequence[_typing.Mapping[int, float]])


class List__Map__i32_double(_typing.Sequence[_typing.Mapping[int, float]]):
    def __init__(self, items: _typing.Sequence[_typing.Mapping[int, float]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: _typing.Mapping[int, float]) -> int: ...
    def count(self, item: _typing.Mapping[int, float]) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Mapping[int, float]]) -> List__Map__i32_double: ...
    def __radd__(self, other: _List__Map__i32_doubleT) -> _List__Map__i32_doubleT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__Map__i32_double: ...
    def __getitem__(self, index: int) -> _typing.Mapping[int, float]: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Mapping[int, float]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Mapping[int, float]]: ...
    def __contains__(self, item: _typing.Mapping[int, float]) -> bool: ...
    def __eq__(self, other: _typing.Sequence[_typing.Mapping[int, float]]) -> bool: ...


