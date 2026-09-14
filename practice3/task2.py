#Завдання 2, Перкевич, ІТ-32

print('Yaroslav Perkevych, IT-32')

num = int(input('Enter the integer:'))

if num > 0:
    print('The number is positive.')
elif num < 0:
    print('The number is negative.')
else:
    print('The number is 0')

if num != 0:
    if num % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
