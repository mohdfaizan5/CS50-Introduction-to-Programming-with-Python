#program that calculates the mathemetic operations:
"""
x is an integer
y is +, -, *, or /
z is an integer
"""

user_input = input("Expression: ").split()
# print(user_input)

x = int(user_input[0])
y = user_input[1]
z = int(user_input[2])

if user_input[1] == "+":
    print(float(x+z))
if user_input[1] == "-":
    print(float(x-z))
if user_input[1] == "*":
    print(float(x*z))
if user_input[1] == "/":
    print(float(x/z))
    
# calcu = x 