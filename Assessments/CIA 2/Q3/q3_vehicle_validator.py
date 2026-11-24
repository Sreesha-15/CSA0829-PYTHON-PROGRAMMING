
# Q3 - Vehicle Registration Validator

def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    return text.upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    if not state.isalpha():
        return False

    if not district.isdigit():
        return False

    if len(series) not in (1, 2) or not series.isalpha():
        return False

    if not number.isdigit():
        return False

    return True


def format_number(reg):
    if not is_valid(reg):
        return "Invalid registration number"

    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


test_numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 CD 4567",
    "AP-39-BZ-1234"
]

for raw in test_numbers:
    reg = normalise(raw)
    result = "valid" if is_valid(reg) else "INVALID"
    print(f"{raw:15} -> {reg:11} {result}")

print("\nReceipt format:")
print(format_number(normalise("tn 09 ab 1234")))

# Demonstrate string slicing
sample9 = "TN09AB123"
sample10 = "TN09AB1234"

print("\n9-character number:")
print("Last four:", sample9[-4:])
print("Middle:", sample9[4:-4])

print("\n10-character number:")
print("Last four:", sample10[-4:])
print("Middle:", sample10[4:-4])
