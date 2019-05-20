def remove_duplicates(tab):
    """Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
    list minus all the duplicates.

    Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
    """
    new_t = []
    for i in tab:
        if i not in new_t:
            new_t.append(i)
    return new_t


def remove_duplicates_set(tab):
    return sorted(set(tab))


print(remove_duplicates([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
print(remove_duplicates_set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))

