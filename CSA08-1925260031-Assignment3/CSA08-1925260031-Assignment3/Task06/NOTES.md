# Q6 – Nested Railway Timetable

The outer dictionary is keyed by train number. Each train's detail dictionary stores name, stops, and running days. Stops are a list because their order matters and the route may have many stops. Each stop is a tuple `(station, arrival, departure)` because it is a fixed record. Running days are a set for fast membership tests.

For train `t`, the departure time at its third stop is `timetable[t]["stops"][2][2]`.

Without an index, a query scans all train stops: O(total stops). A station index maps station → candidate train records; the query then checks only trains serving that station, O(trains at station) average plus day checks. The index adds O(total stop entries) memory and needs maintenance when timetable data changes. A flat list of tuples scanned for each query also costs O(total stops); it is simple but slower for repeated queries.
