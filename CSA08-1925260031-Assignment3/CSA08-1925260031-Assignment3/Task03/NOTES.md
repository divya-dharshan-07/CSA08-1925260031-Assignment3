# Q3 – Dictionaries

The completed TODO 1 uses `dict.get(word, 0)` to increment counts. TODO 2 sorts with key `(-count, word)`, so counts descend and ties are alphabetical. In the supplied output, `price` comes before `received` because both have count 2 and `price` is alphabetically earlier.

Dictionary lookup uses a hash table. Average lookup/insertion is O(1); worst case can degrade with many collisions. Counting n words with a dictionary is O(n) average. Running `list.count` for each of d distinct words scans n values each time: O(n×d). `collections.Counter` is a specialised frequency dictionary and is also O(n) average.

Python 3.7+ guarantees insertion order. `keys()`, `values()`, and `items()` are dynamic views of keys, values, and key-value pairs. For 100,000 complaints, use a dictionary loop or `Counter`, not repeated `list.count`. The benchmark reports measurements from your computer.
