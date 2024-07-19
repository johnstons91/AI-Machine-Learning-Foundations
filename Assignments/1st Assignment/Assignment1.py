import math

'''
Code Calculator:

- Addition
- Subtraction
- Multiplication
- Division

Add more features and make it user-friendly with multiple revision prompts. 

Please submit the code file and the conversation with the AI chatbot (Chat GPT, Gemini, or Claude).

'''
#Define the Variables

def addition(num1, num2):
    '''Addition: Add 2 numbers & returns teh difference.'''
    return num1 + num2

def subtraction(num1, num2):
    '''Subtraction: Calculating the difference between two numbers by subtracting.'''
    return num1 - num2

def multiplication(num1, num2):
    '''Multiplication: Calculates the product of two numbers.''' 
    return num1 * num2

def division(num1, num2):
    '''Division: Calculates the quotient of two numbers. Error message when divide by zero.'''
    if num2 == 0:
        print("Error: Zero cannot be divided.") 
        return None
    else:
        return num1 / num2
    
#Main calculator function to get user input

def calculator():
    while True:
        try:
            '''Input from users.'''
            num1 = float(input("Enter first number: ")) 
            operator = input("Enter operator (+, -, *, /): ")
        
            if num1.lower() == 'e':
                print("Exiting the calculator. Have a nice day!")
                break
        
            num2 = float(input("Enter second number: "))
        
#Calculator performance based on operator.
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = division(num1, num2)
            else:
                result = "Error: Invalid Operator"
            
            if result is not None:
                print(f"Result: {result}")
            
        except ValueError:
            print("Input not valid! Please enter another number. ")
    
#Runs the calculator

calculator()  
    


