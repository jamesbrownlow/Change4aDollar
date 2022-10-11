# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:27:31 2022

@author: Dylan Reynolds

Problem:
    Write a python program to find the total number of ways to make change for $1

    Examples: 100 pennies, or 75 pennies and 5 nickels
"""

coins = (50, 25, 10, 5, 1)

howManyWays = 0

for fifty in range(3): #50 cent pieces
    for quarter in range(5): #25 cent pieces
        for dimes in range(11): #10 cent pieces
            for nickels in range(51): #5 cent pieces
                for pennies in range(101): #1 cent pieces
                    amt = fifty*50 + quarter*25 + dimes*10 + nickels*5 + pennies
                    if amt == 100:
                        howManyWays += 1
                        print(f'fifty={fifty} quarter={quarter} dimes={dimes} nickels={nickels} pennies={pennies}')