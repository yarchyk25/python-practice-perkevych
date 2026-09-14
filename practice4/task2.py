#Завдання 2, Перкевич, ІТ-32

print("Yaroslav Perkevych, IT-32")

number = int(input("Enter birth date (ddmmyyyy): "))

count = 0
total_sum = 0
max_digit = 0
min_digit = 9
reversed_num = 0

while number > 0:
    digit = number % 10

    count += 1
    total_sum += digit

    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit

    reversed_num = reversed_num * 10 + digit

    number = number // 10

print(
    f"Digit count: {count}\n"
    f"Sum of digits: {total_sum}\n"
    f"Max digit: {max_digit}\n"
    f"Min digit: {min_digit}\n"
    f"Reversed number: {reversed_num}"
)