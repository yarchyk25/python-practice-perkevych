#Завдання 3, Перкевич, ІТ-32

name = "Yaroslav"
surname = "Perkevych"

full_name = name + surname

vowels = "aeiouy"
vowel_count = 0
consonant_count = 0

for char in full_name.lower():
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

total_letters = vowel_count + consonant_count

print(f"{name} {surname}")
print(
    f"Vowels: {vowel_count}, consonants: {consonant_count}\n"
    f"Total letters: {total_letters}"
)