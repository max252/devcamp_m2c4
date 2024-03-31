#!/usr/bin/python3

from decimal import Decimal
import math

# Exercise 1
# Create a list, tuple, float, integer, decimal, and dictionary.
test_list = [1, 2, 3, "4"]
test_tuple = ("one", "two", 3)
test_float = 11.1
test_integer = 10
test_decimal = Decimal(100)
test_dict = {"name": "Maksym", "age": 44}

# Exercise 2
# Round your float up.
test_float_round_up = math.ceil(test_float)

# Exercise 3
# Get the square root of your float.
test_float_sqrt = math.sqrt(test_float)

# Exercise 4
# Select the first element from your dictionary.
test_dict_first_element = test_dict["name"]

# Exercise 5
# Select the second element from your tuple.
test_tuple_second_element = test_tuple[1]

# Exercise 6
# Add an element to the end of your list.
test_list.append("end")

# Exercise 7
# Replace the first element in your list.
test_list[0] = 5

# Exercise 8
# Sort your list alphabetically.
test_list_alpha = ["dca", "abc", "xyz"]
test_list_alpha.sort()

# Exercise 9
# Use reassignment to add an element to your tuple.
test_tuple_list = list(test_tuple)
test_tuple_list.append("add element")
test_tuple = tuple(test_tuple_list)
# or
test_tuple += ("new element",)
