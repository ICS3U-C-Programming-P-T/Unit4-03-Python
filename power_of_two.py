#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/18/2025
# This program calculates the power of two using a while loop


try:
    # Ask user for a positive integer
    user_num = int(input("Give a positive integer: "))

    # Check if the number is positive
    if user_num < 0:
        print("Please enter a positive number")

    # Calculate power of two using a for loop
    else:
        for counter in range(0, user_num + 1):
            answer = counter**2
            print(f"{counter} * 2 = {answer}")

    # If the input is not an integer
except ValueError:
    print("Please enter a positive integer")
