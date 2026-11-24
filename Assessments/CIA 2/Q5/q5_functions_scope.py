
# Q5 - Functions, Parameters and Scope


# Buggy function: default list is shared
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# Correct function
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("Buggy function:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print("\nCorrect function:")
print(add_item("Tea"))
print(add_item("Vada"))


# Three independent customers
customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print("\nThree customers:")
print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# Positional, keyword and default arguments
def customer_details(name, item="Tea"):
    print("Customer:", name, "| Item:", item)


print("\nParameter examples:")
customer_details("Arun")
customer_details("Bala", "Coffee")
customer_details(item="Juice", name="Chitra")


# Returning more than one value
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


total, gst = calculate_bill(1000)

print("\nBill:")
print("Total:", total)
print("GST:", gst)


# Local and global scope
college = "SIMATS"


def show_college():
    local_message = "Welcome"
    print(local_message)
    print(college)


show_college()


# Global keyword demonstration
count = 10


def change_global():
    global count
    count = count + 1


change_global()
print("\nGlobal count:", count)


# Nonlocal keyword demonstration
def outer():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Hello Python"

    inner()
    print("Nonlocal value:", message)


outer()


# Inspect the buggy function's default value
print("\nBuggy function default:")
print(add_item_buggy.__defaults__)
