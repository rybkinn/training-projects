"""
Байты, содержащиеся в переменной gif, определяют однопиксельный
прозрачный GIF-файл. Этот формат является одним из самых распространенных.
Корректный файл формата GIF начинается со строки GIF89a.
Корректен ли этот файл?
"""
import binascii

g = b'47494638396101000100800000000000ffffff21f9' \
      + b'0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(g)

print(gif.startswith(b'GIF89a'))