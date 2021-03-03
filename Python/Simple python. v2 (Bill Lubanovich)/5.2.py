"""
Выведите на экран все вопросы из списка, а также правильные ответы в таком виде:
Q: вопрос
A: ответ
"""

questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]

answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "'Pop!' goes the weasel."
           ]

print(
    questions[0] + '\n' + answers[1] + '\n\n'
    + questions[1] + '\n' + answers[2] + '\n\n'
    + questions[2] + '\n' + answers[0]
)
