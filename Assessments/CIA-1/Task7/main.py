
# Import the module using an alias
import milkrate as mr

print("Using imported milkrate module")

# Call functions from the imported module
rate = mr.rate_per_litre(4.2, 8.7)
amount = mr.payout(8.5, 4.2, 8.7)

print("Rate per litre:", rate)
print("Farmer payment:", amount)

# Demonstrate other import styles
from milkrate import payout

print("Payment using direct import:", payout(10, 3.5, 8.5))
