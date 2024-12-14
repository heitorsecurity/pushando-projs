import time

def measure():
    t0 = time.time()
    t1 = t0
    while t1 == t0:
        t1 = time.time()
        return t1-t0

samples = [measure() for i in range(30)]

for s in samples:
    print(f'time delta: {s:.4f} seconds')