# Expense Tracker - Installment 5
# Made by: Nawaf I. Jimenez | Installment 5

print("EXPENSE TRACKER")
print("Know where your money goes.")
print("=========================")

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

while True:
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    
    choice = input("Choose 1-4:")
    
    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("  are you sure?")
            print("  Huge expense")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
            
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax_amount = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax_amount
        over_budget = grand_total > budget
        left_amount = budget - grand_total
        over_amount = grand_total - budget
        
        print("Expenses:")
        print(f" | {count}")
        print(f"Subtotal:\n | ${subtotal}")
        print(f"Tax ({tax_percent}%):\n | ${tax_amount}")
        print(f"Grand total:\n | ${grand_total}")
        
        if over_budget:
            print(f"Over budget by\n | ${over_amount}!")
        elif grand_total > (0.9 * budget):
            print(f"Careful: only\n | ${left_amount} left.")
        else:
            print(f"Within budget.\n | ${left_amount} left.")
            
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print(f"Made by: Nawaf I. Jimenez | Installment 5")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")