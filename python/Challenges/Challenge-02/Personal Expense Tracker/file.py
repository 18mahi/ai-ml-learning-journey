# expense tracker 

# Ask the user how many expenses they want to enter.
num_of_expenses = int(input("How many expenses do you want to add? "))

# For each expense, take:category and amount &  Store expense data using data structures (Use lists and dictionaries)
expenses = []
for _ in range(num_of_expenses):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"category": category, "amount": amount})
    
    
# Display all expenses entered by the user.
print(expenses)

#total amount of expenses
total_expenses = sum(expense["amount"] for expense in expenses)
print(f"Total expenses: {total_expenses}")

#highest expense
highest_expense = max(expenses, key=lambda x: x["amount"])
print(f"Highest expense: {highest_expense['category']} - {highest_expense['amount']}")

#LOWEST EXPENSE
lowest_expense = min(expenses, key=lambda x: x["amount"])
print(f"Lowest expense: {lowest_expense['category']} - {lowest_expense['amount']}")

#Show category-wise expense totals.
category_totals = {}  
for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
print("Category-wise expense totals:")
for category, total in category_totals.items():
    print(f"{category}: {total}")

# ask the user for budget amount
budget = float(input("Enter your budget amount: "))

# Compare total expenses with the budget and provide feedback to the user.
if total_expenses > budget:
    print("Warning: You crossed your budget!")
else:
    print("Great ! You are within your budget.")

