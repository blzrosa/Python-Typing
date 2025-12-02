import time
from casty import RCast, Cast
from typing import Any, Callable, cast

rcast = RCast
ccast = Cast
intcast = Cast[int]

x: int  = RCast[int](3.14)           # → 3, int
s: str  = RCast[str](42)             # → "42"
n: None = RCast[None](print("hi"))   # → None, side effects ignored

print(x, type(x))  # 3 <class 'int'>
print(s)           # 42
print(n)           # None

x: int  = Cast[int](3.14)           # → 3.14, float
s: str  = Cast[str](42)             # → 42
n: None = Cast[None](print("hi"))   # → 'None'

print(x, type(x))  # 3 <class 'int'>
print(s)           # 42
print(n)           # None

def time_func(func: Callable[..., Any]) -> Callable[..., Any]:
    init = time.process_time_ns()
    end = time.process_time_ns()
    print((end - init) / 1e9)
    return func

def time_func_10K(func: Callable[..., Any]) -> Callable[..., Any]:
    init = time.process_time_ns()
    for _ in range(10_000):
        func()
    end = time.process_time_ns()
    print(f'{func.__name__}:', f'{(end - init) / 1e3}us')
    return func

@time_func_10K
def custom_cast() -> None:
    x: int  = Cast[int](3.14)

@time_func_10K
def custom_cast_file() -> None:
    x: int  = ccast[int](3.14)

@time_func_10K
def intcast_cast() -> None:
    x: int  = intcast(3.14)

@time_func_10K
def std_cast() -> None:
    x: int  = cast(int, 3.14)

@time_func_10K
def no_cast() -> None:
    x: int = 3.14 #type: ignore