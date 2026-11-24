
# Q7 - Diagnose, Redesign and Validate
# Selected limitation: Repeated calculations in naive recursion

import time


original_calls = 0
redesign_steps = 0


# Original program: naive recursion
def original_ways(n):
    global original_calls
    original_calls += 1

    if n <= 1:
        return 1

    return original_ways(n - 1) + original_ways(n - 2)


# Redesigned program: iterative calculation
def redesigned_ways(n):
    global redesign_steps
    redesign_steps = 0

    if n <= 1:
        return 1

    previous = 1
    current = 1

    for _ in range(2, n + 1):
        redesign_steps += 1
        previous, current = current, previous + current

    return current


print("Q7 - Original vs Redesigned")
print("--------------------------------")

for n in [10, 20, 25, 30]:
    original_calls = 0

    start = time.perf_counter()
    original_result = original_ways(n)
    original_time = time.perf_counter() - start

    start = time.perf_counter()
    redesigned_result = redesigned_ways(n)
    redesigned_time = time.perf_counter() - start

    print("\nInput steps:", n)
    print("Original result:", original_result)
    print("Original function calls:", original_calls)
    print(f"Original time: {original_time:.6f} seconds")

    print("Redesigned result:", redesigned_result)
    print("Redesigned loop steps:", redesign_steps)
    print(f"Redesigned time: {redesigned_time:.6f} seconds")

    print("Results are equal:", original_result == redesigned_result)


print("\nDesign conclusion:")
print("Redesigned iterative solution avoids repeated recursive calls.")
print("It uses O(n) time and O(1) extra space.")
