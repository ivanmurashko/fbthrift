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
class Empty(thrift.py3.types.Struct): ...
class Nada(thrift.py3.types.Union): ...


class Empty(thrift.py3.types.Struct):
    def __init__(
        self, *
    ) -> None: ...

    def __call__(
        self, *
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[Empty], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Empty) -> bool: ...
    def __lt__(self, other: Empty) -> bool: ...



class NadaType(Enum):
    EMPTY: ...
    value: int


class Nada(thrift.py3.types.Union):
    def __init__(
        self, *
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Nada) -> bool: ...
    def __lt__(self, other: Nada) -> bool: ...

    @property
    def value(self) -> _typing.Union[]: ...
    @property
    def type(self) -> NadaType: ...
    def get_type(self) -> NadaType: ...


