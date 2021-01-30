import time

from functools import wraps


def warn_slow(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if end - start > 2:
            print(f'execution of {func.__name__} with {args} arguments took more than 2 seconds.')
        return result

    return inner


@warn_slow
def func_slow(x, y):
    time.sleep(2)
    if x < y:
        for i in range(x, y):
            i = i // 2
            return i
    elif x > y:
        for i2 in range(x, y):
            i2 = i2 // 3
            return i2


@warn_slow
def func_fast(x, y):
    print(x, y)


func_slow(1, 2)
func_fast(1, 2)
