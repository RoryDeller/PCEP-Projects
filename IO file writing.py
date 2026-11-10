import math
import random

with open('greeting.txt', 'w') as file:
    file.write("Welcome to Python!\n")
    file.write("This is the first line.\n")


with open('greeting.txt', 'r') as file:
    content = file.read()               #read() gets all text as one big string
    print("--- File Content Read ---")
    print(content)
