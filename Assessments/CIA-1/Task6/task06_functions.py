
from decimal import Decimal

# Global constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_RATE = Decimal("0.40")
SNF_STEP_RATE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")


def rate_per_litre(fat, snf):
    """Calculate and return the milk rate per litre using fat and SNF."""
    fat_steps = round((fat - STANDARD_FAT) / STEP_SIZE)
    snf_steps = round((snf - STANDARD_SNF) / STEP_SIZE)

    rate = (
        BASE_RATE
        + Decimal(fat_steps) * FAT_STEP_RATE
        + Decimal(snf_steps) * SNF_STEP_RATE
    )

    return rate


def payout(quantity, fat, snf):
    """Calculate and return the total payment for one farmer."""
    rate = rate_per_litre(fat, snf)
    amount = quantity * rate
    return amount.quantize(Decimal("0.01"))


def ten_day_total(payments):
    """Calculate and return the total payment for a ten-day period."""
    total = sum(payments, Decimal("0.00"))
    return total.quantize(Decimal("0.01"))


def main():
    """Demonstrate the milk payment functions with sample entries."""

    # Sample farmer entries: quantity, fat, SNF
    farmers = [
        (Decimal("10"), Decimal("4.2"), Decimal("8.9")),
        (Decimal("20"), Decimal("3.1"), Decimal("8.5")),
        (Decimal("15"), Decimal("3.5"), Decimal("8.5"))
    ]

    payments = []

    for quantity, fat, snf in farmers:
        rate = rate_per_litre(fat, snf)
        amount = payout(quantity, fat, snf)

        payments.append(amount)

        print(f"Quantity: {quantity:6.2f} litres")
        print(f"Fat:      {fat:6.2f}%")
        print(f"SNF:      {snf:6.2f}%")
        print(f"Rate: Rs. {rate:7.2f}")
        print(f"Payment: Rs. {amount:7.2f}")
        print()

    total = ten_day_total(payments)
    print(f"Ten-day total: Rs. {total:.2f}")


if __name__ == "__main__":
    main()
