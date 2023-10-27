# import the math class to be able to use the math functions.
import math
# prompt user to input the type of calculator they wanna use, either bond or investment and store.
calculator_type = input("investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
# if user wants to do investment calculations.
if calculator_type == "investment" :
# prompt user to enter amount they wanna invest, the interest rate, the number of years they wanna make the investment for and the type of investment they'll be using.
    investment_amount = float(input("How much money are you depositing: R"))
    interest_rate = float(input("Enter interest rate, do not enter the percent sign: ")) / 100
    investment_years = float(input("How many years do you plan on investing: "))
    interest = input("Do you want simple or compound interest: ").lower()
# do necessary calculations based on either the user will be using compound or simple interest and print out the necessary message. 
    if interest == "simple" :
        total_money = round(investment_amount * (1 + interest_rate*investment_years),2)
        print(f"The total money you'll get is: R{total_money}")
    elif interest == "compound" :
        total_money = round(investment_amount * math.pow((1+interest_rate),investment_years),2)
        print(f"The total money you'll get is: R{total_money}")
    else:
        print("Enter either simple or compound")

# if the user wants to do bond calculations and print out monthly repayments.
elif calculator_type == "bond" :
    house_value = float(input("Enter the current value of the house: R"))
    interest_rate = (float(input("What  is the annual interest rate, do not enter the percent sign: ")) / 100) / 12
    repayment_months = int(input("Enter the number of months you'll be making the repayment: "))
    monthly_repayment = round((interest_rate * house_value) / (1-(1 + interest_rate)**-repayment_months),2)
    print(f"Your monthly istallment will be: R{monthly_repayment}")

# print out if user did not enter bond or investment when prompted on line 4
else :
    print("please enter either investment or bond")