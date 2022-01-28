"""
Когда вам будет (или уже было) 10 000 дней от роду?
"""
import datetime

data = datetime.date(1992, 7, 24)

data_new = data + datetime.timedelta(days=10000)

print(data_new)
