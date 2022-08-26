#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys
    
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        else:
        a, operator, b = argv[1:]
        a = int(a)
        b = int(b)
        if operator == '+':
            print(f"{a} + {b} = {calculator_1.add(a, b)}")
        elif operator == '-':
            print(f"{a} - {b} = {calculator_1.sub(a, b)}")
        elif operator == '*':
            print(f"{a} * {b} = {calculator_1.mul(a, b)}")
        elif operator == '/':
            print(f"{a} / {b} = {calculator_1.div(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
