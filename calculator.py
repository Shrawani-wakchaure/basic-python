operator = input("enter any one operator (+ - * /)")
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result =num1 * num2
elif operator == "/":
    result == num1 / num2
else :
    print("symbol not applicable")

print (f"your total is {result}")
