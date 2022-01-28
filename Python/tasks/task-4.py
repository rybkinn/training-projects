"""
Complete the solution so that it splits the string into pairs of two
characters. If the string contains an odd number of characters then it
should replace the missing second character of the final pair
with an underscore ('_').
"""


def solution(s):
    result_list = []
    if len(s) != 0:
        index_item_length = 0
        iter_n = 0
        for symb in s:
            if index_item_length % 2 == 0:
                iter_n = 0
            if iter_n < 2 and iter_n == 0 and index_item_length == 0:
                result_list.insert(index_item_length, symb)
            elif iter_n < 2 and iter_n == 0 and index_item_length != 0:
                result_list.append(symb)
            else:
                list_item = result_list.pop()
                result_list.insert(index_item_length, list_item + symb)
            iter_n += 1
            index_item_length += 1
        if len(s) % 2 == 1:
            last_list_item = result_list.pop()
            result_list.append(last_list_item + '_')
    return result_list


print(solution("asdfadsf"))
