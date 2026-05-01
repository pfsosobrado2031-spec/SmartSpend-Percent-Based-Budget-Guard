"""
Project Title: SmartSpend Budget Guard
Group Members: Sosobrado, Viray, Abasolo
Description: This program tracks spending across multiple categories and provides a summary of budget health.
"""

def GetValidAmount():
    # Input Validation
    amount = float(input("    Enter amount spent: "))
    while amount < 0:
        print("    Error: Amount cannot be negative.")
        amount = float(input("    Enter amount spent: "))
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
        print("    Error: Allowance must be greater than zero.")
        allowance = float(input("Enter total allowance: "))

    # Validation for Budget
    budget = float(input("Enter target budget: "))
    while budget <= 0 or budget > allowance:
        if budget <= 0:
            print("    Error: Budget must be greater than zero.")
        else:
            print("    Error: Budget cannot exceed your allowance.")
        budget = float(input("Enter target budget: "))
