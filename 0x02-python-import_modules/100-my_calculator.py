#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def handle_basic_operation(a, operator, b):
    if operator == '+':
        result = add(int(a), int(b))
    elif operator == '-':
        result = sub(int(a), int(b))
    elif operator == '*':
        result = mul(int(a), int(b))
    elif operator == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    print(f"{a} {operator} {b} = {result}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    
    handle_basic_operation(a, operator, b)
