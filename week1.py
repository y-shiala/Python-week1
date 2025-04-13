num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
operator = input("Enter an operator (+ - * /): ")

if operator == "+":
  result = num1 + num2
  print(result)
elif operator == "-":
  result = num1 - num2
  print(result)
elif operator == "*":
  result = num1 * num2
  print(result)
elif operator == "/":
  result = num1 / num2
  print(result) 
else:
  print("Enter + - * or /")