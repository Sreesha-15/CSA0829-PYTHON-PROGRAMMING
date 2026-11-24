
# Q4 - Building Long Text

import time


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return "".join(p + ";" for p in parts)


def build_fstring(count):
    lines = []
    for i in range(count):
        line = f"Item{i}:Rs{i % 50};"
        lines.append(line)
    return "".join(lines)


def measure(count, repeats=3):
    items = [f"Item{i}:Rs{i % 50}" for i in range(count)]

    plus_times = []
    join_times = []
    fstring_times = []

    for _ in range(repeats):
        start = time.perf_counter()
        a = build_plus(items)
        plus_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        b = build_join(items)
        join_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        c = build_fstring(count)
        fstring_times.append(time.perf_counter() - start)

    print("\nNumber of lines:", count)
    print("Same output:", a == b == c)
    print("Output length:", len(a))
    print(f"Average += time: {sum(plus_times)/repeats:.6f} seconds")
    print(f"Average join time: {sum(join_times)/repeats:.6f} seconds")
    print(f"Average f-string time: {sum(fstring_times)/repeats:.6f} seconds")


for size in [1000, 10000, 200000]:
    measure(size)
