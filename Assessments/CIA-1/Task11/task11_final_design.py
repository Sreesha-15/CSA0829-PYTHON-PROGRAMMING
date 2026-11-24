
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from time import perf_counter


RATE_FILE = Path(__file__).with_name("rate_card.json")


def load_rate_card():
    """Read rate values from the JSON file."""
    start = perf_counter()

    with RATE_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    elapsed = perf_counter() - start

    # Convert decimal strings into Decimal values.
    for key, value in data.items():
        data[key] = Decimal(value)

    return data, elapsed


def calculate_rate(fat, snf, card):
    """Calculate rate per litre using the loaded rate card."""
    fat_steps = (
        (fat - card["standard_fat"]) / card["step_size"]
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    snf_steps = (
        (snf - card["standard_snf"]) / card["step_size"]
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = (
        card["base_rate"]
        + fat_steps * card["fat_step_value"]
        + snf_steps * card["snf_step_value"]
    )

    return rate.quantize(Decimal("0.01"))


def calculate_payment(quantity, fat, snf, card):
    """Validate inputs and calculate a rounded farmer payment."""
    quantity = Decimal(str(quantity))
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if not all(value.is_finite() for value in (quantity, fat, snf)):
        raise ValueError("Inputs must be finite numbers.")

    if quantity <= 0:
        raise ValueError("Quantity must be positive.")

    if not card["min_fat"] <= fat <= card["max_fat"]:
        raise ValueError("Fat is outside the allowed range.")

    if not card["min_snf"] <= snf <= card["max_snf"]:
        raise ValueError("SNF is outside the allowed range.")

    rate = calculate_rate(fat, snf, card)

    # Round each farmer's payment to the nearest paisa.
    amount = (quantity * rate).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    return rate, amount


def main():
    card, load_time = load_rate_card()

    print("CO-OPERATIVE MILK PAYMENT SYSTEM")
    print(f"Rate card loaded in {load_time:.8f} seconds")

    test_entries = [
        ("10", "3.5", "8.5"),
        ("8", "4.0", "8.7"),
        ("12", "3.0", "8.3"),
    ]

    total = Decimal("0.00")

    print("\nQUANTITY   FAT    SNF    RATE/LITRE   PAYMENT")

    for quantity, fat, snf in test_entries:
        rate, amount = calculate_payment(quantity, fat, snf, card)
        total += amount

        print(
            f"{quantity:8} {fat:6} {snf:6} "
            f"Rs.{rate:8} Rs.{amount:9}"
        )

    print("-----------------------------------------------")
    print(f"Total payment: Rs.{total}")

    # Verify the standard rate.
    assert calculate_rate(
        Decimal("3.5"), Decimal("8.5"), card
    ) == Decimal("30.00")

    print("Standard rate test: PASS")


if __name__ == "__main__":
    main()
