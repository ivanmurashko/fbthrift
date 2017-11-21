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


# Forward Definitions for Structs
class Foo(thrift.py3.types.Struct): ...
# Forward Definitions for Containers
class List__bool(_typing.Sequence[bool]): ...
class List__i32(_typing.Sequence[int]): ...


class Foo(thrift.py3.types.Struct):
    def __init__(
        self, *,
        myInteger: int,
        myString: str=None,
        myBools: _typing.Sequence[bool]=None,
        myNumbers: _typing.Sequence[int]
    ) -> None: ...

    def __call__(
        self, *,
        myInteger: _typing.Union[int, NOTSET]=NOTSET,
        myString: _typing.Union[str, NOTSET, None]=NOTSET,
        myBools: _typing.Union[_typing.Sequence[bool], NOTSET, None]=NOTSET,
        myNumbers: _typing.Union[_typing.Sequence[int], NOTSET]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[Foo], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Foo) -> bool: ...
    def __lt__(self, other: Foo) -> bool: ...

    @property
    def myInteger(self) -> int: ...
    @property
    def myString(self) -> str: ...
    @property
    def myBools(self) -> List__bool: ...
    @property
    def myNumbers(self) -> List__i32: ...


_List__boolT = _typing.TypeVar('_List__boolT', bound=_typing.Sequence[bool])


class List__bool(_typing.Sequence[bool]):
    def __init__(self, items: _typing.Sequence[bool]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def index(self, item: bool) -> int: ...
    def count(self, item: bool) -> int: ...
    def __add__(self, other: _typing.Sequence[bool]) -> List__bool: ...
    def __radd__(self, other: _List__boolT) -> _List__boolT: ...
    @_typing.overload
    def __getitem__(self, index: slice) -> List__bool: ...
    def __getitem__(self, index: int) -> bool: ...
    def __reversed__(self) -> _typing.Iterator[bool]: ...
    def __iter__(self) -> _typing.Iterator[bool]: ...
    def __contains__(self, item: bool) -> bool: ...
    def __eq__(self, other: _typing.Sequence[bool]) -> bool: ...


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


