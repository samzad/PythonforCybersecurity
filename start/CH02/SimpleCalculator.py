#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by Sam on 10/1/21

# Get information from user
first_number = float( input("What is the first number? ") )
activity = input("What activity? ( + - * / ) ")
second_number = float( input("What is the second number? ") )

# Do math
if activity == "+":
    print(first_number + second_number)
if activity == "-":
    print(first_number - second_number)
if activity == "*":
    print(first_number * second_number)
if activity == "/":
    print(first_number / second_number)