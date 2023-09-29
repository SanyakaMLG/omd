import csv
from datetime import datetime

# maybe better to use enum but idk how
DEPARTMENT = 'Департамент'
SALARY = 'Оклад'
MIN_SALARY = 'Минимальная зарплата'
MAX_SALARY = 'Максимальная зарплата'
AVG_SALARY = 'Средняя зарплата'
DEP_SIZE = 'Численность'
TEAM = 'Отдел'


def print_teams(filename: str) -> None:
    """
    Prints a list of departments and their teams
    :param filename: The name of input file in CSV format
    :return: None
    """
    departments = {}
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=';')
        for row in file_reader:
            department = row[DEPARTMENT]
            if department not in departments:
                departments[department] = set()
            departments[department].add(row[TEAM])

    for dep, teams in departments.items():
        print(dep)
        for team in teams:
            print(' ' * 4, team)


def get_depart_report(filename: str) -> dict:
    """
    Retrieves department-wise statistics from a CSV file
    :param filename: The name of input file in CSV format
    :return: dict: A dictionary containing department-wise statistics,
                   including department size, minimum salary,
                   maximum salary, and average salary
    """
    departments = {}
    with open(filename, 'r', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=';')
        for row in file_reader:
            salary = row[SALARY]
            department = row[DEPARTMENT]
            if department not in departments:
                departments[department] = {
                    DEP_SIZE: 1,
                    MIN_SALARY: int(salary),
                    MAX_SALARY: int(salary),
                    AVG_SALARY: float(salary)
                }
            else:
                departments[department][DEP_SIZE] += 1
                departments[department][AVG_SALARY] += float(salary)
                if int(salary) < departments[department][MIN_SALARY]:
                    departments[department][MIN_SALARY] = int(salary)
                if int(salary) > departments[department][MAX_SALARY]:
                    departments[department][MAX_SALARY] = int(salary)

    for department, stat in departments.items():
        stat[AVG_SALARY] = round(stat[AVG_SALARY] / stat[DEP_SIZE], 2)

    return departments


def print_report(filename: str) -> None:
    """
    Print a report based on the input file in CSV format
    :param filename: The name of input file in CSV format
    :return: None
    """
    departments = get_depart_report(filename)
    for department, stat in departments.items():
        print(department)
        for key, value in stat.items():
            print(' ' * 4, key, value)


def report_to_csv(filename: str) -> None:
    """
    Generates a report in CSV format based on the input file provided
    :param filename: The name of input file in csv format
    :return: None
    """
    departments = get_depart_report(filename)
    report_filename = 'report_' + \
                      datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    with open(report_filename, 'w', encoding='utf-8') as file:
        names = [DEPARTMENT, DEP_SIZE, MIN_SALARY, MAX_SALARY, AVG_SALARY]
        file_writer = csv.DictWriter(file, delimiter=';',
                                     fieldnames=names,
                                     lineterminator='\n')
        file_writer.writeheader()
        for department, stat in departments.items():
            row = {DEPARTMENT: department} | stat
            file_writer.writerow(row)
    print('Report successfully generated:', report_filename)


if __name__ == '__main__':
    print(
        'Выберите действие (число):\n'
        '1. Вывести иерархию команд\n'
        '2. Вывести сводный отчёт по департаментам\n'
        '3. Сохранить сводный отчёт по департаментам в csv'
    )
    while True:
        try:
            action = int(input())
            if not 1 <= action <= 3:
                raise ValueError
        except ValueError:
            print('Некорректный ввод, введите число от 1 до 3')
        else:
            break

    functions = [print_teams, print_report, report_to_csv]
    functions[action - 1]('Corp_Summary.csv')
