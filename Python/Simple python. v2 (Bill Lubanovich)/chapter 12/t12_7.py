"""
Найдите все слова, которые заканчиваются на букву r.
"""
import re
import t12_4

result = re.findall(r'\b\w*r\b', t12_4.mammoth)

print(result)
