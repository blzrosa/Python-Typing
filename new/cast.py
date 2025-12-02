from functools import cache
from typing import Any, Callable, TypeVar

T = TypeVar("T")

def _identity(x: Any) -> Any:
    return x

class SCast:
    def __init__(self) -> None:
        pass
    
    @cache
    def __getitem__(self, typ: type[T]) -> Callable[[Any], T]:
        return _identity

Cast = SCast()

__all__ = ['Cast']

