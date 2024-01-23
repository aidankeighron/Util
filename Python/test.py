from random import randrange

def quick_sort(collection):
    length = len(collection)

    if length < 2:
        return collection

    pivot_index = randrange(length)
    pivot = collection.pop(pivot_index)

    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    a = [*lesser, pivot, *greater]
    print(a)
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


print(quick_sort([5,1,3,2]))