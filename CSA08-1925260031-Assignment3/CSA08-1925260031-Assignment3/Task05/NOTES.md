# Q5 – List Comprehensions

General form: `[expression for item in iterable if condition]`. A comprehension is compact for a simple transformation/filter. Prefer a loop when logic has many branches, side effects, or complex exception handling.

Dictionary comprehension: `{minute: c for minute, c in enumerate(readings) if -50 <= c <= 50}`. Set comprehension: `{c for c in readings if -50 <= c <= 50}`.

A list comprehension eagerly creates a list and uses O(n) result memory. A generator expression is lazy and usually uses O(1) auxiliary memory, excluding its source; consuming either takes O(n) time. `sys.getsizeof(generator)` measures only the generator object, not the complete memory footprint of the data it will produce.

The alarm list reports valid sensor readings outside the safe 2–8 °C band; sensor errors outside −50 to 50 °C are excluded. No one implementation is always best: comprehensions are readable and often fast, loops can be clearest for complex logic, and generators are best when streaming or avoiding a full result list.
