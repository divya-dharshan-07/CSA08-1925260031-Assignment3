"""Q5: Cleaning sensor readings with loops, comprehensions, map and filter."""
import random
import sys
import time


def clean_loop(readings):
    valid = []
    for celsius in readings:
        if -50 <= celsius <= 50:
            valid.append(celsius)
    fahrenheit = []
    for celsius in valid:
        fahrenheit.append(celsius * 9 / 5 + 32)
    return valid, fahrenheit


def clean_comprehension(readings):
    valid = [c for c in readings if -50 <= c <= 50]
    fahrenheit = [c * 9 / 5 + 32 for c in valid]
    return valid, fahrenheit


def clean_map_filter(readings):
    valid = list(filter(lambda c: -50 <= c <= 50, readings))
    fahrenheit = list(map(lambda c: c * 9 / 5 + 32, valid))
    return valid, fahrenheit


def main():
    readings = [2.0, 5.5, 9.0, 55.0, -60.0, 7.0, 1.0, 51.0]
    loop_result = clean_loop(readings)
    comp_result = clean_comprehension(readings)
    map_result = clean_map_filter(readings)
    print("Valid Celsius:", loop_result[0])
    print("Fahrenheit:", [round(x, 2) for x in loop_result[1]])
    print("All implementations equal:", loop_result == comp_result == map_result)
    alarms = [
        minute for minute, c in enumerate(readings, start=1)
        if -50 <= c <= 50 and not (2 <= c <= 8)
    ]
    print("Alarm minutes (valid sensor data outside 2–8 C):", alarms)

    valid_dict = {minute: c for minute, c in enumerate(readings, start=1) if -50 <= c <= 50}
    valid_set = {c for c in readings if -50 <= c <= 50}
    print("Dictionary comprehension:", valid_dict)
    print("Set comprehension:", valid_set)

    print("\nEdge cases:")
    print("All valid:", clean_comprehension([2, 3, 4])[0])
    print("All invalid:", clean_comprehension([51, -51])[0])

    print("\nBenchmark (seconds; timings vary):")
    random.seed(42)
    for n in (10_000, 100_000, 1_000_000):
        data = [random.uniform(-60, 60) for _ in range(n)]
        timings = {}
        outputs = []
        for name, function in (
            ("loop", clean_loop),
            ("comprehension", clean_comprehension),
            ("map_filter", clean_map_filter),
        ):
            start = time.perf_counter()
            result = function(data)
            timings[name] = time.perf_counter() - start
            outputs.append(result)
        print(f"n={n:>7}: {timings}, identical={outputs[0] == outputs[1] == outputs[2]}")

    generator = (c for c in readings if -50 <= c <= 50)
    list_result = [c for c in readings if -50 <= c <= 50]
    print("\nShallow object sizes:")
    print("List comprehension bytes:", sys.getsizeof(list_result))
    print("Generator object bytes:", sys.getsizeof(generator))
    print("Note: generator size excludes the source and values produced later.")


if __name__ == "__main__":
    main()
