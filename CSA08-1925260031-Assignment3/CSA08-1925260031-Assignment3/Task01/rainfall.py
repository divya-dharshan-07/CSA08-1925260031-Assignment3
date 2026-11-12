"""Q1: Daily rainfall records – list slicing and moving averages."""
import random
import time
import math


def weekly_totals(readings):
    return [sum(readings[i:i + 7]) for i in range(0, len(readings), 7)]


def moving_average_naive(readings, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    return [
        sum(readings[i:i + window]) / window
        for i in range(len(readings) - window + 1)
    ]


def moving_average_running(readings, window=7):
    if window <= 0:
        raise ValueError("window must be positive")
    if len(readings) < window:
        return []
    current_sum = sum(readings[:window])
    averages = [current_sum / window]
    for i in range(window, len(readings)):
        current_sum += readings[i] - readings[i - window]
        averages.append(current_sum / window)
    return averages


def main():
    random.seed(42)
    readings = [round(random.uniform(0, 40), 1) for _ in range(365)]

    totals = weekly_totals(readings)
    wettest = max(range(len(totals)), key=totals.__getitem__)
    driest = min(range(len(totals)), key=totals.__getitem__)
    dry_days = [day + 1 for day, value in enumerate(readings) if value == 0]
    averages = moving_average_running(readings)

    print("First 5 readings:", readings[:5])
    print("Number of weekly totals:", len(totals))
    print("Wettest week (1-based):", wettest + 1, "total:", totals[wettest])
    print("Driest week (1-based):", driest + 1, "total:", totals[driest])
    print("First 5 moving averages:", [round(x, 2) for x in averages[:5]])
    print("Dry days (1-based):", dry_days)
    print("readings[7:14]:", readings[7:14])
    print("readings[-7:]:", readings[-7:])
    print("readings[::7] (first 5):", readings[::7][:5])

    print("\nEdge cases:")
    print("Empty:", moving_average_running([]))
    print("Short:", moving_average_running([1, 2, 3, 4, 5, 6]))

    print("\nBenchmark (seconds; actual values depend on your computer):")
    for n in (365, 36_500, 365_000):
        data = [random.random() * 40 for _ in range(n)]
        start = time.perf_counter()
        naive = moving_average_naive(data)
        naive_time = time.perf_counter() - start
        start = time.perf_counter()
        fast = moving_average_running(data)
        fast_time = time.perf_counter() - start
        equal = all(
    math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
    for a, b in zip(naive, fast)
)

print(f"n={n:>7}: naive={naive_time:.6f}, running={fast_time:.6f}, equal={equal}")


if __name__ == "__main__":
    main()
