"""Q4: Elective registration clash detection with sets."""
import random
import time


def main():
    ai_elective = {"192311001", "192311004", "192311007", "192311009"}
    iot_elective = {"192311002", "192311004", "192311009", "192311010"}
    all_students = {f"1923110{i:02d}" for i in range(1, 11)}

    # TODO 1 completed using set operators.
    both = ai_elective & iot_elective
    exactly_one = ai_elective ^ iot_elective
    neither = all_students - (ai_elective | iot_elective)

    print("clash      :", sorted(both))
    print("exactly one:", sorted(exactly_one))
    print("neither    :", sorted(neither))

    # Same result using set methods.
    both_method = ai_elective.intersection(iot_elective)
    exactly_one_method = ai_elective.symmetric_difference(iot_elective)
    neither_method = all_students.difference(ai_elective.union(iot_elective))
    print("Methods match:", (both, exactly_one, neither) ==
          (both_method, exactly_one_method, neither_method))

    print("\nEdge cases:")
    print("Empty intersection:", set() & ai_elective)
    print("Identical symmetric difference:", ai_elective ^ ai_elective)

    print("\nMembership benchmark (seconds; timings vary):")
    random.seed(42)
    for n in (10_000, 100_000, 1_000_000):
        values = [str(i) for i in range(n)]
        value_set = set(values)
        target = str(n - 1)
        repeats = 2_000
        start = time.perf_counter()
        for _ in range(repeats):
            target in values
        list_time = time.perf_counter() - start
        start = time.perf_counter()
        for _ in range(repeats):
            target in value_set
        set_time = time.perf_counter() - start
        print(f"n={n:>7}: list={list_time:.6f}s, set={set_time:.6f}s")

    print("\nCommon-element benchmark:")
    for n in (1_000, 5_000, 10_000):
        left = list(range(n))
        right = list(range(n // 2, n + n // 2))
        start = time.perf_counter()
        nested = {a for a in left for b in right if a == b}
        nested_time = time.perf_counter() - start
        start = time.perf_counter()
        efficient = set(left) & set(right)
        set_time = time.perf_counter() - start
        print(f"n={n:>5}: nested={nested_time:.6f}s, set intersection={set_time:.6f}s, same={nested == efficient}")


if __name__ == "__main__":
    main()
