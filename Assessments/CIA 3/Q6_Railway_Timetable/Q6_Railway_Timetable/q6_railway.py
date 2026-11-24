
import random
import time
import sys


# Railway timetable with five trains
timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:15")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12602": {
        "name": "Southern Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Vellore", "09:00", "09:05"),
            ("Bangalore", "12:00", "12:15")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12603": {
        "name": "Coastal Express",
        "stops": [
            ("Coimbatore", "05:00", "05:10"),
            ("Salem", "07:00", "07:05"),
            ("Chennai", "10:00", "10:15")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}
    },

    "12604": {
        "name": "Hill Express",
        "stops": [
            ("Madurai", "06:00", "06:10"),
            ("Trichy", "08:00", "08:05"),
            ("Chennai", "11:00", "11:15")
        ],
        "days": {"Sat", "Sun"}
    },

    "12605": {
        "name": "City Express",
        "stops": [
            ("Bangalore", "06:30", "06:40"),
            ("Katpadi", "09:00", "09:05"),
            ("Chennai", "12:00", "12:15")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}
    }
}


# Display timetable
def display_timetable(data):
    print("RAILWAY TIMETABLE")

    for train_number, details in data.items():
        print("\nTrain:", train_number)
        print("Name:", details["name"])
        print("Running days:", sorted(details["days"]))

        for station, arrival, departure in details["stops"]:
            print(station, arrival, departure)


# Find trains at a station on a given day
def find_trains(data, station, day):
    results = []

    for train_number, details in data.items():

        if day not in details["days"]:
            continue

        for name, arrival, departure in details["stops"]:

            if name.lower() == station.lower():
                results.append(
                    (train_number, details["name"], departure)
                )
                break

    return sorted(results, key=lambda item: item[2])


display_timetable(timetable)


# Query
print("\nSTATION SEARCH")

results = find_trains(timetable, "Chennai", "Mon")

for train_number, name, departure in results:
    print(train_number, name, departure)


# Unknown station
print("\nUNKNOWN STATION")
print(find_trains(timetable, "Mumbai", "Mon"))


# Train not running on requested day
print("\nDAY FILTER")
print(find_trains(timetable, "Chennai", "Sun"))


# Build station index
def build_station_index(data):
    index = {}

    for train_number, details in data.items():

        for station, arrival, departure in details["stops"]:

            index.setdefault(station, []).append(
                (train_number, departure)
            )

    return index


station_index = build_station_index(timetable)


# Indexed station query
def indexed_query(data, index, station, day):
    results = []

    for train_number, departure in index.get(station, []):

        if day in data[train_number]["days"]:
            results.append(
                (train_number, data[train_number]["name"], departure)
            )

    return sorted(results, key=lambda item: item[2])


print("\nINDEXED QUERY")
print(indexed_query(timetable, station_index, "Chennai", "Mon"))


# Large timetable generation
def generate_timetable(count):
    stations = [
        "Chennai", "Bangalore", "Madurai",
        "Salem", "Trichy", "Katpadi"
    ]

    generated = {}

    for i in range(count):

        train_number = str(10000 + i)

        selected_stations = random.sample(stations, 3)

        generated[train_number] = {
            "name": f"Train {train_number}",
            "stops": [
                (station, "08:00", "08:10")
                for station in selected_stations
            ],
            "days": {"Mon", "Wed", "Fri"}
        }

    return generated


# Benchmark station queries
print("\nSTATION QUERY PERFORMANCE")
print("Trains        Scan Time       Indexed Time")

for size in [100, 1000, 10000]:

    data = generate_timetable(size)

    start = time.perf_counter()
    scan_result = find_trains(data, "Chennai", "Mon")
    scan_time = time.perf_counter() - start

    start = time.perf_counter()
    index = build_station_index(data)
    index_build_time = time.perf_counter() - start

    start = time.perf_counter()
    index_result = indexed_query(data, index, "Chennai", "Mon")
    indexed_time = time.perf_counter() - start

    print(
        f"{size:<14}"
        f"{scan_time:.6f} s   "
        f"{indexed_time:.6f} s"
    )

    print("Results identical:", scan_result == index_result)
    print("Index build time:", round(index_build_time, 6), "seconds")


# Memory of index
print("\nINDEX MEMORY")
print("Index dictionary size:", sys.getsizeof(station_index), "bytes")
