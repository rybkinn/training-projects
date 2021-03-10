"""Напишите последний элемент списка surprise со строчной буквы,
затем выведите эту строку в обратном порядке и с прописной буквы."""

surprise = ['Groucho', 'Chico', 'Harpo']

surprise[-1] = surprise[-1].lower()

print(surprise[-1][::-1].capitalize())
