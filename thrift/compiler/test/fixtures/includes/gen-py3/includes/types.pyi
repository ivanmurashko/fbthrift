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
import transitive.types


# Forward Definitions for Structs
class Included(thrift.py3.types.Struct): ...


class Included(thrift.py3.types.Struct):
    def __init__(
        self, *,
        MyIntField: int=None,
        MyTransitiveField: transitive.types.Foo=None
    ) -> None: ...

    def __call__(
        self, *,
        MyIntField: _typing.Union[int, NOTSET, None]=NOTSET,
        MyTransitiveField: _typing.Union[transitive.types.Foo, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[Included], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Included) -> bool: ...
    def __lt__(self, other: Included) -> bool: ...

    @property
    def MyIntField(self) -> int: ...
    @property
    def MyTransitiveField(self) -> transitive.types.Foo: ...


