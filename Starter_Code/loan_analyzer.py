# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.
Automate the calculations for the loan portfolio summaries.
"""
loan_costs = [500, 600, 200, 1000, 450]


# Using the `len` function to calculate the total number of loans in the list.

number_of_loans = len(loan_costs)
print(f"The total number of loans are: ", number_of_loans)


# Using the `sum` function to calculate the total of all loans in the list.

value_of_loans = sum(loan_costs)
print(f"The total of all loans is: $", value_of_loans)

# Using the sum of all loans and the total number of loans, to calculate the average loan price.

average_loan_price = sum(loan_costs) / len(loan_costs)
print(f"The average loan amount is: $", average_loan_price)

"""Part 2: Analyze Loan Data.
Analyze the loan to determine the investment evaluation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Useing get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"Future Value:{future_value}")
print(f"Remaining Months:{remaining_months}")


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate = 0.20
present_value = future_value / (1 + (discount_rate/12)) ** remaining_months
print(f"The fair value of the loan is: {present_value}")


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

cost = loan.get("loan_price")

if present_value >= cost:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.
Perform financial calculations using functions.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defining a function that will be used to calculate present value.
# Includeing parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# returning the `present_value` for the loan.

def price_this_home(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
    return present_value


# Using the function to calculate the present value of the new loan.
# Including an `annual_discount_rate` of 0.2 for this new loan calculation.

annual_discount_rate = 0.2
present_value = price_this_home(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans.
In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Empty list called `inexpensive_loans`

inexpensive_loans = []

# Using a for Loop through all the loans to deturmine if loan_price is less than or equal to $500 and append to the `inexpensive_loans` list

for loan in loans: 
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)


# Print `inexpensive_loans` list

print(f"The inexpensive loans are:{inexpensive_loans}")


"""Part 5: Save the results.
Output this list of inexpensive loans to a csv file
"""

# output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# output file path
output_path = Path("inexpensive_loans.csv")

# using with open to open a new CSV file 
# csvwriter using the csv library.
# csvwriter to write the header variable in the first row.
# Use a for loop to iterate through each loan in inexpensive_loans
# Use csvwriter to write the loan.values() to a row in the CSV file

with open(output_path,"w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())


