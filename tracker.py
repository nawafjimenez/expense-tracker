# Installment 2: Talking to the User
# Made by: Nawaf I. Jimenez

print("EXPENSE TRACKER")
print("Know where your money goes.")
print("=" * 26)
print("MAIN MENU")
print("[1] Add an expense       (coming soon)")
print("[2] View all expenses    (coming soon)")
print("[3] Show total spent     (coming soon)")
print("[4] Exit                 (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("SUMMARY")
print("-" * 40)
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Nawaf I. Jimenez | Installment 2")