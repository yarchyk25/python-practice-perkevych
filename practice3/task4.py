#Завдання 4, Перкевич, ІТ-32

score = int(input('Enter your score(integer):'))
missed_classes = int(input('Enter the number of missed classes(integer):'))

if score < 0 or score > 100:
    print('Incorrect score entered.')

else:
    if 90 <= score <= 100:
        grade = 'A'

    elif 82 <= score <= 89:
        grade = 'B'

    elif 74 <= score <= 81:
        grade = 'C' 

    elif 64 <= score <= 73:
        grade = 'D'

    elif 60 <= score <= 63:
        grade = 'E'

    else:
        grade = 'F'

    max_absences = 0.30 * 16

    print('Yaroslav Perkevych, IT-32')

    if missed_classes > max_absences:
        print('Warning: not admitted.')
        print(f'Score: {score}, grade: {grade}, failed')

    elif score >= 60:
        print(f'Score: {score}, grade: {grade}, passed')

    else:
        print(f'Score: {score}, grade: {grade}, failed')