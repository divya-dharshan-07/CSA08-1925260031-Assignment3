# Q1 – Lists and Slicing

**Pseudocode:** Check at least 7 values; sum the first 7; output average; slide one position at a time by subtracting the outgoing reading and adding the incoming reading.

- `readings[7:14]`: elements at indices 7–13.
- `readings[-7:]`: last seven elements.
- `readings[::7]`: every seventh element starting at index 0.
- `append`: amortized O(1); `insert`/front or middle `pop`: O(n); `sort`: O(n log n).
- Naive: up to 7 additions per window, about `7(n-6)` = O(n). Running sum: 7 initial additions plus two arithmetic updates for each later window = O(n).
- Late insertion into a list is O(n). A deque is useful for a rolling window; a date dictionary is useful for date lookup but needs ordering for sequential processing.
- Window deque space O(7)=O(1); all stored readings O(n). A dictionary keyed by date also stores O(n) readings.
- Run `python Task01/rainfall.py` and record your own timings.
