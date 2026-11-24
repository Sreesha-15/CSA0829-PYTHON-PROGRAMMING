
# Q6 - Recursion and Its Limits

from functools import lru_cache
import sys
import time

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n):
    if n <= 1:
        return 1

    previous, current = 1, 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


# Correctness check from 1 to 6
print("Correctness check:")
for n in range(1, 7):
    print(n, "steps:", ways_iterative(n), "ways")


# Naive and memoised call count
print("\nCall count comparison:")

for n in [10, 20, 25, 30]:
    calls = 0
    naive_result = ways_naive(n)
    naive_calls = calls

    ways_memo.cache_clear()
    calls = 0
    memo_result = ways_memo(n)
    memo_calls = calls

    print(
        "n =", n,
        "| naive =", naive_result,
        "calls =", naive_calls,
        "| memo =", memo_result,
        "calls =", memo_calls
    )

# Recursion limit demonstration
print("\nRecursion limit:", sys.getrecursionlimit())

ways_memo.cache_clear()

try:
    print("Memoised ways for 1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError occurred at 1000 steps.")


# Iterative version for 1000
start = time.perf_counter()
answer = ways_iterative(1000)
elapsed = time.perf_counter() - start

print("\nIterative result for 1000 steps:")
print("Number of digits:", len(str(answer)))
print(f"Time: {elapsed:.6f} seconds")
