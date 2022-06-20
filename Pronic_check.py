import math
def ispronic(number):
    #for in in range()
    value = math.sqrt(number)
    value = round(value)
    num = value * (value + 1)
    if num == number:
        return True
    return False
number = int(input("Enter an integer: "))
print("is ", number, "a pronic number? ", ispronic(number))

# ALTERNATIVELY
"""
def pronic(number):
    for i in range(1, number):
        if (i * (i - 1)) == number:
            return True
        return False

number = int(input("Enter an integer: "))
print(pronic(number))
"""