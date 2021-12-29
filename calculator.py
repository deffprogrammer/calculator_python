print("========= Calculator =========")
num1 = float(input("Enter the first number : "))
op = input("Enter the operators (+,-) : ")
num2 = float(input("Enter the second number : "))

total = 0

if op == "+":
    total = num1 + num2
elif op == "-":
    total = num1 - num2

print("{} {} {} = {}".format(num1, op, num2, total))