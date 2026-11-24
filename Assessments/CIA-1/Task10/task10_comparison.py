
from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter
from statistics import median

# Milk rate constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")
STEP_SIZE = Decimal("0.1")

CENT = Decimal("0.01")

# Five sample entries: quantity, fat, SNF
SAMPLE_ENTRIES = [
    (Decimal("10.005"), Decimal("3.5"), Decimal("8.5")),
    (Decimal("8.555"), Decimal("4.0"), Decimal("8.7")),
    (Decimal("12.125"), Decimal("3.0"), Decimal("8.3")),
    (Decimal("5.555"), Decimal("4.2"), Decimal("8.5")),
    (Decimal("6.666"), Decimal("3.5"), Decimal("8.8")),
]


def round_money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def decimal_rate(fat, snf):
    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    return BASE_RATE + fat_steps * FAT_STEP + snf_steps * SNF_STEP


def float_rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return 30.0 + fat_steps * 0.40 + snf_steps * 0.30


def make_entries(count):
    return [
        SAMPLE_ENTRIES[i % len(SAMPLE_ENTRIES)]
        for i in range(count)
    ]


def calculate_float_total(entries):
    total = 0.0
    for quantity, fat, snf in entries:
        rate = float_rate(float(fat), float(snf))
        total += float(quantity) * rate
    return total


def calculate_decimal_total(entries):
    total = Decimal("0")
    for quantity, fat, snf in entries:
        rate = decimal_rate(fat, snf)
        total += quantity * rate
    return total


def calculate_rounded_payment_total(entries):
    total = Decimal("0")
    for quantity, fat, snf in entries:
        rate = decimal_rate(fat, snf)
        payment = round_money(quantity * rate)
        total += payment
    return total


def calculate_rate_table(entries):
    # Calculate each distinct (fat, snf) rate only once.
    rate_table = {}

    for _, fat, snf in entries:
        key = (fat, snf)
        if key not in rate_table:
            rate_table[key] = decimal_rate(fat, snf)

    total = Decimal("0")
    for quantity, fat, snf in entries:
        total += quantity * rate_table[(fat, snf)]

    return total, rate_table


def measure_time(function, entries, repeats=5):
    times = []

    for _ in range(repeats):
        start = perf_counter()
        function(entries)
        end = perf_counter()
        times.append(end - start)

    return median(times)


def main():
    print("FLOAT AND DECIMAL COMPARISON")
    print("=" * 75)

    for count in [300, 6000, 150000]:
        entries = make_entries(count)

        float_time = measure_time(calculate_float_total, entries)
        decimal_time = measure_time(calculate_decimal_total, entries)

        float_total = calculate_float_total(entries)
        decimal_total = calculate_decimal_total(entries)

        difference = abs(Decimal(str(float_total)) - decimal_total)

        print(f"\nNumber of payments: {count}")
        print(f"Float total       : {float_total:.6f}")
        print(f"Decimal total     : {decimal_total}")
        print(f"Absolute difference: {difference}")
        print(f"Float time        : {float_time:.6f} seconds")
        print(f"Decimal time      : {decimal_time:.6f} seconds")

    # Compare rounding methods
    entries = make_entries(5)

    raw_total = calculate_decimal_total(entries)
    round_total_only = round_money(raw_total)
    round_each_payment = calculate_rounded_payment_total(entries)

    print("\nROUNDING COMPARISON FOR FIVE PAYMENTS")
    print("=" * 55)
    print(f"Raw total before rounding : {raw_total}")
    print(f"Round only final total    : {round_total_only}")
    print(f"Round each payment first  : {round_each_payment}")

    # Compare recalculation and dictionary lookup
    entries = make_entries(150000)

    normal_time = measure_time(calculate_decimal_total, entries)
    table_time = measure_time(calculate_rate_table, entries)

    table_total, rate_table = calculate_rate_table(entries)

    print("\nRATE TABLE PERFORMANCE")
    print("=" * 55)
    print(f"Number of payments       : {len(entries)}")
    print(f"Different fat-SNF pairs  : {len(rate_table)}")
    print(f"Normal calculation time  : {normal_time:.6f} seconds")
    print(f"Rate table time          : {table_time:.6f} seconds")
    print(f"Normal total             : {calculate_decimal_total(entries)}")
    print(f"Rate table total         : {table_total}")

    assert table_total == calculate_decimal_total(entries)
    print("\nRATE TABLE CHECK: PASS")
    print("COMPARISON COMPLETED")


if __name__ == "__main__":
    main()
