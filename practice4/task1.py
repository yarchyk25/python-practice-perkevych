#Завдання 1, Перкевич, ІТ-32

c = len('Perkevych')
d = 25

print("Yaroslav Perkevych, IT-32")

count_for = 0
sum_for = 0
prod_for = 1
even_count_for = 0
odd_count_for = 0

for num in range(d, 32):
    print(num)
    count_for += 1
    sum_for += num
    prod_for *= num

    if num % 2 == 0:
        even_count_for += 1
    else:
        odd_count_for += 1


avg_for = sum_for / count_for if count_for > 0 else 0

print(
    f"Number count: {count_for}\n"
    f"Sum: {sum_for}\n"
    f"Product: {prod_for}\n"
    f"Arithmetic mean: {avg_for:.2f}\n"
    f"Even: {even_count_for}, Odd: {odd_count_for}"
)

# while version

count_while = 0
sum_while = 0
prod_while = 1
even_count_while = 0
odd_count_while = 0

current = d
while current <= 31:
    print(current)
    count_while += 1
    sum_while += current
    prod_while *= current

    if current % 2 == 0:
        even_count_while += 1
    else:
        odd_count_while += 1

    current += 1


avg_while = sum_while / count_while if count_while > 0 else 0

print(
    f"Number count: {count_while}\n"
    f"Sum: {sum_while}\n"
    f"Product: {prod_while}\n"
    f"Arithmetic mean: {avg_while:.2f}\n"
    f"Even: {even_count_while}, Odd: {odd_count_while}"
)

# Countdown
for num in range(c, 0, -1):
    print(num)
