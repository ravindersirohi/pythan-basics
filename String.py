import os, datetime
os.system('cls')
# String Playground
print('/n------String Playground------')

# Multiple assignment
x, y, z, address = (1.4, 1, True, 'Bond Street')

# Format string
print('Your values {3}, {2}, {1}, {0}'.format(x, y, z, address))
print(address[0:4])

# Input
name = input('What is your name ?\n')
print(f'Hello {name.upper()}, you are great!!')

#DateTime
your_age = 21
print('If we asssume you are ' + str(your_age) + ' yeasrs old!')
birth_year = datetime.datetime.now().year-your_age
print(f'Your was born in {birth_year}.')
