
import random
import time
import sys


random.seed(42)

# Sensor readings
readings = [
    round(random.uniform(-10, 60), 2)
    for _ in range(10000)
]


# Method 1: For loop with append
def using_loop(data):
    valid = []

    for c in data:
        if -50 <= c <= 50:
            valid.append(c)

    return valid


# Method 2: List comprehension
def using_comprehension(data):
    return [c for c in data if -50 <= c <= 50]


# Method 3: Filter and map
def using_filter_map(data):
    valid = filter(lambda c: -50 <= c <= 50, data)

    fahrenheit = map(lambda c: (c * 9 / 5) + 32, valid)

    return list(fahrenheit)


# Convert valid Celsius values into Fahrenheit
valid_celsius = using_loop(readings)

fahrenheit_loop = [
    (c * 9 / 5) + 32
    for c in valid_celsius
]

fahrenheit_comprehension = [
    (c * 9 / 5) + 32
    for c in using_comprehension(readings)
]


# Dictionary comprehension
temperature_dictionary = {
    index: value
    for index, value in enumerate(readings)
    if -50 <= value <= 50
}


# Set comprehension
temperature_set = {
    value
    for value in readings
    if -50 <= value <= 50
}


# Alarm minutes using enumerate
alarm_minutes = [
    index + 1
    for index, value in enumerate(readings)
    if -50 <= value <= 50 and not (2 <= value <= 8)
]


print("SENSOR REPORT")
print("Total readings:", len(readings))
print("Valid readings:", len(valid_celsius))
print("Invalid readings:", len(readings) - len(valid_celsius))
print("First 5 Celsius:", valid_celsius[:5])
print("First 5 Fahrenheit:", fahrenheit_loop[:5])
print("Alarm minutes:", alarm_minutes[:20])
print("Dictionary entries:", len(temperature_dictionary))
print("Unique valid temperatures:", len(temperature_set))


# Verify three approaches
print("\nRESULT VERIFICATION")

print(
    "Loop and comprehension identical:",
    using_loop(readings) == using_comprehension(readings)
)

print(
    "Loop and filter-map identical:",
    all(
        abs(a - b) < 1e-9
        for a, b in zip(
            fahrenheit_loop,
            using_filter_map(readings)
        )
    )
)


# Performance investigation
print("\nPERFORMANCE COMPARISON")
print("Size          Loop          Comprehension       Filter-map")

for size in [10000, 100000, 1000000]:

    data = [
        random.uniform(-60, 60)
        for _ in range(size)
    ]

    start = time.perf_counter()
    result1 = using_loop(data)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = using_comprehension(data)
    t2 = time.perf_counter() - start

    start = time.perf_counter()
    result3 = using_filter_map(data)
    t3 = time.perf_counter() - start

    print(
        f"{size:<14}"
        f"{t1:.6f} s   "
        f"{t2:.6f} s   "
        f"{t3:.6f} s"
    )

    print("All results identical:", result1 == result2)


# Memory investigation
print("\nMEMORY COMPARISON")

large_data = list(range(100000))

list_result = [x * 2 for x in large_data]
generator_result = (x * 2 for x in large_data)

print("List memory:", sys.getsizeof(list_result), "bytes")
print("Generator memory:", sys.getsizeof(generator_result), "bytes")


# Edge cases
print("\nEDGE CASE TESTING")

all_valid = [2, 3, 4, 5, 6, 7, 8]
all_invalid = [100, -100, 60, -60]

print("All valid:", using_comprehension(all_valid))
print("All invalid:", using_comprehension(all_invalid))
print("Empty input:", using_comprehension([]))
