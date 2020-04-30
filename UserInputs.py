import os
from CalculatorClass import Calculator
os.system('cls')

# Capture user Input

first_input = input('Please enter first input \n')
second_input = input('Please enter second input \n')
operator = input('Please enter an operator (+, -, x, / )\n')

# Use a Class
calculator = Calculator(float(first_input), float(second_input), operator)
result = calculator.calculate()
os.system('cls')
print(f'Result : {first_input} {operator} {second_input} = {result}')
