def add(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers and returns the difference."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers and returns the product."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers and returns the quotient. 
      Handles division by zero error."""
  if num2 == 0:
    print("Error: Cannot divide by zero.")
    return None
  else:
    return num1 / num2

# Get user input
while True:
  print("Enter first number: ")
  try:
    num1 = float(input())
    break
  except ValueError:
    print("Invalid input. Please enter a number.")

while True:
  print("Enter operator (+, -, *, /): ")
  operator = input()
  if operator in ["+", "-", "*", "/"]:
    break
  else:
    print("Invalid operator. Please use +, -, *, or /.")

while True:
  print("Enter second number: ")
  try:
    num2 = float(input())
    break
  except ValueError:
    print("Invalid input. Please enter a number.")

# Perform calculation based on operator
result = None
if operator == "+":
  result = add(num1, num2)
elif operator == "-":
  result = subtract(num1, num2)
elif operator == "*":
  result = multiply(num1, num2)
elif operator == "/":
  result = divide(num1, num2)

# Print the result
if result is not None:
  print("The result is:", result)
else:
  print("Calculation failed.")