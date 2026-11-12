"""Q6: Nested railway timetable and station index."""
import random
import time
from collections import defaultdict


def build_timetable():
    return {
        "12601": {
            "name": "Chennai Express",
            "stops": [
                ("Chennai", "06:00", "06:15"),
                ("Katpadi", "08:20", "08:22"),
                ("Jolarpettai", "10:00", "10:05"),
            ],
            "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
        },
        "12602": {
            "name": "Bengaluru Mail",
            "stops": [
                ("Chennai", "07:00", "07:20"),
                ("Arakkonam", "08:10", "08:12"),
                ("Katpadi", "09:30", "09:35"),
            ],
            "days": {"Mon", "Wed", "Fri"},
        },
        "12603": {
            "name": "Vaigai Express",
            "stops": [
                ("Chennai", "13:15", "13:30"),
                ("Villupuram", "15:00", "15:02"),
                ("Madurai", "19:00", "19:10"),
            ],
            "days": {"Tue", "Thu", "Sat"},
        },
        "12604": {
            "name": "Pandian Express",
            "stops": [
                ("Chennai", "21:00", "21:15"),
                ("Tiruchirappalli", "03:00", "03:05"),
                ("Madurai", "05:30", "05:40"),
            ],
            "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
        },
        "12605": {
            "name": "West Coast Express",
            "stops": [
                ("Chennai", "11:00", "11:10"),
                ("Katpadi", "13:00", "13:05"),
                ("Bengaluru", "16:00", "16:10"),
            ],
            "days": {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"},
        },
    }


def build_station_index(timetable):
    index = defaultdict(list)
    for train_no, details in timetable.items():
        for station, arrival, departure in details["stops"]:
            index[station].append((train_no, arrival, departure))
    return index


def find_trains(timetable, station, day):
    matches = []
    for train_no, details in timetable.items():
        if day in details["days"]:
            for stop_station, arrival, departure in details["stops"]:
                if stop_station == station:
                    matches.append((train_no, details["name"], arrival, departure))
    return matches


def find_trains_indexed(timetable, index, station, day):
    matches = []
    for train_no, arrival, departure in index.get(station, []):
        if day in timetable[train_no]["days"]:
            matches.append((train_no, timetable[train_no]["name"], arrival, departure))
    return matches


def main():
    timetable = build_timetable()
    index = build_station_index(timetable)
    station, day = "Katpadi", "Mon"
    result = find_trains(timetable, station, day)
    print(f"Trains stopping at {station} on {day}:")
    for train in sorted(result, key=lambda item: item[3]):
        print(train)
    print("Unknown station:", find_trains_indexed(timetable, index, "Atlantis", day))
    print("Train 12603 on Monday (does not run):",
          find_trains_indexed(timetable, index, "Madurai", "Mon")
          if "Mon" in timetable["12603"]["days"] else [])
    print("Third stop departure of 12601:", timetable["12601"]["stops"][2][2])
    print("\nNeatly formatted timetable:")
    for train_no, details in timetable.items():
        print(f"\n{train_no} – {details['name']} | Days: {', '.join(sorted(details['days']))}")
        for stop in details["stops"]:
            print(f"  {stop[0]:18} arrival {stop[1]} departure {stop[2]}")

    print("\nGenerated-data benchmark (seconds; timings vary):")
    random.seed(42)
    stations = ["Chennai", "Katpadi", "Madurai", "Salem", "Erode", "Bengaluru"]
    for n in (100, 1_000, 10_000):
        generated = {}
        for i in range(n):
            chosen = random.sample(stations, 4)
            generated[str(i)] = {
                "name": f"Train {i}",
                "stops": [(s, "10:00", "10:05") for s in chosen],
                "days": {"Mon", "Wed", "Fri"},
            }
        generated_index = build_station_index(generated)
        index_shallow_bytes = sys.getsizeof(generated_index)
        index_entries = sum(sys.getsizeof(entries) for entries in generated_index.values())
        index_storage_bytes = index_shallow_bytes + index_entries
        start = time.perf_counter()
        plain = find_trains(generated, "Madurai", "Mon")
        plain_time = time.perf_counter() - start
        start = time.perf_counter()
        indexed = find_trains_indexed(generated, generated_index, "Madurai", "Mon")
        index_time = time.perf_counter() - start
        print(f"trains={n:>5}: scan={plain_time:.6f}s, indexed={index_time:.6f}s, same={sorted(plain)==sorted(indexed)}")


if __name__ == "__main__":
    main()
