# Завдання 4, Перкевич, ІТ-32
print('Yaroslav Perkevych, IT-32')

def read_grade(prompt):
    """Prompt user until a valid integer grade between 0 and 100 is entered."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Error: digits only")
            continue
        grade = int(value)
        if 0 <= grade <= 100:
            return grade
        print("Error: the value must be between 0 and 100")

def to_letter(grade):
    """Convert numeric grade to letter grade A-F using multiple returns."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"

def average(grades):
    """Calculate and return arithmetic mean of grades list."""
    return sum(grades) / len(grades)

def count_above(grades, limit):
    """Count how many grades are strictly greater than the limit."""
    count = 0
    for grade in grades:
        if grade > limit:
            count += 1
    return count

def print_report(name, group, grades):
    """Print complete academic report using helper functions."""
    avg_grade = average(grades)
    letter = to_letter(avg_grade)
    above_avg = count_above(grades, avg_grade)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    
    print("Grades:", end=" ")
    for g in grades:
        print(g, end=" ")
    print()

    print(f"Average: {avg_grade:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above_avg}")

def main():
    """Run the main grading workflow."""
    name = "Yaroslav Perkevych"
    group = "IT-32"
    first_name = "Yaroslav"
    n = max(3, len(first_name))

    grades = []
    for i in range(1, n + 1):
        grade = read_grade(f"Grade {i} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)

main()