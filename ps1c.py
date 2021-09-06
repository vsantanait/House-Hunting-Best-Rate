#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:58:21 2021

@author: vanessamsantana
"""

# REFERENCE POST: https://stackoverflow.com/questions/53374233/mit-programming-in-python-problem-set-1-part-c

def calculateSavings(current_Savings, monthly_Salary, portion_saved, downpayment_months):
    
    semi_annual_raise = 0.07
    monthly_invest_return = 0
    r = 0.04 #annual return at end of each month
    
    for downpayment_months in range(1, 37):
        if (downpayment_months%6 == 0):
            
            annual_salary = monthly_Salary * 12
            annual_salary = annual_salary + (annual_salary*semi_annual_raise)
            monthly_Salary = annual_salary/12
            
        current_Savings = current_Savings + (monthly_Salary * portion_saved)
    
        current_Savings = current_Savings + monthly_invest_return
        monthly_invest_return = current_Savings*(r/12)
        
        current_Savings = round(current_Savings, 0)
        # print("Current savings: " + str(current_Savings) + ", on month " + str(downpayment_months))
    
    return (current_Savings)

x = 1.0
epsilon = 100
numGuesses = 0
low = 0.0
high = max(0.0, x)
ans = (high + low)/2.0
portion_saved = ans


portion_down_payment = 0.25
# monthly_invest_return = 0
current_savings = 0.0

# annual_salary = 300000 #150000

total_cost = 1000000.0

downpayment_months = 36
downpayment_amount = total_cost*portion_down_payment
# print("Down payment: " + str(downpayment_amount))
# print()


annual_salary = input("Enter the starting salary: ")
print()

annual_salary = float(annual_salary)
monthly_salary = annual_salary/12
  

while abs(current_savings - downpayment_amount) >= epsilon:
    
    # portion_saved = round(portion_saved, 4)
    current_savings = calculateSavings(current_savings, monthly_salary, portion_saved, 1)
    
    
    # print("Saved Percentage: " + str(portion_saved))
    # print("Current savings in " + str(downpayment_months) + " months: " + str(current_savings))
    # print()
    
    if (current_savings < downpayment_amount):
        low = ans
        current_savings = 0
        
    elif (current_savings > downpayment_amount + epsilon):
        high = ans
        current_savings = 0
        
    if (numGuesses > 50):
        print("It is not possible to pay the down payment in " + str(downpayment_months) + " months.")
        print()
        break
    
    
    
    ans = (high + low)/2.0
    ans = round(ans, 4)
    portion_saved = ans
    numGuesses = numGuesses + 1

if (numGuesses < 50):
    print("Best Savings Rate: " + str(portion_saved))
    print("Down payment: " + str(downpayment_amount))
    print("Final savings amount: " + str(current_savings))
    print("Steps in Bisection Search: " + str(numGuesses))
    
    
    

