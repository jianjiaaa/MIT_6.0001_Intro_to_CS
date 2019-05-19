# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:56:47 2019

@author: user
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0
r = 0.04

num_months = 0

while current_savings < portion_down_payment * total_cost:
    current_savings +=  current_savings * r/12
    current_savings += annual_salary*portion_saved/12
    num_months += 1
    if num_months % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary
print("Number of months required to pay down payment:", num_months)
    
