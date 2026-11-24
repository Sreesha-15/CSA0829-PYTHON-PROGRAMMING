
import random
import string
import time
import re


# Normalise phone numbers
def normalise_phone(phone):
    if not phone:
        return ""

    digits = "".join(
        character
        for character in phone
        if character.isdigit()
    )

    # Remove India's country code
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits


# Normalise names
def normalise_name(name):
    if not name:
        return ""

    name = name.strip().lower()

    name = re.sub(r"^(dr\.?|mr\.?|mrs\.?|ms\.?)\s+", "", name)

    return " ".join(name.split())


# Normalise email addresses
def normalise_email(email):
    if not email:
        return ""

    return email.strip().lower()


# Merge contacts using dictionary
def merge_contacts(contacts):
    merged = {}
    phone_index = {}

    for contact in contacts:

        name = contact.get("name", "").strip()

        phones = {
            normalise_phone(phone)
            for phone in contact.get("phones", [])
            if normalise_phone(phone)
        }

        emails = {
            normalise_email(email)
            for email in contact.get("emails", [])
            if normalise_email(email)
        }

        # Find an existing contact through shared phone numbers
        existing_ids = {
            phone_index[phone]
            for phone in phones
            if phone in phone_index
        }

        if existing_ids:
            # Choose one existing contact
            contact_id = min(existing_ids)

            # Merge any other matching contact groups
            for other_id in sorted(existing_ids):
                if other_id == contact_id:
                    continue

                merged[contact_id]["phones"].update(
                    merged[other_id]["phones"]
                )

                merged[contact_id]["emails"].update(
                    merged[other_id]["emails"]
                )

                del merged[other_id]

                for phone in merged[contact_id]["phones"]:
                    phone_index[phone] = contact_id

        else:
            contact_id = len(merged) + 1

            merged[contact_id] = {
                "name": name,
                "normalised_name": normalise_name(name),
                "phones": set(),
                "emails": set()
            }

        merged[contact_id]["phones"].update(phones)
        merged[contact_id]["emails"].update(emails)

        # Preserve the first available display name
        if not merged[contact_id]["name"] and name:
            merged[contact_id]["name"] = name

        for phone in merged[contact_id]["phones"]:
            phone_index[phone] = contact_id

    return list(merged.values())


# Sample contacts
contacts = [
    {
        "name": "Dr. Ravi",
        "phones": ["+91 98400 12345"],
        "emails": ["RAVI@GMAIL.COM"]
    },

    {
        "name": "Ravi Kumar",
        "phones": ["9840012345", "9876543210"],
        "emails": ["ravi@gmail.com", "ravi.work@gmail.com"]
    },

    {
        "name": "Priya",
        "phones": ["+91-90000-11111"],
        "emails": ["priya@gmail.com"]
    },

    {
        "name": "Priya",
        "phones": ["9000011111"],
        "emails": ["PRIYA@GMAIL.COM"]
    },

    {
        "name": "Arun",
        "phones": [],
        "emails": ["arun@gmail.com"]
    },

    {
        "name": "Arun",
        "phones": [],
        "emails": []
    }
]


# Display normalisation
print("PHONE NORMALISATION")

for phone in [
    "+91 98400 12345",
    "9840012345",
    "+91-90000-11111"
]:
    print(phone, "->", normalise_phone(phone))


# Merge contacts
print("\nMERGED CONTACTS")

result = merge_contacts(contacts)

for contact in result:
    print("\nName:", contact["name"])
    print("Normalised name:", contact["normalised_name"])
    print("Phones:", sorted(contact["phones"]))
    print("Emails:", sorted(contact["emails"]))


print("\nSUMMARY")
print("Original contacts:", len(contacts))
print("Merged contacts:", len(result))


# Hand verification
print("\nHAND VERIFICATION")

print("Expected Ravi phone count:", 2)
print("Actual Ravi phone count:", len(result[0]["phones"]))


# Generate large test datasets
def generate_contacts(count):
    data = []

    for i in range(count):

        # Every two records share one phone number
        number = str(9000000000 + i // 2)

        data.append({
            "name": f"Person {i}",
            "phones": [number],
            "emails": [f"user{i}@example.com"]
        })

    return data


# Pairwise comparison method
def pairwise_duplicate_count(data):
    count = 0

    normalised = [
        normalise_phone(contact["phones"][0])
        if contact["phones"] else ""
        for contact in data
    ]

    for i in range(len(normalised)):
        for j in range(i + 1, len(normalised)):

            if normalised[i] and normalised[i] == normalised[j]:
                count += 1

    return count


# Performance comparison
print("\nPERFORMANCE COMPARISON")
print("Contacts       Dictionary Merge       Pairwise Comparison")

for size in [1000, 100000]:

    data = generate_contacts(size)

    start = time.perf_counter()
    merged_data = merge_contacts(data)
    dictionary_time = time.perf_counter() - start

    print(
        f"{size:<15}"
        f"{dictionary_time:.6f} s"
        ,
        end=""
    )

    # Pairwise comparison is expensive.
    # Use 1000 for the full pairwise experiment.
    if size == 1000:

        start = time.perf_counter()
        duplicate_count = pairwise_duplicate_count(data)
        pairwise_time = time.perf_counter() - start

        print(f"       {pairwise_time:.6f} s")
        print("Duplicate pairs:", duplicate_count)

    else:
        print("       Not executed for 100000 records")


# Missing field testing
print("\nMISSING FIELD TEST")

missing_contacts = [
    {
        "name": "Kumar",
        "phones": [],
        "emails": []
    },
    {
        "name": "Meena",
        "phones": ["9000012345"],
        "emails": []
    }
]

print(merge_contacts(missing_contacts))
