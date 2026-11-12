
"""Q7: Contact merging using normalised phone numbers as dictionary keys."""

import random
import re
import time


def normalize_phone(raw):
    """Keep digits; normalise Indian +91/91 numbers."""
    digits = re.sub(r"\D", "", raw or "")

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    if len(digits) == 10:
        return digits

    # Reject malformed lengths instead of treating them as valid match keys.
    return None


def normalize_name(name):
    """Normalise names for sorting."""
    return " ".join(re.findall(r"[a-z]+", (name or "").lower()))


def merge_contacts(contacts):
    """Merge records sharing at least one normalised phone number."""

    groups = {}
    no_phone = []

    for contact in contacts:
        name = (contact.get("name") or "").strip()
        phones = set(contact.get("phones") or [])

        emails = {
            email.strip().lower()
            for email in (contact.get("emails") or [])
            if email and email.strip()
        }

        keys = {normalize_phone(phone) for phone in phones}
        keys.discard(None)

        if not keys:
            no_phone.append({
                "name": name or "(Unnamed contact)",
                "phones": sorted(phones),
                "emails": sorted(emails),
                "match_status": "not merged: no usable phone",
            })
            continue

        # Find existing groups without putting dictionaries in a set.
        existing = []
        seen_groups = set()

        for key in keys:
            if key in groups:
                group = groups[key]

                if id(group) not in seen_groups:
                    existing.append(group)
                    seen_groups.add(id(group))

        if existing:
            target = existing[0]

            # Merge previously separate groups.
            for other in existing[1:]:
                target["phones"].update(other["phones"])
                target["emails"].update(other["emails"])

                if target["name"] == "(Unnamed contact)" and other["name"]:
                    target["name"] = other["name"]

                for old_key, value in list(groups.items()):
                    if value is other:
                        groups[old_key] = target

        else:
            target = {
                "name": name or "(Unnamed contact)",
                "phones": set(),
                "emails": set(),
            }

        target["phones"].update(phones)
        target["emails"].update(emails)

        if target["name"] == "(Unnamed contact)" and name:
            target["name"] = name

        for key in keys:
            groups[key] = target

    # Remove duplicate references to the same group.
    unique_groups = []
    seen_ids = set()

    for group in groups.values():
        if id(group) not in seen_ids:
            seen_ids.add(id(group))
            unique_groups.append(group)

    result = []

    for group in unique_groups:
        result.append({
            "name": group["name"],
            "phones": sorted(group["phones"]),
            "emails": sorted(group["emails"]),
        })

    result.extend(no_phone)

    return sorted(
        result,
        key=lambda item: (
            normalize_name(item["name"]),
            item["phones"]
        )
    )


def main():

    contacts = [
        {
            "name": "Dr. Ravi",
            "phones": ["+91 98400 12345"],
            "emails": ["RAVI@example.com"]
        },
        {
            "name": "ravi kumar",
            "phones": ["9840012345", "044-22223333"],
            "emails": ["ravi.work@example.com"]
        },
        {
            "name": "Anu",
            "phones": ["9876543210"],
            "emails": []
        },
        {
            "name": "Anu S",
            "phones": ["+91 98765 43210"],
            "emails": ["anu@example.com"]
        },
        {
            "name": "No phone contact",
            "phones": [],
            "emails": ["unknown@example.com"]
        },
        {
            "name": "Missing fields",
            "phones": [],
            "emails": []
        },
    ]

    print("Merged small example:")

    for item in merge_contacts(contacts):
        print(item)

    # Benchmark generated contact records.
    print("\nBenchmark (seconds; timings vary):")

    random.seed(42)

    for n in (1_000, 100_000):

        generated = []

        for i in range(n):
            number = str(9000000000 + (i // 2))

            generated.append({
                "name": f"Person {i}",
                "phones": [number],
                "emails": [f"person{i}@example.com"],
            })

        start = time.perf_counter()

        merged = merge_contacts(generated)

        elapsed = time.perf_counter() - start

        print(
            f"contacts={n:>6}: "
            f"dictionary merge={elapsed:.6f}s, "
            f"output groups={len(merged)}"
        )


# Program execution starts here.
if __name__ == "__main__":
    main()
