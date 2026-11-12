
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
        key=lambda item: (normalize_name(item["name"]), item["phones"])
    )
