import time

class timer(object):

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print(f"--- {(time.time() - self.start)*1000:.3f} ms ---")