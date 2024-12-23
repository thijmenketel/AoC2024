from functools import wraps
import time

def timed(func):
    @wraps(func)
    def inner(*arg, **kw):
        start = time.time()
        res = func(*arg, **kw)
        print(f"--- {(time.time() - start)*1000:.3f} ms ---")
        return res
    return inner