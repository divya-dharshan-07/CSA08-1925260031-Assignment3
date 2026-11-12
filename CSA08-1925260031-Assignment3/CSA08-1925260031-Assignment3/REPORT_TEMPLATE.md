# Assignment 3 – CO3 Report

**Name:** Divya Dharshan  
**Register number:** 1925260031  
**Repository:** CSA08-1925260031-Assignment3  
**GitHub link:** [Paste your working repository URL here]  
**Python version:** [Fill in after running `python --version`]

## Execution evidence and measurements

For every question, paste your own output screenshot and record the results from your own computer. Timings vary by device and should never be invented or copied.

| Question | Program executed? | Screenshot added? | Measurements recorded? |
|---|---|---|---|
| Q1 | [ ] | [ ] | [ ] |
| Q2 | [ ] | [ ] | [ ] |
| Q3 | [ ] | [ ] | [ ] |
| Q4 | [ ] | [ ] | [ ] |
| Q5 | [ ] | [ ] | [ ] |
| Q6 | [ ] | [ ] | [ ] |
| Q7 | [ ] | [ ] | [ ] |

## Q1 – Lists and slicing

The program stores 365 daily rainfall values in a list. Weekly totals are calculated with slices. The 7-day moving average is calculated both by repeatedly summing each window and by maintaining a running sum.

**Pseudocode – running moving average**
1. If fewer than 7 readings exist, return an empty list.
2. Calculate the sum of the first 7 readings.
3. Append that sum divided by 7.
4. For each next index, subtract the value leaving the window and add the new value entering it.
5. Append the updated sum divided by 7.

`readings[7:14]` selects indices 7 through 13; `readings[-7:]` selects the final seven values; `readings[::7]` selects every seventh value beginning at index 0.

A list is suitable because it is ordered, supports indexing/slicing, and can grow. `append` is amortized O(1); `insert` and `pop` at the front/middle are O(n) because elements shift; `sort` is O(n log n). Naive moving average performs up to 7 additions per output, approximately 7(n−6), which is O(7n)=O(n). Running sum performs 7 initial additions and two updates per later window, approximately 7+2(n−7), also O(n), but with a smaller constant factor.

The running-window `deque(maxlen=7)` makes window updates efficient and uses O(7)=O(1) window space. Keeping all readings still uses O(n). A date-keyed dictionary offers convenient date lookup but requires explicit date ordering for sequential calculations. A late insertion into a list is O(n) due to shifting; for a frequently updated chronological stream, a deque or date-keyed structure may be preferable.

**Record your own benchmark output from `rainfall.py`.**

## Q2 – Tuples, mutability and copying

A tuple is hashable when all its elements are hashable, so a coordinate tuple can be a dictionary key. A list is mutable and unhashable, so it cannot be a dictionary key.

Bad grid: all three outer-list entries refer to the same inner list. Correct grid: each row is a separately created list. `copy.copy` and slicing create shallow copies: the outer container is new, but nested objects are shared. `copy.deepcopy` recursively copies nested objects. A shallow copy is enough for a flat list or when nested values are intentionally shared; deep copy is needed when nested mutable objects must be independent.

Python passes object references to functions. Mutating a list parameter mutates the same list object observed by the caller. Rebinding the local parameter does not rebind the caller's variable.

The tuple itself is immutable, but a mutable list stored inside a tuple can still be changed. Immutability protects the tuple's item references from reassignment; it does not recursively freeze nested objects.

For `[[0] * 3] * 3`, the three rows point to one inner list. For `[[0 for _ in range(cols)] for _ in range(rows)]`, each row is independent. Both list-of-lists and a dictionary keyed by `(row, col)` have average O(1) cell access. A dense grid uses O(rows × cols); a sparse dictionary uses O(number of non-empty cells), but missing cells need a default value.

## Q3 – Dictionaries

The program tokenises complaint text, normalises case, removes punctuation and stop words, and counts terms with a dictionary. Dictionary lookup uses hashing: average lookup/insertion is O(1), although collisions can make worst-case operations O(n). Counting all words with a dictionary is O(n) average; repeatedly calling `list.count` for each of d distinct words costs O(n × d).

Python 3.7+ guarantees dictionary insertion order. `keys()`, `values()` and `items()` are dynamic views reflecting the dictionary; `items()` yields key-value pairs. The top-k result is sorted by descending count and then alphabetically, so `price` precedes `received` when both have count 2.

`collections.Counter` is a specialised and concise frequency-counting tool, generally O(n) average. For a large daily workload, use a dictionary loop or `Counter`; both avoid repeated full-list scans. The program compares timings for generated complaint data.

## Q4 – Sets

The program uses set intersection (`&`) for students in both electives, symmetric difference (`^`) for students in exactly one, and difference (`-`) for students in neither. Union (`|`) gives everyone registered in at least one elective.

A set stores unique hashable elements, so duplicates are removed. Membership is average O(1) for a set and O(n) for a list. Lists cannot be set elements because they are mutable/unhashable; tuples can be elements when all their contents are hashable.

Venn diagram interpretation:
- Intersection: overlap of the two circles.
- Symmetric difference: the two non-overlapping regions.
- Union: both circles, including overlap.
- Neither: outside both circles but inside the universe of all students.

Converting a list to a set is useful for deduplication and repeated membership tests, but it loses duplicate counts and positional order. Set operations are average O(n+m). Nested list comparisons are O(n×m); sorting both lists and merging them is O(n log n + m log m), with extra storage depending on implementation.

## Q5 – List comprehension

A conditional list comprehension has the form `[expression for item in iterable if condition]`. A comprehension is concise for a simple transformation/filter; a normal loop is clearer when there are multiple branches, side effects, or complex error handling.

A list comprehension creates and stores all results (O(n) memory). A generator expression produces values lazily (typically O(1) auxiliary memory, excluding the source), while both take O(n) time to consume. The program compares a loop, comprehension, and `filter`/`map`, checks equal results, and measures list versus generator object size. `sys.getsizeof(generator)` measures only the generator object, not all memory eventually consumed.

Dictionary comprehension example: `{minute: c for minute, c in enumerate(readings) if -50 <= c <= 50}`. Set comprehension example: `{c for c in readings if -50 <= c <= 50}`. The alarm condition is valid sensor data outside the safe 2–8 °C range.

## Q6 – Nested railway timetable

The outer dictionary maps train number to train details. Each detail dictionary stores the train name, a list of stops, and a set of running days. Each stop is a tuple `(station, arrival, departure)`: its fields are fixed together. A set efficiently checks whether a day is served.

A station query without an index scans train records and their stops, O(total stops). An index maps station names to candidate train numbers, reducing work to O(number of trains serving that station), plus day checks. The index costs additional O(total indexed train-stop relationships) memory and must be updated when the timetable changes.

For a train `t`, the departure from its third stop is `timetable[train_no]["stops"][2][2]`.

A flat list of `(train, station, arrival, departure, days)` records can also answer queries by scanning all records in O(total stops). It is simple, but the nested dictionary plus station index is faster for repeated station queries.

## Q7 – Contact merging

The program uses normalised phone numbers as dictionary keys. It removes non-digits and strips a leading country code `91` for Indian 10-digit mobile numbers. Each grouped contact stores sets of original phone formats and email addresses, plus a display name. Contacts with no usable phone number are kept separately because the selected matching rule cannot safely identify them.

**Pseudocode**
1. For each contact, normalise each phone number.
2. If at least one normalised number exists, use each number as a key and merge the contact's numbers/emails into the matching group.
3. If there is no usable number, preserve it as an unmatched record rather than guessing identity from name alone.
4. Merge groups that share a normalised number.
5. Sort and display the merged contacts.

Dictionary grouping is O(n) average for n contact records (plus the total number of phone/email fields). Comparing every pair is O(n²). Two people with the same name but different phone numbers remain separate. A limitation is that changed or missing phone numbers can prevent the same person from being recognised; a shared/recycled phone number can also cause a false merge. Real contact merging should ask for confirmation in ambiguous cases.

## Final conclusion

Python data structures should be selected according to the operations required: lists for ordered mutable sequences, tuples for fixed records, dictionaries for key-based lookup, and sets for unique membership and set algebra. The best choice balances clarity, time, memory, and the information that must be preserved.
