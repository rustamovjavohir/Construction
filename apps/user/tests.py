import time
from datetime import datetime, timedelta
from functools import reduce, lru_cache, cache, wraps


def cache_decorator(func):
    _cache = {}

    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        else:
            result = func(*args)
            _cache[args] = result
        return _cache[args]

    return wrapper


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache


@lru_cache
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = time.process_time_ns()
    print(fibonacci(500))
    end_time = time.process_time_ns()
    print(end_time - start)
