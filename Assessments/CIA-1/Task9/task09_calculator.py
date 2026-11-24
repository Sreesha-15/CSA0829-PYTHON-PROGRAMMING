
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# Standard values
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")

# Allowed input ranges
MIN_FAT = Decimal("0")
MAX_FAT = Decimal("10")
MIN_SNF = Decimal("0")
MAX_SNF = Decimal("100")


def validate_entry(quantity, fat, snf):
    """Convert inputs and check that all values are valid."""
    try:
        quantity = Decimal(str(quantity).strip())
        fat = Decimal(str(fat).strip())
        snf = Decimal(str(snf).strip())
    except (InvalidOperation, ValueError):
        raise ValueError("Please enter numeric values.")

    if not quantity.is_finite() or not fat.is_finite() or not snf.is_finite():
        raise ValueError("Values must be finite numbers.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 0 and 10.")

    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("SNF must be between 0 and 100.")

    return quantity, fat, snf


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )

    return rate.quantize(Decimal("0.01"))


def calculate_payment(quantity, fat, snf):
    """Validate an entry and calculate its payment."""
    quantity, fat, snf = validate_entry(quantity, fat, snf)

    rate = rate_per_litre(fat, snf)
    amount = (quantity * rate).quantize(Decimal("0.01"))

    return rate, amount


def run_tests():
    """Run automatic tests and display expected and actual results."""

    tests = [
        ("Fat above standard", ("10", "4.0", "8.5"), "32.00"),
        ("Fat below standard", ("10", "3.0", "8.5"), "28.00"),
        ("SNF above standard", ("10", "3.5", "8.7"), "30.60"),
        ("SNF below standard", ("10", "3.5", "8.3"), "29.40"),
        ("Standard boundary", ("10", "3.5", "8.5"), "30.00"),
        ("Lowest allowed fat", ("1", "0", "8.5"), "16.00"),
        ("Highest allowed fat", ("1", "10", "8.5"), "56.00"),
    ]

    print("\nCALCULATOR TEST RESULTS")
    print("-" * 68)
    print(f"{'Test case':25} {'Expected rate':18} {'Actual rate':18} Result")
    print("-" * 68)

    for name, inputs, expected in tests:
        actual_rate, actual_amount = calculate_payment(*inputs)
        result = "PASS" if actual_rate == Decimal(expected) else "FAIL"
        print(f"{name:25} {expected:18} {str(actual_rate):18} {result}")
        assert actual_rate == Decimal(expected), name

    # Invalid input tests
    invalid_tests = [
        ("Text input", ("abc", "3.5", "8.5")),
        ("Negative quantity", ("-5", "3.5", "8.5")),
        ("Fat below range", ("5", "-1", "8.5")),
        ("Fat above range", ("5", "11", "8.5")),
    ]

    print("\nINVALID INPUT TESTS")
    print("-" * 50)

    for name, inputs in invalid_tests:
        try:
            calculate_payment(*inputs)
            actual = "Accepted"
        except ValueError:
            actual = "Rejected"

        expected = "Rejected"
        result = "PASS" if actual == expected else "FAIL"
        print(f"{name:25} Expected: {expected:10} Actual: {actual:10} {result}")
        assert actual == expected, name

    # Five entries: calculate the total payment
    entries = [
        ("10", "3.5", "8.5"),
        ("8", "4.0", "8.7"),
        ("12", "3.0", "8.3"),
        ("5", "4.2", "8.5"),
        ("6", "3.5", "8.8"),
    ]

    expected_payments = [
        Decimal("300.00"),
        Decimal("251.20"),
        Decimal("328.80"),
        Decimal("164.00"),
        Decimal("185.40"),
    ]

    total = Decimal("0.00")

    print("\nFIVE-ENTRY TOTAL TEST")
    print("-" * 55)
    print(f"{'Entry':8} {'Quantity':10} {'Rate':10} {'Payment':10}")

    for index, entry in enumerate(entries):
        rate, amount = calculate_payment(*entry)
        total += amount
        print(
            f"{index + 1:<8} {entry[0]:<10} "
            f"{rate:<10} {amount:<10}"
        )
        assert amount == expected_payments[index]

    expected_total = Decimal("1229.40")
    print("-" * 55)
    print(f"Expected total: Rs. {expected_total}")
    print(f"Actual total:   Rs. {total}")
    assert total == expected_total

    print("\nALL TESTS PASSED!")


def main():
    """Run the calculator for user-entered milk details."""
    print("MILK PAYMENT CALCULATOR")

    try:
        quantity = input("Enter milk quantity in litres: ")
        fat = input("Enter fat percentage: ")
        snf = input("Enter SNF percentage: ")

        rate, amount = calculate_payment(quantity, fat, snf)

        print(f"\nRate per litre : Rs. {rate}")
        print(f"Total payment : Rs. {amount}")

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    run_tests()
    main()
