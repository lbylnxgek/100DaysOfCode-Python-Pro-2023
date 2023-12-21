# Print greeting.
print("Welcome to the tip calculator.")

# Get the total bill as float via input.
bill = float(input("What was the total bill? $"))

# Get tip percentage as int via input.
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get number of diners as int via input.
num_diners = int(input("How many people will split the bill? "))

# Calculate tip amount.
tip_amount = bill * (tip_percent / 100)

# Calculate total bill.
bill_with_tip = bill + tip_amount

# Calculate amount per diner, rounded to two decimal places.
amount_per_diner = round(bill_with_tip / num_diners, 2)

# Print how much each diner should pay.
# Apply additional formatting in case the result is only one decimal place.
# Note: Python 3.x f-string/template-string formatting.
print(f"Each person should pay: ${amount_per_diner:.2f}")
