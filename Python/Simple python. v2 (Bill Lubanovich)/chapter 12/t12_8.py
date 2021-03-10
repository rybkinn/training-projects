"""
Найдите все слова, которые содержат три гласные подряд.
"""
import re
import t12_4

result = re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', t12_4.mammoth)

print(result)
