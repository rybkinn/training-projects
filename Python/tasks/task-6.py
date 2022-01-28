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

