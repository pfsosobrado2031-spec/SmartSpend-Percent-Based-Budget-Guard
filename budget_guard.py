"""
Project Title: SmartSpend Budget Guard
Group Members: Sosobrado, Viray, Abasolo
Description: This program tracks spending across multiple categories and provides a summary of budget health.
"""

def GetValidAmount():
    # Input Validation
    amount = float(input("    Enter amount spent: "))
    while amount < 0:
        print("    Error: Amount cannot be negative.")
        amount = float(input("    Enter amount spent: "))
    return amount
    
def ShowFinalFeedback(percent_used):
    # Selection Structure for Feedback
    print("\n--- FINAL BUDGET REPORT ---")
    if percent_used <= 50:
        print("Feedback: Excellent management! You saved half your budget.")
    elif percent_used <= 80:
        print("Feedback: Good, but you've used more than half of your budget.")
    elif percent_used <= 99:
        print("Feedback: Warning: You are almost out of budget!")
    else:
        print("Feedback: Alert: You have exceeded your budget limits!")

def Main():
    print("=== SMART-SPEND TRACKING SYSTEM ===")
    
    # Validation for Allowance
    allowance = float(input("Enter total allowance: "))
    while allowance <= 0:
        print("    Error: Allowance must be greater than zero.")
        allowance = float(input("Enter total allowance: "))

    # Validation for Budget
    budget = float(input("Enter target budget: "))
    while budget <= 0 or budget > allowance:
        if budget <= 0:
            print("    Error: Budget must be greater than zero.")
        else:
            print("    Error: Budget cannot exceed your allowance.")
        budget = float(input("Enter target budget: "))

    num_categories = int(input("How many categories? "))
    
    # Variables for determining which is the highest and low costing category
    total_spent = 0
    highest_amt = 0
    highest_name = ""
    lowest_amt = 999999999999999999999999999999999999999999999999999999999999999
    lowest_name = ""

    # Amount and percentage spent in category
    for i in range(num_categories):
        print("-" * 35)
        print("Category #", i + 1)
        name = input("    Name: ")
        spent = GetValidAmount()
        
        total_spent = total_spent + spent
        
        cat_percent = round((spent / budget) * 100, 2)
        print("    > This category uses", cat_percent, "% of your budget.")

        # Logic to update Highest/Lowest
        if spent > highest_amt:
            highest_amt = spent
            highest_name = name
        
        if spent < lowest_amt:
            lowest_amt = spent
            lowest_name = name

    # Final Summary
    remaining = allowance - total_spent
    total_percent = (total_spent / budget) * 100

    print("\n" + "=" * 35)
    print("TOTAL SPENT:    ", round(total_spent, 2))
    print("MONEY LEFT:     ", round(remaining, 2))
    print("HIGHEST ITEM:   ", highest_name, "(", highest_amt, ")")
    print("LOWEST ITEM:    ", lowest_name, "(", lowest_amt, ")")
    
    ShowFinalFeedback(total_percent)

Main()
