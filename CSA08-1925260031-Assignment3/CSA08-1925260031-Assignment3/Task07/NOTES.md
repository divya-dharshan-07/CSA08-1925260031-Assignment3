# Q7 – Contact Merging

**Inputs:** contact records containing a name, zero or more phone numbers, and zero or more email addresses.  
**Output:** merged contact records with unique phone and email values.  
**Matching rule:** records are the same contact when they share a normalised phone number. Names are display labels, not identity keys.

Phone normalisation removes spaces/punctuation and strips a leading Indian country code `91` from a 12-digit number. Names are lowercased and punctuation is removed for sorting/display consistency. The dictionary maps each normalised number to a shared contact group; sets prevent duplicate phone/email values. Records with no usable number are preserved separately rather than merged based on a potentially shared name.

**Pseudocode**
1. For each contact, normalise each phone number.
2. If there are no valid phone keys, preserve it as unmatched.
3. Find groups already indexed by any normalised phone key.
4. If groups exist, merge their number/email sets; otherwise create a new group.
5. Add this record's numbers and emails and map all its phone keys to the group.
6. Remove duplicate group references and output sorted records.

Dictionary grouping is O(n) average in the number of contacts, plus the total number of phone/email fields. Comparing every pair is O(n²). For n=1,000 and n=100,000, run the benchmark and record your own timings. Two people with the same name but different phone numbers remain separate. Limitation: changed/missing numbers can prevent a match, and a recycled/shared number can cause a false merge. Ambiguous merges should be confirmed by a person.
