print("EXPENSE TRACKER")
print("Know where your money goes.")
print("=========================")
print("MAIN MENU")
print("[1] Add an expense")
print("(coming soon)")
print("[2] View all expenses")
print("(coming soon)")
print("[3] Show total spent")
print("(coming soon)")
print("[4] Exit")
print("(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

exp1_name = input("First expense? ")
exp1_amount = float(input("Amount? "))

if exp1_amount > 200:
    print("  are you sure?")
    print("  Huge expense")
elif exp1_amount > 100:
    print("  Big expense.")
elif exp1_amount > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

exp2_name = input("Second expense? ")
exp2_amount = float(input("Amount? "))

if exp2_amount > 200:
    print("  are you sure?")
    print("  Huge expense")
elif exp2_amount > 100:
    print("  Big expense.")
elif exp2_amount > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if exp1_amount > 100 and exp2_amount > 100:
    print("  slow down!")
    print("  Two big expenses in a row")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = exp1_amount + exp2_amount
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount
over_budget = grand_total > budget
left_amount = budget - grand_total
over_amount = grand_total - budget

print("SUMMARY")
print(f"{exp1_name}: | ${exp1_amount}")
print(f"{exp2_name}: | ${exp2_amount}")
print(f"Subtotal: | ${subtotal}")
print(f"Average: | ${average}")
print(f"Tax ({tax_rate}%): | ${tax_amount}")
print(f"Grand total: | ${grand_total}")

if over_budget:
    print(f"Over budget by ${over_amount}!")
elif grand_total > (0.9 * budget):
    print(f"Careful: only ${left_amount} left.")
else:
    print(f"Within budget. ${left_amount} left.")

print("Made by: Nawaf I. Jimenez | Installment 4")