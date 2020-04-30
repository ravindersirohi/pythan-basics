import os
os.system('cls')

print('------Number Playground------'.upper())

int_number = input('Enter a number \n')

# Cast input
print(f'As Integer : {int(int_number)}')
print(f'As Float : {float(int_number)}')

print(f'{int_number}x{int_number} : {int(int_number) * float(int_number)}')
print(f'{int_number}^{int_number} : {float(int_number) ** int(int_number)}')
