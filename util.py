import time

def timed(func):
    def inner():
        start = time.time()
        func()
        print(f"--- {(time.time() - start)*1000:.3f} ms ---")
    
    return inner