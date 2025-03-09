import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def gen_random():
    aList = []
    for number in range(20):
        number = random.randint(1, 50)
        aList.append(number)
    return aList


if __name__ == "__main__":
    old_list = gen_random()
    print(old_list)
    new_list = selection_sort(old_list)
    print(new_list)
