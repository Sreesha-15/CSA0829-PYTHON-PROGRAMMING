
import random
import string
import time
from collections import Counter


# Given complaint data
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


# Count word frequencies using dictionary get()
def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = text.lower().split()

        for word in words:
            word = word.strip(string.punctuation)

            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


# Top k words: count descending, alphabetical for ties
def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


# Demonstrate setdefault()
def group_by_district(records):
    grouped = {}

    for district, complaint in records:
        grouped.setdefault(district, []).append(complaint)

    return grouped


# District complaint records
records = [
    ("Chennai", "Seeds not received"),
    ("Madurai", "Fertiliser price high"),
    ("Chennai", "Water supply problem"),
    ("Salem", "Crop disease"),
    ("Madurai", "Subsidy not received")
]

print("WORD FREQUENCIES")
result = frequencies(calls, STOP)
print(result)

print("\nTOP 3 WORDS")
print(top(result, 3))

print("\nDISTRICT GROUPING")
district_groups = group_by_district(records)

for district, complaints in district_groups.items():
    print(district, ":", complaints)


# Dictionary counting
def dictionary_count(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


# list.count() counting
def list_count(words):
    unique_words = set(words)

    return {
        word: words.count(word)
        for word in unique_words
    }


# Generate experimental data
vocabulary = [
    "seeds", "water", "fertiliser", "crop",
    "subsidy", "price", "soil", "harvest"
]

def generate_complaints(count):
    return [
        " ".join(random.choices(vocabulary, k=8))
        for _ in range(count)
    ]


# Benchmark all three methods
print("\nPERFORMANCE COMPARISON")
print("Complaints     Dictionary     list.count()     Counter")

for size in [1000, 10000, 100000]:

    data = generate_complaints(size)
    words = " ".join(data).split()

    start = time.perf_counter()
    dictionary_result = dictionary_count(words)
    dictionary_time = time.perf_counter() - start

    start = time.perf_counter()
    list_result = list_count(words)
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    counter_result = Counter(words)
    counter_time = time.perf_counter() - start

    print(
        f"{size:<14}"
        f"{dictionary_time:.6f} s   "
        f"{list_time:.6f} s   "
        f"{counter_time:.6f} s"
    )

    print(
        "Results identical:",
        dictionary_result == list_result == dict(counter_result)
    )


# Edge case testing
print("\nEDGE CASE TESTING")

test_calls = [
    "",
    "SEEDS seeds Seeds",
    "Seeds, price! high."
]

print(frequencies(test_calls, STOP))


# Dictionary views
print("\nDICTIONARY VIEWS")
print("Keys:", result.keys())
print("Values:", result.values())
print("Items:", result.items())
