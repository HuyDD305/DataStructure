import random
import math


def binarysearch(aList, guess):
    """A demo of binary search in python"""
    if isinstance(aList, list):
        low = 0
        high = len(aList) - 1
        while low <= high:
            mid = (low + high) // 2
            if aList[mid] == guess:
                return mid
            if guess > aList[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def gen_random():
    aList = []
    for number in range(20):
        number = random.randint(1, 50)
        aList.append(number)
    return aList


if __name__ == "__main__":
    random_list = sorted(gen_random())
    print(random_list)

    guess = int(input("Please enter your number: "))
    x = binarysearch(random_list, guess)
    if x != -1:
        print(f"Found the number at {x}")
    else:
        print("Can't find the number")
