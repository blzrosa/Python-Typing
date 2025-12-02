from typing import Any, overload, TypeVar, Callable

T = TypeVar("T")

# One single function — reused everywhere
def _identity(x: Any) -> Any:
    return x

# Static cast — zero-cost, perfect typing
class _StaticCast:
    @overload
    def __getitem__(self, typ: type[T]) -> Callable[[Any], T]: ...
    @overload
    def __getitem__(self, typ: None) -> Callable[[Any], None]: ...

    def __getitem__(self, typ: object) -> Callable[[Any], Any]:
        return _identity  # ← single shared function!

# Runtime cast — unchanged
class _RunTimeCast:
    @overload
    def __getitem__(self, typ: type[T]) -> Callable[[Any], T]: ...
    @overload
    def __getitem__(self, typ: None) -> Callable[[Any], None]:
        return lambda _: None

    def __getitem__(self, typ: Any) -> Callable[[Any], Any]:
        if typ is None:
            return lambda _: None
        return typ.__call__  # fastest way to call constructor

# Export singletons
Cast = _StaticCast()
RCast = _RunTimeCast()

__all__ = ["Cast", "RCast",]
