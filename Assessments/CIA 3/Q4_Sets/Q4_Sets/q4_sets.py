
import random
import time


# Elective registrations
ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}


# Set operations
both = ai_elective & iot_elective

exactly_one = ai_elective ^ iot_elective

neither = all_students - (ai_elective | iot_elective)


print("ELECTIVE REGISTRATION REPORT")
print("AI students:", sorted(ai_elective))
print("IoT students:", sorted(iot_elective))

print("\nRESULTS")
print("clash      :", sorted(both))
print("exactly one:", sorted(exactly_one))
print("neither    :", sorted(neither))


# Verify using set methods
both_method = ai_elective.intersection(iot_elective)

exactly_one_method = ai_elective.symmetric_difference(
    iot_elective
)

neither_method = all_students.difference(
    ai_elective.union(iot_elective)
)

print("\nSET METHOD VERIFICATION")
print("Intersection correct:", both == both_method)
print("Symmetric difference correct:",
      exactly_one == exactly_one_method)
print("Difference correct:", neither == neither_method)


# Duplicate removal
registrations = [
    "192311001", "192311004",
    "192311001", "192311007",
    "192311004"
]

unique_registrations = set(registrations)

print("\nDUPLICATE REMOVAL")
print("Original:", registrations)
print("Unique:", sorted(unique_registrations))


# Membership performance comparison
print("\nMEMBERSHIP PERFORMANCE")
print("Size          List Time       Set Time")

for size in [10000, 100000, 1000000]:

    data = list(range(size))
    data_set = set(data)

    target = size - 1

    start = time.perf_counter()

    for _ in range(1000):
        target in data

    list_time = time.perf_counter() - start

    start = time.perf_counter()

    for _ in range(1000):
        target in data_set

    set_time = time.perf_counter() - start

    print(
        f"{size:<14}"
        f"{list_time:.6f} s   "
        f"{set_time:.6f} s"
    )


# Nested loops versus set intersection
print("\nINTERSECTION PERFORMANCE")

a = set(range(5000))
b = set(range(2500, 7500))

list_a = list(a)
list_b = list(b)

start = time.perf_counter()

nested_result = []

for x in list_a:
    for y in list_b:
        if x == y:
            nested_result.append(x)

nested_time = time.perf_counter() - start

start = time.perf_counter()
set_result = a & b
set_time = time.perf_counter() - start

print("Nested loop time:", round(nested_time, 6), "seconds")
print("Set operation time:", round(set_time, 6), "seconds")
print("Results identical:", set(nested_result) == set_result)


# Edge cases
print("\nEDGE CASE TESTING")

empty = set()

print("Empty intersection:", empty & ai_elective)
print("Identical intersection:", ai_elective & ai_elective)
print("Identical difference:", ai_elective ^ ai_elective)
