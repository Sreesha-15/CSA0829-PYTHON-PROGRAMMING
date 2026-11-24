
from decimal import Decimal
import sys

# 1,000 payments of Rs 33.40 and three small adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    # TODO 1: Add amounts exactly using Decimal
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(amount)

    return total


print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))

print(
    0.1 + 0.2 == 0.3,
    Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
)


# Demonstrate Decimal(float(amount))
def total_decimal_from_float(items):
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(float(amount))

    return total


print("Decimal(float):", total_decimal_from_float(payments))


# Alternative 1: Integer paise
def total_paise(items):
    total = 0

    for amount in items:
        rupees, paise = amount.split(".")
        total += int(rupees) * 100 + int(paise)

    return total


print("Integer paise:", total_paise(payments), "paise")


# Alternative 2: Float with round()
def total_rounded_float(items):
    total = 0.0

    for amount in items:
        total = round(total + float(amount), 2)

    return total


print("Rounded float:", total_rounded_float(payments))


# Memory comparison
print("\nMEMORY COMPARISON")
print("Integer:", sys.getsizeof(0), "bytes")
print("Float:", sys.getsizeof(0.0), "bytes")
print("Decimal:", sys.getsizeof(Decimal("0.00")), "bytes")


# Complexity
print("\nCOMPLEXITY ANALYSIS")
print("Number of payments:", len(payments))
print("Time per addition: O(1), assuming fixed-size values")
print("Total time: O(n)")
