number1 = int(input("Enter First Number: "))
sign = input("Enter a sign: ")
number2 = int(input("Enter second Number: "))

if sign == "+":
    print(number1 + number2)
elif sign == "*":
    print(number1 * number2)
elif sign == "-":
    print(number1 - number2)
elif sign == "/":
    print(number1 / number2)
elif sign == "%":
    print(number1 % number2)
else:
    print("Invalid")

