#Завдання 3, Перкевич, ІТ-32

number1 = float(input('Enter first number:'))
operation = input('Enter the operation symbol:')
number2 = float(input('Enter second number:'))

print('Yaroslav Perkevych, IT-32')

if operation == '+':
    result = number1 + number2
    print(f'{number1} + {number2} = {round(result, 4)}')

elif operation == '-':
    result = number1 - number2
    print(f'{number1} - {number2} = {round(result, 4)}')

elif operation == '*':
    result = number1 * number2
    print(f'{number1} * {number2} = {round(result, 4)}')

elif operation == '/':
    if number2 == 0:
        print('The action cannot be performed.')
    else:
        result = number1 / number2
        print(f'{number1} / {number2} = {round(result, 4)}')

elif operation == '//':
    if number2 == 0:
        print('The action cannot be performed.')
    else:
        result = number1 // number2
        print(f'{number1} // {number2} = {round(result, 4)}')

elif operation == '%':
    if number2 == 0:
        print('The action cannot be performed.')
    else:
        result = number1 % number2
        print(f'{number1} % {number2} = {round(result, 4)}')

elif operation == '**':
    result = number1 ** number2
    print(f'{number1} ** {number2} = {round(result, 4)}')

        
else:
    print('Invalid operation symbol entered.')