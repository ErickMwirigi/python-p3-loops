#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i > 0 :
        print(i)
        i -= 1       
        print ('Happy New Year!')

happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = []  # Initialize an empty list to store squared elements
    for num in int_list:
        squared_list.append(num ** 2)  # Square each element and append to the new list
    return squared_list

def fizzbuzz():
    # code goes here!
    pass
    for num in range(1, 101):  # Iterate from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
