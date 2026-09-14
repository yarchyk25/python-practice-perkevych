# Завдання 2, Перкевич, ІТ-32
print('Yaroslav Perkevych, IT-32')

def print_age(year):
    age = 2026 - year
    print(age)

def get_age(year, current_year=2026):
    if year < 0 or year > current_year:
        return -1
    else:
        age = current_year - year
        return age
        print("after return")

print_age(2008)
get_age(2008)
print(print_age(2008))

age_in_months = get_age(2008) * 12
print(f'Age in month: {age_in_months}')

age_in_weeks = get_age(2008) * 52
print(f'Age in weeks: {age_in_weeks}')

age_in_2030 = get_age(2008, current_year=2030)
print(f'Age in 2030: {age_in_2030}')

# print(print_age(2008) * 12)

print(f'Check at a value of 3000: {get_age(3000)}')