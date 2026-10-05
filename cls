[1mdiff --git a/tracker.py b/tracker.py[m
[1mindex 90ada1e..2f5527a 100644[m
[1m--- a/tracker.py[m
[1m+++ b/tracker.py[m
[36m@@ -1,20 +1,34 @@[m
[31m-# Project: Expense Tracker - Installment 1[m
[31m-# Author: Nawaf I. Jimenez[m
[31m-# Description: A landing page for a personal expense tracker application.[m
[32m+[m[32m# Installment 2: Talking to the User[m
[32m+[m[32m# Made by: Nawaf I. Jimenez[m
 [m
[31m-print("=" * 40)[m
[31m-print("\tEXPENSE TRACKER")[m
[31m-print("\tKnow where your money goes.")[m
[31m-print("=" * 40)[m
[32m+[m[32mprint("EXPENSE TRACKER")[m
[32m+[m[32mprint("Know where your money goes.")[m
[32m+[m[32mprint("=" * 26)[m
[32m+[m[32mprint("MAIN MENU")[m
[32m+[m[32mprint("[1] Add an expense       (coming soon)")[m
[32m+[m[32mprint("[2] View all expenses    (coming soon)")[m
[32m+[m[32mprint("[3] Show total spent     (coming soon)")[m
[32m+[m[32mprint("[4] Exit                 (coming soon)")[m
[32m+[m[32mprint()[m
 [m
[31m-print("\nWelcome! This is your personal expense tracker.\n")[m
[32m+[m[32mname = input("What's your name? ")[m
[32m+[m[32mprint(f"Welcome, {name}! Let's log two expenses.")[m
 [m
[31m-print("MAIN MENU")[m
[31m-print("[1] Add an expense\t(coming soon)")[m
[31m-print("[2] View all expenses\t(coming soon)")[m
[31m-print("[3] Show total spent\t(coming soon)")[m
[31m-print("[4] Exit\t\t(coming soon)")[m
[32m+[m[32mitem1 = input("First expense? ")[m
[32m+[m[32mamount1 = float(input("Amount? "))[m
[32m+[m
[32m+[m[32mitem2 = input("Second expense? ")[m
[32m+[m[32mamount2 = float(input("Amount? "))[m
 [m
[32m+[m[32mtotal = amount1 + amount2[m
[32m+[m[32maverage = total / 2[m
[32m+[m
[32m+[m[32mprint()[m
[32m+[m[32mprint("SUMMARY")[m
[32m+[m[32mprint("-" * 40)[m
[32m+[m[32mprint(f"{item1}:\t\t${amount1}")[m
[32m+[m[32mprint(f"{item2}:\t\t${amount2}")[m
[32m+[m[32mprint(f"Total spent:\t${total}")[m
[32m+[m[32mprint(f"Average:\t${average}")[m
 print("-" * 40)[m
[31m-print("Made by: Nawaf Ibay Jimenez | Installment 1")[m
[31m-print("=" * 40)[m
\ No newline at end of file[m
[32m+[m[32mprint("Made by: Nawaf I. Jimenez | Installment 2")[m
\ No newline at end of file[m
