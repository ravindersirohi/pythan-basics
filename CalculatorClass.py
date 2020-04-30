class Calculator:
    add, sub, mul, div = ('+', '-', 'x', '/')

    def __init__(self, first, second, operation):
        self.first = first
        self.second = second
        self.operation = operation

    def calculate(self):
        if self.operation == self.add:
            return self.first+self.second
        elif self.operation == self.sub:
            return self.first-self.second
        elif self.operation == self.mul.lower():
            return self.first*self.second
        elif self.operation == self.div:
            return self.first/self.second
        else:
            return f'Invalid operator ({self.operation}) supplied!'


# Runn Test
first_Input = 3
second_Input = 2
operation = '+'
calculator = Calculator(first_Input, second_Input, operation)
result = calculator.calculate()
print(f'Test Result {first_Input} {operation} {second_Input} = {result}')
