#Завдання 5, Перкевич, ІТ-32

d = 25
c = len("Perkevych")  
n = d * c  

print("Yaroslav Perkevych, IT-32")
print(f"n = {d} * {c} = {n}")

divisors_str = ""
divisors_count = 0
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors_str += f"{i} "
        divisors_count += 1
        divisors_sum += i

print(f"Divisors: {divisors_str.strip()}")
print(f"Divisors count: {divisors_count}, sum: {divisors_sum}")

if n < 2:
    print(f"{n} is not prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

primes_str = ""
primes_count = 0

for num in range(2, n + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        primes_str += f"{num} "
        primes_count += 1

print(
    f"Primes up to {n}: {primes_str.strip()}\n"
    f"Primes count: {primes_count}"
)