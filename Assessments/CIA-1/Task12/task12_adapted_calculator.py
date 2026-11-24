
from decimal import Decimal, ROUND_HALF_UP

# Original rate card
ORIGINAL_CARD = {
    "base_rate": Decimal("30.00"),
    "fat_step": Decimal("0.40"),
    "snf_step": Decimal("0.30"),
}

# April to June seasonal rate card
SEASONAL_CARD = {
    "base_rate": Decimal("32.00"),
    "fat_step": Decimal("0.45"),
    "snf_step": Decimal("0.30"),
}

STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")

BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")
CENT = Decimal("0.01")


def select_rate_card(month):
    """Select seasonal or original rate card using the month."""
    if month in (4, 5, 6):
        return SEASONAL_CARD
    return ORIGINAL_CARD


def validate_reading(quantity, fat, snf):
    """Validate analyser readings and milk quantity."""
    quantity = Decimal(str(quantity))
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if not all(x.is_finite() for x in (quantity, fat, snf)):
        raise ValueError("Inputs must be finite numbers.")

    if quantity <= 0:
        raise ValueError("Quantity must be positive.")

    if not Decimal("0") <= fat <= Decimal("10"):
        raise ValueError("Fat must be between 0 and 10.")

    if not Decimal("0") <= snf <= Decimal("100"):
        raise ValueError("SNF must be between 0 and 100.")

    return quantity, fat, snf


def calculate_steps(reading, standard):
    """Convert a two-decimal reading into 0.1% steps."""
    return ((reading - standard) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )


def calculate_rate(fat, snf, month):
    """Calculate rate using the selected rate card."""
    card = select_rate_card(month)

    fat_steps = calculate_steps(fat, STANDARD_FAT)
    snf_steps = calculate_steps(snf, STANDARD_SNF)

    rate = (
        card["base_rate"]
        + fat_steps * card["fat_step"]
        + snf_steps * card["snf_step"]
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def calculate_payment(quantity, fat, snf, month):
    """Calculate one farmer's payment before ten-day bonus."""
    quantity, fat, snf = validate_reading(quantity, fat, snf)

    rate = calculate_rate(fat, snf, month)
    payment = (quantity * rate).quantize(
        CENT, rounding=ROUND_HALF_UP
    )

    return rate, payment

def calculate_bonus(total_quantity):
    """Give a bonus only when ten-day supply exceeds 500 litres."""
    bonus = calculate_bonus(total_quantity)
        return (total_quantity * BONUS_PER_LITRE).quantize(
            CENT, rounding=ROUND_HALF_UP
        )
    return Decimal("0.00")

def calculate_ten_day_total(entries, month):
    """
    Calculate ten-day payment.
    Entries contain (quantity, fat, snf).
    Bonus applies when total quantity is greater than 500 litres.
    """
    total_quantity = Decimal("0")
    milk_payment = Decimal("0.00")

    for quantity, fat, snf in entries:
        quantity, fat, snf = validate_reading(quantity, fat, snf)

        rate = calculate_rate(fat, snf, month)
        payment = (quantity * rate).quantize(
            CENT, rounding=ROUND_HALF_UP
        )

        total_quantity += quantity
        milk_payment += payment

    if total_quantity > BONUS_THRESHOLD:
        bonus = (total_quantity * BONUS_PER_LITRE).quantize(
            CENT, rounding=ROUND_HALF_UP
        )
    else:
        bonus = Decimal("0.00")

    final_total = milk_payment + bonus

    return total_quantity, milk_payment, bonus, final_total


def run_tests():
    """Test both seasons, decimal readings and bonus conditions."""

    print("SEASONAL RATE TESTS")
    print("-" * 60)

    # Same analyser readings tested in both seasons
    readings = (Decimal("4.26"), Decimal("8.74"))

    regular_rate = calculate_rate(readings[0], readings[1], 3)
    seasonal_rate = calculate_rate(readings[0], readings[1], 4)

    print("Regular season rate expected: 33.80, actual:", regular_rate)
    print("Seasonal rate expected:       36.20, actual:", seasonal_rate)

    assert regular_rate == Decimal("33.80")
    assert seasonal_rate == Decimal("36.20")

    # Two-decimal rounding tests
    print("\nTWO-DECIMAL READING TESTS")
    rate_356 = calculate_rate(Decimal("3.56"), Decimal("8.54"), 4)
    rate_354 = calculate_rate(Decimal("3.54"), Decimal("8.56"), 4)

    print("Fat 3.56, SNF 8.54 expected 32.45, actual:", rate_356)
    print("Fat 3.54, SNF 8.56 expected 32.30, actual:", rate_354)

    assert rate_356 == Decimal("32.45")
    assert rate_354 == Decimal("32.30")

    # Exactly 500 litres: no bonus
    entries_500 = [
        ("250", "3.50", "8.50"),
        ("250", "3.50", "8.50"),
    ]

    q, milk, bonus, total = calculate_ten_day_total(entries_500, 4)

    print("\n500-LITRE BONUS TEST")
    print("Expected bonus: 0.00, actual:", bonus)
    print("Expected total: 16000.00, actual:", total)

    assert q == Decimal("500")
    assert bonus == Decimal("0.00")
    assert total == Decimal("16000.00")

    # More than 500 litres: bonus applies
    entries_501 = [
        ("250", "3.50", "8.50"),
        ("251", "3.50", "8.50"),
    ]

    q, milk, bonus, total = calculate_ten_day_total(entries_501, 4)

    print("\n501-LITRE BONUS TEST")
    print("Expected milk payment: 16032.00, actual:", milk)
    print("Expected bonus:         250.50, actual:", bonus)
    print("Expected final total:  16282.50, actual:", total)

    assert q == Decimal("501")
    assert milk == Decimal("16032.00")
    assert bonus == Decimal("250.50")
    assert total == Decimal("16282.50")

    print("\nALL TASK 12 TESTS PASSED!")


def main():
    run_tests()

    print("\nSAMPLE FARMER PAYMENT")
    rate, payment = calculate_payment("10", "4.26", "8.74", 4)

    print("Season: April-June")
    print("Quantity: 10 litres")
    print("Fat: 4.26%")
    print("SNF: 8.74%")
    print("Rate per litre: Rs.", rate)
    print("Payment before ten-day bonus: Rs.", payment)


if __name__ == "__main__":
    main()
