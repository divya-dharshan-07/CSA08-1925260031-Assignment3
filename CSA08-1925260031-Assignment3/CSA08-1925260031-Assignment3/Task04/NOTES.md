# Q4 – Sets

The completed operator solution is `both = A & B`, `exactly_one = A ^ B`, and `neither = universe - (A | B)`. The equivalent methods are `intersection`, `symmetric_difference`, `union`, and `difference`.

Venn diagrams: intersection is the overlap; symmetric difference is the two non-overlap regions; union is all parts inside either circle; neither is outside both circles but within the universe.

Sets automatically discard duplicates. Membership is average O(1) in a set and O(n) in a list. A list cannot be a set element because it is mutable/unhashable; a tuple can be used if all its members are hashable.

Convert a list to a set for deduplication and repeated membership tests. This loses duplicates and original positional order. Nested loops cost O(n×m); sorting both lists then merging costs O(n log n + m log m); set intersection is O(n+m) average. Set storage is O(n+m); sorting/merge may need additional storage depending on implementation.
