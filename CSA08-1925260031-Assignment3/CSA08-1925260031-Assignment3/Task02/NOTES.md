# Q2 – Tuples, Mutability and Copying

Tuples are immutable and hashable if every contained element is hashable; therefore coordinate tuples can be dictionary keys. Lists are mutable and unhashable, so a list key raises `TypeError`.

Bad-grid memory picture: `bad[0]`, `bad[1]`, and `bad[2]` all point to the same inner list `[0, 0, 0, 0]`. Correct-grid picture: three different row objects each initially contain four zero values.

Aliasing assigns another name to the same object. Shallow copy (`copy.copy` or slicing) creates a new outer container but shares nested objects. Deep copy recursively copies nested objects. A shallow copy is enough for flat immutable elements; deep copy is useful when nested mutable elements must be independent.

A function receives a reference to the same list object, so mutating it changes what the caller sees. A tuple cannot have its element reassigned, but a list contained inside it can still mutate.

Dense grid: O(rows×cols) memory. Sparse dictionary keyed by `(row, col)`: average O(1) lookup and O(k) memory for k non-empty cells; missing cells are interpreted as zero. Both have average O(1) access. `sys.getsizeof` reports shallow container size, not the recursively total memory of contained integers.
