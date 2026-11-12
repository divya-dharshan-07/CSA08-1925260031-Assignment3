"""Q3: Farmer helpline complaint analysis with dictionaries and Counter."""
import random
import re
import time
from collections import Counter, defaultdict


calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}


def frequencies(texts, stop):
    """Return word -> count, using dict.get()."""
    counts = {}
    for text in texts:
        for word in re.findall(r"\b[a-z]+\b", text.lower()):
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts


def top(counts, k):
    """Sort by descending count, then alphabetical word."""
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]


def main():
    print("Expected example:", top(frequencies(calls, STOP), 3))

    by_district = defaultdict(list)
    complaints = [
        ("Sivaganga", "Seeds were delayed"),
        ("Madurai", "Paddy crop leaves turning yellow"),
        ("Sivaganga", "Fertiliser price is high"),
    ]
    for district, complaint in complaints:
        by_district[district].append(complaint)
    print("Complaints by district:", dict(by_district))

    print("\nEdge cases:")
    print("Empty:", frequencies([""], STOP))
    print("Case/punctuation:", frequencies(["SEEDS, seeds! Price? price."], STOP))

    print("\nBenchmark (seconds; generated text, timings vary):")
    random.seed(42)
    vocabulary = ["seed", "paddy", "fertiliser", "water", "price", "crop", "loan", "subsidy"]
    for n in (1_000, 10_000, 100_000):
        texts = [
            " ".join(random.choices(vocabulary, k=12))
            for _ in range(n)
        ]
        words = [w for t in texts for w in re.findall(r"\b[a-z]+\b", t.lower())]
        start = time.perf_counter()
        dictionary_counts = frequencies(texts, set())
        dict_time = time.perf_counter() - start
        start = time.perf_counter()
        counter_counts = Counter(words)
        counter_time = time.perf_counter() - start
        start = time.perf_counter()
        distinct = set(words)
        list_count_result = {word: words.count(word) for word in distinct}
        list_count_time = time.perf_counter() - start
        print(
            f"complaints={n:>6}: dict={dict_time:.6f}s, "
            f"Counter={counter_time:.6f}s, list.count={list_count_time:.6f}s, "
            f"same={dictionary_counts == counter_counts == list_count_result}"
        )


if __name__ == "__main__":
    main()
