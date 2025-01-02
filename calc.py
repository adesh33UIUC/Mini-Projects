print('Welcome to my first project!!!')
print("\"W Calculator\" - By Anish Deshpande")

operand = input("Input an operand (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operand == "+":
    print(num1 + num2)
elif operand == "-":
    print(num1 - num2)
elif operand == "*":
    print(num1 * num2)
elif operand == "/":
    print(num1 / num2)
else:
    print(operand + " isn't a valid operand")