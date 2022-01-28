"""
Подходило 1 сентября, университет готовился к наплыву абитуриентов. 
Так вышло, что Вы, как программист, должны были помочь в отборе тех 
абитуриентов, кто поступит в университет на конкурсной основе на 
специальность программиста. 

Схема была проста: есть абитуриент, у него есть результаты сданных 
экзаменов по математике, русскому и информатике. Соответственно, 
у каждого потенциального студента есть сумма баллов по этим экзаменам. 
Также есть дополнительные (extra_scores) баллы: за волонтерство, 
участие в олимпиадах и другие активности. 

Вам нужно отобрать 20 человек, у которых суммарный балл выше, 
чем у других. В случае, если не получается однозначно определить 
20 человек (например, 2 человека набрали одинаковое СУММАРНОЕ 
количество баллов и претендуют на 20 место в списке, стоит их 
ранжировать по "профильным" дисциплинам - "информатике" и "математике").

Напишите функцию find_top_20 *
Функция принимает на вход список сводной информации по 
абитуриентам (candidates) и возвращает список с именами 20 человек, 
набравших наибольшее СУММАРНОЕ количество баллов 
(с учетом extra баллов), которые станут студентами университета. 
Пример входных данных приведен ниже.
"""


def find_top_20(candidates:list) -> list:
    results_candidates = []

    new_id = 1
    for candidate in candidates:
        results_candidates.append({
            "id": new_id,
            "name": candidate["name"],
            "scores_sum_math_and_computer_science": \
                candidate["scores"]["math"] + candidate["scores"]["computer_science"],
            "scores_sum_all": sum(candidate["scores"].values()) + candidate["extra_scores"]
        })
        new_id += 1
    
    sorted_math_and_computer_science_candidates = sorted(
        results_candidates,
        key=lambda item: item['scores_sum_math_and_computer_science'],
        reverse=True)

    sorted_results_candidates = sorted(
        sorted_math_and_computer_science_candidates, 
        key=lambda item: item['scores_sum_all'], 
        reverse=True)

    if len(sorted_results_candidates) > 20:
        sorted_results_candidates[:20]

    admitted_candidates = []
    for candidates in sorted_results_candidates:
        admitted_candidates.append(candidates['name'])

    return admitted_candidates



candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores":0},
 {"name": "Anatoliy",  "scores": {"math": 33, "russian_language": 85, "computer_science": 52},  "extra_scores":2},
 {"name": "Anton",  "scores": {"math": 33, "russian_language": 67, "computer_science": 41},  "extra_scores":0},
 {"name": "Artur",  "scores": {"math": 72, "russian_language": 26, "computer_science": 69},  "extra_scores":0},
 {"name": "Boris",  "scores": {"math": 86, "russian_language": 36, "computer_science": 45},  "extra_scores":0},
 {"name": "Denis",  "scores": {"math": 18, "russian_language": 60, "computer_science": 35},  "extra_scores":3},
 {"name": "Igor",  "scores": {"math": 49, "russian_language": 74, "computer_science": 57},  "extra_scores":1},
 {"name": "Ilya",  "scores": {"math": 51, "russian_language": 69, "computer_science": 62},  "extra_scores":0},
 {"name": "Leonid",  "scores": {"math": 47, "russian_language": 18, "computer_science": 19},  "extra_scores":0},
 {"name": "Vasya",  "scores": {"math": 69, "russian_language": 36, "computer_science": 67},  "extra_scores":0},
 {"name": "Igor",  "scores": {"math": 67, "russian_language": 39, "computer_science": 67},  "extra_scores":0},
 {"name": "Denis",  "scores": {"math": 37, "russian_language": 20, "computer_science": 57},  "extra_scores":5},
 {"name": "Maksim",  "scores": {"math": 35, "russian_language": 21, "computer_science": 63},  "extra_scores":4},
 {"name": "Nikita",  "scores": {"math": 90, "russian_language": 54, "computer_science": 73},  "extra_scores":3},
 {"name": "Nikolay",  "scores": {"math": 44, "russian_language": 62, "computer_science": 81},  "extra_scores":2},
 {"name": "Valeriy",  "scores": {"math": 37, "russian_language": 71, "computer_science": 61},  "extra_scores":1},
 {"name": "Nikita",  "scores": {"math": 27, "russian_language": 66, "computer_science": 64},  "extra_scores":0},
 {"name": "Yan",  "scores": {"math": 26, "russian_language": 47, "computer_science": 43},  "extra_scores":0},
 {"name": "Stepan",  "scores": {"math": 49, "russian_language": 35, "computer_science": 52},  "extra_scores":0},
 {"name": "Nikita",  "scores": {"math": 55, "russian_language": 39, "computer_science": 22},  "extra_scores":0},
 {"name": "Ruslan",  "scores": {"math": 74, "russian_language": 33, "computer_science": 43},  "extra_scores":0},
 {"name": "Pavel",  "scores": {"math": 20, "russian_language": 22, "computer_science": 51},  "extra_scores":0},
 {"name": "Igor",  "scores": {"math": 67, "russian_language": 47, "computer_science": 54},  "extra_scores":1},
 {"name": "Timofey",  "scores": {"math": 97, "russian_language": 85, "computer_science": 61},  "extra_scores":1},
 {"name": "Petya",  "scores": {"math": 25, "russian_language": 33, "computer_science": 34},  "extra_scores":1}
]

print(find_top_20(candidates))
