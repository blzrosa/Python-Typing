import time
from cast import Cast
from typing import Any, Callable, cast

def time_func_10K(func: Callable[..., Any]) -> Callable[..., Any]:
    init = time.process_time_ns()
    for _ in range(10_000):
        func()
    end = time.process_time_ns()
    print(f'{func.__name__}:', f'{(end - init) / 1e3}us')
    return func

@time_func_10K
def custom_cast() -> None:
    x  = Cast[int](3.14)

@time_func_10K
def std_cast() -> None:
    x  = cast(int, 3.14)

@time_func_10K
def no_cast() -> None:
    x = 3.14