
# TASK 3 - Variables and Constants

# 1. Valid variable names
student_name = "Arun"
total_amount = 500
payment_count = 10

print("Student Name:", student_name)
print("Total Amount:", total_amount)
print("Payment Count:", payment_count)


# 2. Constants in Python
TAX_RATE = 0.05
MAX_PAYMENTS = 100

print("Tax Rate:", TAX_RATE)
print("Maximum Payments:", MAX_PAYMENTS)


# 3. Dynamic typing
value = 100
print("Value:", value)
print("Type:", type(value))

value = "Python"
print("Value:", value)
print("Type:", type(value))


# 4. Multiple assignment
a, b = 10, 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# 5. Dictionary instead of magic numbers
RATE_CARD = {
    "basic": 100,
    "premium": 200,
    "deluxe": 300
}

plan = "premium"
print("Selected Plan:", plan)
print("Plan Rate:", RATE_CARD[plan])
