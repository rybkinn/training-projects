"""
Найдите все четырехбуквенные слова, которые начинаются с буквы c.
"""
import re
import t12_4

result = re.findall(r'\bc\w{3}\b', t12_4.mammoth)

print(result)
