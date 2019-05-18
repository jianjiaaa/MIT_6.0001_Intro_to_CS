# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:27:18 2019

@author: user
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0
r = 0.04

num_months = 0

while current_savings < portion_down_payment * total_cost:
    current_savings +=  current_savings * r/12
    current_savings += annual_salary*portion_saved/12
    num_months += 1
print("Number of months required to pay down payment:", num_months)
    