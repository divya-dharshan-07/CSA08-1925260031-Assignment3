"""Q2: Tuples, mutability, aliasing, shallow and deep copying."""
import copy
import sys
import time


def main():
    rows, cols = 3, 4
    bad = [[0] * cols] * rows
    bad[0][1] = 7

    # TODO 1 completed: each iteration creates a separate row list.
    good = [[0 for _ in range(cols)] for _ in range(rows)]
    good[0][1] = 7

    print("bad :", bad)
    print("good:", good)
    print(bad[0] is bad[1], good[0] is good[1])

    stops = {
        (13.0827, 80.2707): "Chennai Central",
        (13.0418, 80.2341): "T. Nagar",
    }
    print(stops[(13.0418, 80.2341)])
    try:
        stops[[13.0418, 80.2341]] = "Invalid key"
    except TypeError as error:
        print("List key error:", error)

    print("\nAliasing and copies:")
    original = [[1, 2], [3, 4]]
    alias = original
    shallow_copy = copy.copy(original)
    slice_copy = original[:]
    deep_copy = copy.deepcopy(original)
    original[0][0] = 99
    print("alias sees change:", alias)
    print("shallow nested item shared:", shallow_copy[0] is original[0])
    print("slice nested item shared:", slice_copy[0] is original[0])
    print("deep copy independent:", deep_copy)

    def change_first(values):
        values[0] = -1

    sample = [10, 20]
    change_first(sample)
    print("Caller list after function:", sample)

    packed = ("route-A", [1, 2, 3])
    packed[1].append(4)
    print("List inside immutable tuple can change:", packed)

    print("\nMemory comparison (shallow container size only):")
    values_list = list(range(1_000_000))
    values_tuple = tuple(values_list)
    print("list bytes:", sys.getsizeof(values_list))
    print("tuple bytes:", sys.getsizeof(values_tuple))

    print("\nCreation/indexing timing (seconds):")
    source = list(range(200_000))
    for label, constructor in (("list", list), ("tuple", tuple)):
        start = time.perf_counter()
        obj = constructor(source)
        create_time = time.perf_counter() - start
        start = time.perf_counter()
        checksum = sum(obj[i] for i in range(0, len(obj), 100))
        index_time = time.perf_counter() - start
        print(f"{label}: create={create_time:.6f}, index={index_time:.6f}, checksum={checksum}")


if __name__ == "__main__":
    main()
