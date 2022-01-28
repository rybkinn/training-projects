"""
У студентов-программистов шел последний год обучения, и близилась 
выдача дипломов. К этой знаменательной дате было решено подготовить 
символические подарки трем студентам, которые имеют максимальный 
средний балл по итогам обучения. Но задача осложнялась тем, что нужно 
предоставить эти данные в бухгалтерию, причем так, чтобы главный 
бухгалтер Ольга Петровна, списывающая деньги на подарки, смогла 
открыть это в своём любимом Excel.

Впрочем, для Вас, человека который работает не первый год в данном 
учреждении, это не казалось невыполнимой задачей.

Вам нужно написать функцию make_report_about_top3 *
Функция make_report_about_top3 принимает словарь (students_avg_scores), 
в котором ключами являются имена студентов, а значениями — средний балл 
за всю учебу. Функция находит ТОП-3 студентов, чей средний балл выше, 
чем у других. Функция возвращает ссылку на эксель-файл, в котором 
упомянуты 3 студента и который потом будет передан в бухгалтерию. 
Сам файл необходимо создать внутри функции. Важно сохранить 
совместимость с Excel, чтобы Ольга Петровна смогла без проблем 
получить всю нужную информацию. 
"""
import xlsxwriter
from pathlib import Path


def make_report_about_top3(students_avg_scores: dict[str, float]) -> Path:

    students_avg_scores_sorted = sorted(
        students_avg_scores.items(), 
        key=lambda item: item[1], 
        reverse=True)
    
    top3_xlsx = xlsxwriter.Workbook('report_about_top3.xlsx')
    worksheet = top3_xlsx.add_worksheet()

    for index, student_info in zip(range(3), students_avg_scores_sorted):
        worksheet.write(index, 0, student_info[0])
        worksheet.write(index, 1, student_info[1])

    top3_xlsx.close()

    excel_file = Path('report_about_top3.xlsx')
    return excel_file.absolute()


# Пример входных данных:
students_avg_scores = {
    'Max': 4.964, 
    'Eric': 4.962, 
    'Peter': 4.923, 
    'Mark': 4.957, 
    'Julie': 4.95, 
    'Jimmy': 4.973, 
    'Felix': 4.937, 
    'Vasya': 4.911, 
    'Don': 4.936, 
    'Zoi': 4.937}


print(make_report_about_top3(students_avg_scores))
