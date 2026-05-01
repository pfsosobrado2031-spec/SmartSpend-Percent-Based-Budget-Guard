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
