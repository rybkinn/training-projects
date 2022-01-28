"""
Given a list of integers and a single sum value,
return the first two values (parse from the left please) in order of
appearance that add up to form the sum.
"""

"""
sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
"""
import time


start_time = time.time()


def sum_pairs(ints, s):
    index_list = []
    count_delete_index = 0
    ints_without_first_numb = ints.copy()
    for index_first_numb, first_numb in enumerate(ints):
        for index_second_numb, second_numb in enumerate(ints_without_first_numb):
            result = first_numb + second_numb
            if result == s and index_first_numb != index_second_numb + count_delete_index:
                index_list.append((index_first_numb, index_second_numb + count_delete_index))

        ints_without_first_numb.pop(0)
        count_delete_index += 1
    if len(index_list) > 1:
        result_index_pairs = index_list[0]
        for index, item_pairs in enumerate(index_list):
            if item_pairs[1] < result_index_pairs[1]:
                result_index_pairs = index_list[index]
        return [ints[result_index_pairs[0]], ints[result_index_pairs[1]]]
    elif len(index_list) == 1:
        return [ints[index_list[0][0]], ints[index_list[0][1]]]
    else:
        return None


# Tests
l1 = [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [20, -13, 40]
l4 = [1, 2, 3, 4, 1, 0]
l5 = [10, 5, 2, 3, 7, 5]
l6 = [4, -2, 3, 3, 4]
l7 = [0, 2, 0]
l8 = [5, 9, 13, -3]

print(sum_pairs(l1, 8) == [1, 7])
print(sum_pairs(l2, -6) == [0, -6])
print(sum_pairs(l3, -7) == None)
print(sum_pairs(l4, 2) == [1, 1])
print(sum_pairs(l5, 10) == [3, 7])
print(sum_pairs(l6, 8) == [4, 4])
print(sum_pairs(l7, 0) == [0, 0])
print(sum_pairs(l8, 10) == [13, -3])

test_list_10k = []
for n in range(10000):
    test_list_10k.append(n)

sum_pairs(test_list_10k, 10)

print(f'--- {time.time() - start_time} seconds ---')
