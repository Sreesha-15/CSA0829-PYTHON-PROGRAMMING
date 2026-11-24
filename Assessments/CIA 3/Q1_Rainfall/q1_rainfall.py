
import random
import time


# Generate daily rainfall readings
random.seed(42)
readings = [round(random.uniform(0, 50), 2) for _ in range(365)]


# Calculate weekly totals using slicing
weekly_totals = []

for i in range(0, len(readings), 7):
    week = readings[i:i + 7]
    weekly_totals.append(round(sum(week), 2))


# Find wettest and driest weeks
wettest_week = max(weekly_totals)
driest_week = min(weekly_totals)

print("WEEKLY RAINFALL REPORT")
print("Total readings:", len(readings))
print("Number of weeks:", len(weekly_totals))
print("Wettest week:", weekly_totals.index(wettest_week) + 1)
print("Wettest rainfall:", wettest_week, "mm")
print("Driest week:", weekly_totals.index(driest_week) + 1)
print("Driest rainfall:", driest_week, "mm")


# Naive moving average
def naive_moving_average(data, window=7):
    averages = []

    if len(data) < window:
        return averages

    for i in range(len(data) - window + 1):
        total = sum(data[i:i + window])
        averages.append(total / window)

    return averages


# Running sum moving average
def running_moving_average(data, window=7):
    averages = []

    if len(data) < window:
        return averages

    current_sum = sum(data[:window])
    averages.append(current_sum / window)

    for i in range(window, len(data)):
        current_sum += data[i] - data[i - window]
        averages.append(current_sum / window)

    return averages


# Find dry days
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("\nMOVING AVERAGE")
print("First 7-day average:", round(
    naive_moving_average(readings)[0], 2
))
print("Number of moving averages:", len(
    running_moving_average(readings)
))
print("Dry days:", dry_days)


# Explain slicing
print("\nSLICING EXAMPLES")
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7]:", readings[::7][:10])


# Experimental investigation
def benchmark(size):
    data = [random.uniform(0, 50) for _ in range(size)]

    start = time.perf_counter()
    naive = naive_moving_average(data)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    running = running_moving_average(data)
    running_time = time.perf_counter() - start

    print(
        f"{size:<12} {naive_time:.6f} s"
        f"       {running_time:.6f} s"
    )

    print("Results identical:", all(
        abs(a - b) < 1e-9 for a, b in zip(naive, running)
    ))


print("\nPERFORMANCE COMPARISON")
print("Readings     Naive Time       Running Sum Time")

for size in [365, 36500, 365000]:
    benchmark(size)


# Edge cases
print("\nEDGE CASE TESTING")
print("Empty list:", naive_moving_average([]))
print("Short list:", naive_moving_average([1, 2, 3, 4]))
print("All zeros:", running_moving_average([0] * 7))
