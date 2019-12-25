origin_text = list(input())
code_text = list(input())
need_code = list(input())
need_de_code = list(input())

i = 0
j = 0

for symbol_orogin in need_code:
    for symbol_code in origin_text:
        if symbol_orogin == symbol_code:
            need_code[j] = code_text[i]
            i = 0
            break
        i += 1
    j += 1
    if j == len(need_code):
        i = 0
        j = 0

for symbol_orogin_decode in need_de_code:
    for symbol_code_decode in code_text:
        if symbol_orogin_decode == symbol_code_decode:
            need_de_code[j] = origin_text[i]
            i = 0
            break
        i += 1
    j += 1

for symbol_pr_encode in need_code:
    print(symbol_pr_encode, end='')

print()
for symbol_pr_decode in need_de_code:
    print(symbol_pr_decode, end='')
