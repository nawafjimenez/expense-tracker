print("EXPENSE TRACKER")
print("Know where your money goes.")
print("=========================")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0.0

expense1_name = input("First expense? ")
expense1_amt = float(input("Amount? "))
subtotal += expense1_amt

expense2_name = input("Second expense? ")
expense2_amt = float(input("Amount? "))
subtotal += expense2_amt

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print("\nMAIN MENU")
print("[1] Add an expense (coming soon)")
print("[2] View all expenses (coming soon)")
print("[3] Show total spent (coming soon)")
print("[4] Exit (coming soon)")

print("\nSUMMARY")
print(f"{expense1_name}:\t${expense1_amt}")
print(f"{expense2_name}:\t${expense2_amt}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")

print("\nMade by: Nawaf Jimenez | Installment 3")