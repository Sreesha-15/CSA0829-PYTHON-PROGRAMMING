
from decimal import Decimal

# TASK 5 - READ INPUT AND CONVERT TYPES

# Validate positive decimal numbers using string methods
def is_valid_number(text):
    text = text.strip()

    if text.count(".") > 1:
        return False

    return text.replace(".", "", 1).isdigit()


# Read and validate input
def get_number(prompt):
    while True:
        text = input(prompt)

        if is_valid_number(text):
            return Decimal(text.strip())

        print("Invalid input! Enter a valid number (example: 8.5).")


# Read clerk's entries
quantity = get_number("Enter milk quantity in litres: ")
fat = get_number("Enter fat percentage: ")
snf = get_number("Enter SNF percentage: ")

# Calculate fat and SNF steps
fat_steps = round((float(fat) - 3.5) / 0.1)
snf_steps = round((float(snf) - 8.5) / 0.1)

# Calculate rate and amount
rate = (
    Decimal("30.00")
    + Decimal(fat_steps) * Decimal("0.40")
    + Decimal(snf_steps) * Decimal("0.30")
)

amount = quantity * rate

# Display aligned output using f-strings
print("\n------ MILK PAYMENT DETAILS ------")
print(f"Quantity       : {quantity:8.2f} litres")
print(f"Fat            : {fat:8.2f}%")
print(f"SNF            : {snf:8.2f}%")
print(f"Fat steps      : {fat_steps:8d}")
print(f"SNF steps      : {snf_steps:8d}")
print(f"Rate per litre : Rs. {rate:8.2f}")
print(f"Total amount   : Rs. {amount:8.2f}")
