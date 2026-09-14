#Завдання 5, Перкевич, ІТ-32

print("Yaroslav Perkevych, IT-32")

day = int(input("Enter day (integer): "))
month = int(input("Enter month (integer): "))
year = int(input("Enter year (integer): "))

if month < 1 or month > 12:
    print(f"Date is invalid: month must be from 1 to 12.")

elif year <= 0:
    print(f"Date is invalid: year must be positive.")

else:
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28

    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30

    else:
        max_days = 31

    if day < 1 or day > max_days:
        print(f"Date is invalid: day must be from 1 to {max_days} for this month.")

    else:
        print(f"Date is valid: {day}.{month}.{year}")