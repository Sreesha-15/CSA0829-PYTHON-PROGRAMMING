
import copy
import sys
import time


# Tuple coordinates as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar",
    (13.0674, 80.2376): "Nungambakkam"
}

print("BUS STOP DETAILS")

for (latitude, longitude), name in stops.items():
    print(name, ":", latitude, longitude)


# Aliasing problem
rows, cols = 3, 4

bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("\nGRID COMPARISON")
print("bad :", bad)
print("good:", good)
print("Bad rows same object:", bad[0] is bad[1])
print("Good rows same object:", good[0] is good[1])

print("Bad row IDs:", [id(row) for row in bad])
print("Good row IDs:", [id(row) for row in good])


# Aliasing and copying
original = [[10, 20], [30, 40]]

alias = original
shallow_copy = copy.copy(original)
slice_copy = original[:]
deep_copy = copy.deepcopy(original)

original[0][0] = 99
original[0].append(50)

print("\nCOPYING COMPARISON")
print("Original:", original)
print("Alias:", alias)
print("Shallow copy:", shallow_copy)
print("Slice copy:", slice_copy)
print("Deep copy:", deep_copy)

print("Alias is original:", alias is original)
print("Shallow copy is original:", shallow_copy is original)
print("Deep copy is original:", deep_copy is original)


# Tuple unpacking
print("\nTUPLE UNPACKING")

coordinates = [
    ("Central", 13.0827, 80.2707),
    ("T Nagar", 13.0418, 80.2341),
    ("Guindy", 13.0067, 80.2206)
]

for name, latitude, longitude in coordinates:
    print(name, latitude, longitude)


# A list inside a tuple can still be changed
data = ("Bus", [10, 20, 30])
data[1].append(40)

print("\nLIST INSIDE TUPLE")
print(data)


# Function modifying a list
def add_stop(route):
    route.append("Velachery")


my_route = ["Central", "Guindy"]
add_stop(my_route)

print("\nFUNCTION ARGUMENT")
print(my_route)


# Memory comparison
values = list(range(1_000_000))
tuple_values = tuple(values)

print("\nMEMORY COMPARISON")
print("List size:", sys.getsizeof(values), "bytes")
print("Tuple size:", sys.getsizeof(tuple_values), "bytes")


# Creation and indexing benchmark
size = 100_000

start = time.perf_counter()
test_list = list(range(size))
list_creation = time.perf_counter() - start

start = time.perf_counter()
test_tuple = tuple(range(size))
tuple_creation = time.perf_counter() - start

start = time.perf_counter()
list_result = test_list[size // 2]
list_indexing = time.perf_counter() - start

start = time.perf_counter()
tuple_result = test_tuple[size // 2]
tuple_indexing = time.perf_counter() - start

print("\nPERFORMANCE")
print("List creation:", round(list_creation, 6), "seconds")
print("Tuple creation:", round(tuple_creation, 6), "seconds")
print("List indexing:", round(list_indexing, 9), "seconds")
print("Tuple indexing:", round(tuple_indexing, 9), "seconds")


# Dictionary lookup
print("\nDICTIONARY LOOKUP")
print(stops[(13.0418, 80.2341)])


# Unhashable list test
print("\nLIST AS DICTIONARY KEY")

try:
    invalid = {[13.0418, 80.2341]: "T Nagar"}
except TypeError as error:
    print("Error:", error)
