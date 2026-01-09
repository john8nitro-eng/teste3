def calculator():
    """Teste calculator that performs basic arithmetic operations."""
    print("Simple Calculator")
    print("-" * 30)
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator!")
            return
        
        print(f"\n{num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
