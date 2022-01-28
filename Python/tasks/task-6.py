<<<<<<< HEAD
'''
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

    Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

Write a program that will return the name of the person who will drink the n-th cola.
'''



def who_is_next(names, r):
    amount_names = len(names)
    residue = r % amount_names

    if r != 1:
        for i in range(r):
            item = names.pop(0)
            names.append(item)
            names.append(item)

    return names[0]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 1))
print(who_is_next(names, 52))
#print(who_is_next(names, 7230702951))

=======
"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

-There must be a function for each number from 0 ("zero") to 9 ("nine")
-There must be a function for each of the following mathematical operations: plus, minus, times,
dividedBy (divided_by in Ruby and Python)
-Each calculation consist of exactly one operation and two numbers
-The most outer function represents the left operand, the most inner function represents the right operand
-Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""


def zero(func=None): return 0 if func is None else eval(f'{func[1]}(0, {func[0]})')
def one(func=None): return 1 if func is None else eval(f'{func[1]}(1, {func[0]})')
def two(func=None): return 2 if func is None else eval(f'{func[1]}(2, {func[0]})')
def three(func=None): return 3 if func is None else eval(f'{func[1]}(3, {func[0]})')
def four(func=None): return 4 if func is None else eval(f'{func[1]}(4, {func[0]})')
def five(func=None): return 5 if func is None else eval(f'{func[1]}(5, {func[0]})')
def six(func=None): return 6 if func is None else eval(f'{func[1]}(6, {func[0]})')
def seven(func=None): return 7 if func is None else eval(f'{func[1]}(7, {func[0]})')
def eight(func=None): return 8 if func is None else eval(f'{func[1]}(8, {func[0]})')
def nine(func=None): return 9 if func is None else eval(f'{func[1]}(9, {func[0]})')


def plus(number1, number2=None): return (number1, 'plus') if number2 is None else number1 + number2
def minus(number1, number2=None): return (number1, 'minus') if number2 is None else number1 - number2
def times(number1, number2=None): return (number1, 'times') if number2 is None else number1 * number2
def divided_by(number1, number2=None): return (number1, 'divided_by') if number2 is None else number1 // number2


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
>>>>>>> a54784f19a28494bda54e960a2a7d116cc94460f
