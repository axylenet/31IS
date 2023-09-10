#Гаврюшкин Максим 31ИС-21
import re

# Функция для чтения информации о предметах и группах из первого файла
def read_subjects_and_groups(file_name):
    data = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'(\d+\w+-\d+):(.+)', line)
            if match:
                group = match.group(1)
                subjects = match.group(2).split(',')
                data[group] = subjects
    return data

# Функция для чтения информации о студентах и их оценках из второго файла
def read_students(file_name):
    students = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'(.+):(\d+\w+-\d+,.+)', line)
            if match:
                name = match.group(1)
                student_data = match.group(2).split(',')
                group = student_data[0]
                grades = {subject.split('-')[0]: int(subject.split('-')[1]) for subject in student_data[1:]}
                students.append((name, group, grades))
    return students

# Функция для проверки стипендии студента
def check_scholarship(grades):
    for grade in grades.values():
        if grade < 4:
            return "не получает стипендию"
    if all(grade > 4 for grade in grades.values()):
        return "получает повышенную стипендию"
    return "получает обычную стипендию"

# Чтение данных из файлов
subjects_and_groups_data = read_subjects_and_groups('file1.txt')
students_data = read_students('file2.txt')

# Вывод информации о студентах и их стипендиях
for i, student_info in enumerate(students_data, start=1):
    name, group, grades = student_info
    subjects = subjects_and_groups_data.get(group)
    if subjects:
        eligible = check_scholarship(grades)
        if eligible != "не получает стипендию":
            print(f"{i}.{name} {group},{', '.join([f'{subject}-{grade}' for subject, grade in grades.items()])} - {eligible}")

