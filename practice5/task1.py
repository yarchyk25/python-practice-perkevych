# Завдання 1, Перкевич, ІТ-32

print('Yaroslav Perkevych, IT-32')

# Без параметрів
def print_card():
    print(
        'Name: Yaroslav.\n'
    'Surname: Perkevych.\n'
    'Group: IT-32.\n'
    'Year: 2008'
    )

print('no parameters, call 1')
print_card()

print('no parameters, call 2')
print_card()

print('no parameters, call 3')
print_card()

# З параметрами
def print_card_args(name, surname, group, year):
    print(
        f'Name: {name}\n'
        f'Surname: {surname}\n'
        f'Group: {group}\n'
        f'Year: {year}'
        )

print('positional arguments')
print_card_args('Yaroslav', 'Perkevych', 'IT-32', 2008)

print('keyword arguments')
print_card_args(surname='Perkevych', year=2008, name='Yaroslav', group='IT-32')

print('mixed arguments')
print_card_args('Yaroslav', 'Perkevych', year=2008, group='IT-32')

# Зі значенням за замовчуванням

def print_card_default(name, surname, year, group='IT-32'):
    print(
        f'Name: {name}\n'
        f'Surname: {surname}\n'
        f'Group: {group}\n'
        f'Year: {year}'
    )

print('default argument call')
print_card_default('Yaroslav', 'Perkevych', 2008)

print_card_args('Yaroslav')
print_card_args(name='Yaroslav', 'Perkevych') 