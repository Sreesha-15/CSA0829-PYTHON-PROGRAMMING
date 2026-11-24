
from decimal import Decimal

# TASK 8 - TEN DAY MILK PAYMENT ALGORITHM

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def calculate_payment(quantity, fat, snf):
    """Calculate the rate and payment for one milk entry."""

    fat_steps = round(float((fat - Decimal("3.5")) / Decimal("0.1")))
    snf_steps = round(float((snf - Decimal("8.5")) / Decimal("0.1")))

    rate = (
        BASE_RATE
        + Decimal(fat_steps) * FAT_STEP_VALUE
        + Decimal(snf_steps) * SNF_STEP_VALUE
    )

    amount = (quantity * rate).quantize(Decimal("0.01"))

    return fat_steps, snf_steps, rate, amount


def main():
    """Read milk entries and calculate the ten-day payment total."""

    total = Decimal("0.00")

    try:
        n = int(input("Enter number of entries: "))

        if n <= 0:
            print("Number of entries must be positive.")
            return

        for i in range(1, n + 1):
            print(f"\nEntry {i}")

            while True:
                try:
                    quantity = Decimal(input("Enter quantity: ").strip())
                    fat = Decimal(input("Enter fat percentage: ").strip())
                    snf = Decimal(input("Enter SNF percentage: ").strip())

                    if not quantity.is_finite() or not fat.is_finite() or not snf.is_finite():
                        raise ValueError

                    if quantity <= 0 or not (0 <= fat <= 100) or not (0 <= snf <= 100):
                        raise ValueError

                    break

                except Exception:
                    print("Invalid entry. Please enter valid positive quantity and percentages from 0 to 100.")

            fat_steps, snf_steps, rate, amount = calculate_payment(
                quantity, fat, snf
            )

            total += amount

            print("Fat steps:", fat_steps)
            print("SNF steps:", snf_steps)
            print(f"Rate per litre: Rs. {rate:.2f}")
            print(f"Payment: Rs. {amount:.2f}")

        print("\nTEN-DAY PAYMENT SUMMARY")
        print(f"Total payment: Rs. {total:.2f}")

    except ValueError:
        print("Please enter a valid number of entries.")


if __name__ == "__main__":
    main()
