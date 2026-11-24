
import math
from decimal import Decimal

# TASK 4 - WRITE CORRECT EXPRESSIONS

# Milk details
quantity = Decimal("10.0")
fat = 4.2
snf = 8.9

# 1. Calculate fat and SNF steps
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)

# 2. Calculate rate per litre
rate_per_litre = (
    Decimal("30.00")
    + Decimal(fat_steps) * Decimal("0.40")
    + Decimal(snf_steps) * Decimal("0.30")
)

# 3. Calculate total amount
amount = quantity * rate_per_litre

print("FAT:", fat)
print("SNF:", snf)
print("QUANTITY:", quantity)
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs.", rate_per_litre)
print("Total amount: Rs.", amount)

# Unexpected result 1 - Floating point precision
result1 = (4.2 - 3.5) / 0.1
print("\nSurprise 1:", result1)
print("Correct step count using round():", round(result1))

# Unexpected result 2 - Floating point comparison
result2 = 0.1 + 0.2 == 0.3
print("\nSurprise 2: 0.1 + 0.2 == 0.3:", result2)

# Unexpected result 3 - Exponentiation associativity
result3 = 2 ** 3 ** 2
print("\nSurprise 3: 2 ** 3 ** 2 =", result3)
print("It is evaluated as 2 ** (3 ** 2)")

# Additional surprise - Unary minus and exponentiation
print("\n-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# Difference between round(), int() and floor()
number = -2.7
print("\nNegative number:", number)
print("round():", round(number))
print("int():", int(number))
print("math.floor():", math.floor(number))

# Comparison chaining and Boolean operators
print("\nFat valid:", 2.0 <= fat <= 7.0)
print("Both conditions:", fat >= 3.5 and snf >= 8.5)
print("At least one condition:", fat >= 3.5 or snf >= 8.5)

# Alternative calculation: round(), int(), floor()
# SNF is kept at its baseline of 8.5%

for fat_value in [4.2, 3.1]:
    steps = (fat_value - 3.5) / 0.1

    round_steps = round(steps)
    int_steps = int(steps)
    floor_steps = math.floor(steps)

    round_rate = Decimal("30.00") + Decimal(round_steps) * Decimal("0.40")
    int_rate = Decimal("30.00") + Decimal(int_steps) * Decimal("0.40")
    floor_rate = Decimal("30.00") + Decimal(floor_steps) * Decimal("0.40")

    print("\nFat value:", fat_value)
    print("round steps:", round_steps, "Rate:", round_rate)
    print("int steps:", int_steps, "Rate:", int_rate)
    print("floor steps:", floor_steps, "Rate:", floor_rate)

# Time complexity: O(1)
# Space complexity: O(1)

