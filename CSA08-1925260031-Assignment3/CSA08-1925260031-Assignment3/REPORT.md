# Assignment 3 – CO3 Report

**Name:** Divya Dharshan  
**Register number:** 1925260031  
**Repository:** CSA08-1925260031-Assignment3  
**GitHub link:** https://github.com/divya-dharshan-07/CSA08-1925260031-Assignment3  
**Python version:** To be confirmed. Run import sys; print(sys.version) in the same Python runtime used for the assignment.

## Execution evidence

All seven programs were run and their output screenshots were uploaded to their respective task folders. Benchmark timings below are the values reported from the student's runs. Timings vary by device and runtime.

| Question | Program executed? | Screenshot added? | Measurements recorded? |
|---|---|---|---|
| Q1 | Yes | Yes | Yes |
| Q2 | Yes | Yes | Yes |
| Q3 | Yes | Yes | Yes |
| Q4 | Yes | Yes | Yes |
| Q5 | Yes | Yes | Yes |
| Q6 | Yes | Yes | Yes |
| Q7 | Yes | Yes | Yes |

## Q1 – Lists and slicing

The program stores 365 daily rainfall values in a list. Weekly totals are calculated using slices. The 7-day moving average is calculated using both repeated window summation and a running sum.

**Running moving-average algorithm**
1. If fewer than 7 readings exist, return an empty list.
2. Calculate the sum of the first 7 readings.
3. Append that sum divided by 7.
4. For each next index, subtract the value leaving the window and add the new value entering it.
5. Append the updated sum divided by 7.

List slicing selects ranges or steps: readings[7:14] selects indices 7 through 13; readings[-7:] selects the final seven values; readings[::7] selects every seventh value beginning at index 0.

A list is suitable because it is ordered, supports indexing and slicing, and can grow. Appending is amortized O(1); inserting or removing at the front or middle is O(n) because elements shift. For a fixed window of 7, both moving-average methods are O(n), but the running-sum method performs fewer operations per output. It uses O(1) additional window space, excluding the output list.

**Recorded benchmark results**

| n | Naive (s) | Running sum (s) | Equal |
|---:|---:|---:|---|
| 365 | 0.000209 | 0.000063 | Yes |
| 36,500 | 0.012242 | 0.004286 | Yes |
| 365,000 | 0.121268 | 0.043036 | Yes |

The running-sum method was faster in these runs, and both implementations matched within floating-point tolerance.

## Q2 – Tuples, mutability and copying

A tuple is hashable when all its elements are hashable, so a coordinate tuple can be a dictionary key. A list is mutable and unhashable, so it cannot be a dictionary key.

The expression [[0] * 3] * 3 creates multiple references to the same inner list. A list comprehension creates independent rows. Shallow copying creates a new outer container while sharing nested objects; deep copying recursively copies nested objects. Python passes object references to functions, so mutating a list parameter changes the same list observed by the caller.

A tuple is immutable, but a mutable list stored inside a tuple can still be changed. Immutability protects the tuple's item references from reassignment; it does not recursively freeze nested objects.

**Recorded benchmark results**

| Type | Creation (s) | Indexing (s) | Checksum |
|---|---:|---:|---:|
| List | 0.001118 | 0.000151 | 199900000 |
| Tuple | 0.001572 | 0.000172 | 199900000 |

Reported object sizes were 8,000,056 bytes for the list and 8,000,040 bytes for the tuple. These values are environment-specific.

## Q3 – Dictionaries and complaint analysis

The program tokenises complaint text, normalises case, removes punctuation and stop words, and counts terms with a dictionary. Dictionary lookup and insertion are average O(1), so counting all words is O(n) average. Repeatedly calling list.count for each of d distinct words costs O(n × d). Counter is a specialised frequency-counting tool. The top-word output is sorted by descending count and then alphabetically.

**Recorded benchmark results**

| Complaints | Dictionary (s) | Counter (s) | list.count (s) | Same results |
|---:|---:|---:|---:|---|
| 1,000 | 0.007103 | 0.001691 | 0.002376 | Yes |
| 10,000 | 0.051248 | 0.010128 | 0.022649 | Yes |
| 100,000 | 0.441704 | 0.097078 | 0.166595 | Yes |

Counter was fastest among the three methods in these runs.

## Q4 – Sets and elective clash detection

The program uses set intersection (&) for students in both electives, symmetric difference (^) for students in exactly one, and difference (-) for students in neither. Union (|) gives everyone registered in at least one elective.

A set stores unique hashable elements. Membership is average O(1) for a set and O(n) for a list. Set operations are generally efficient because they use hashing.

**Recorded membership benchmark**

| n | List membership (s) | Set membership (s) |
|---:|---:|---:|
| 10,000 | 0.273467 | 0.000069 |
| 100,000 | 2.653233 | 0.000079 |
| 1,000,000 | 25.412370 | 0.000072 |

**Recorded common-element benchmark**

| n | Nested loops (s) | Set intersection (s) | Same |
|---:|---:|---:|---|
| 1,000 | 0.014742 | 0.000057 | Yes |
| 5,000 | 0.356507 | 0.000363 | Yes |
| 10,000 | 1.384618 | 0.000669 | Yes |

The results demonstrate the advantage of sets for repeated membership tests and common-element detection.

## Q5 – List comprehensions and sensor readings

A conditional list comprehension has the form [expression for item in iterable if condition]. A comprehension is concise for a simple transformation or filter; a normal loop can be clearer for complex branches or side effects.

A list comprehension creates and stores all results (O(n) memory). A generator expression produces values lazily (typically O(1) auxiliary memory, excluding the source), while both take O(n) time to consume. Measuring the generator object alone does not measure all memory eventually consumed.

The program compared a loop, comprehension, and map/filter implementation. All three produced identical results.

**Recorded benchmark results**

| n | Loop (s) | Comprehension (s) | map/filter (s) | Identical |
|---:|---:|---:|---:|---|
| 10,000 | 0.002876 | 0.001887 | 0.002369 | Yes |
| 100,000 | 0.015557 | 0.027393 | 0.037775 | Yes |
| 1,000,000 | 0.152413 | 0.142977 | 0.226243 | Yes |

The measured list-comprehension object size was 120 bytes and the generator object size was 208 bytes. This is not a direct comparison of total memory usage: the generator size excludes its source and values produced later.

## Q6 – Nested railway timetable and station index

The outer dictionary maps train number to train details. Each detail dictionary stores the train name, a list of stops, and a set of running days. Each stop is a tuple containing station, arrival, and departure. A station index maps station names to candidate trains and makes repeated station queries faster.

A query without an index scans train records and their stops. The index uses additional memory but reduces search work for stations served by only a subset of trains. The third stop's departure for a train is accessed using timetable[train_no]["stops"][2][2].

**Verified example results**
- Katpadi on Monday: 12601 Chennai Express, 12602 Bengaluru Mail, and 12605 West Coast Express.
- Unknown station Atlantis: empty result.
- Third stop departure of train 12601: 10:05.

**Recorded generated-data benchmark**

| Trains | Scan (s) | Indexed (s) | Same |
|---:|---:|---:|---|
| 100 | 0.000046 | 0.000024 | Yes |
| 1,000 | 0.000527 | 0.000198 | Yes |
| 10,000 | 0.004056 | 0.002821 | Yes |

The indexed search was faster in all three reported runs.

## Q7 – Contact merging

The program uses normalised phone numbers as dictionary keys. It removes non-digits and strips a leading country code 91 for Indian 10-digit mobile numbers. Each grouped contact stores original phone formats and email addresses in sets, together with a display name. Contacts with no usable phone number are kept separately because the selected matching rule cannot safely identify them.

**Algorithm**
1. For each contact, normalise each phone number.
2. If at least one normalised number exists, use each number as a key and merge the contact's numbers and emails into the matching group.
3. If there is no usable number, preserve it as an unmatched record rather than guessing identity from name alone.
4. Merge groups that share a normalised number.
5. Sort and display the merged contacts.

**Verified example results**
- Anu's two phone formats were merged into one contact.
- Dr. Ravi and ravi kumar were merged into one contact with three original phone formats and two email addresses.
- No phone contact and Missing fields were retained separately.
- 1,000 generated contacts produced 500 groups.
- 100,000 generated contacts produced 50,000 groups.

**Recorded benchmark results**

| Contacts | Dictionary merge (s) | Output groups |
|---:|---:|---:|
| 1,000 | 0.006032 | 500 |
| 100,000 | 0.596314 | 50,000 |

Dictionary grouping is efficient on average. Changed or missing phone numbers can prevent the same person from being recognised; a shared or recycled phone number can also cause a false merge. Real contact merging should ask for confirmation in ambiguous cases.

## Final conclusion

Python data structures should be selected according to the operations required: lists for ordered mutable sequences, tuples for fixed records, dictionaries for key-based lookup, and sets for unique membership and set algebra. The assignment demonstrated how data-structure choices affect clarity, execution time, and memory use. All benchmark values above are the values reported from the student's runs and may vary on other systems.
