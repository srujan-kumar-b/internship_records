a=input("Enter first number: ")
b=input("Enter second number: ")
op=input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Addition: ", float(a)+float(b))
elif op == "-":
    print("Subtraction: ", float(a)-float(b))
elif op == "*":
    print("Multiplication: ", float(a)*float(b))
elif op == "/":
    print("Division: ", float(a)/float(b))
else:
    print("Invalid operator")