"""
Откройте файл test.txt и считайте его содержимое в строку test2.
Будут ли одинаковыми строки test1 и test2?
"""
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'r') as file:
    test2 = file.read()

print(test1 == test2)
