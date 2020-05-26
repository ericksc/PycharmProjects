
import time


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
start = time.time()

print([fib(n) for n in range(35)])
print(f'Duration: {time.time() - start}s')
# 21.25 s