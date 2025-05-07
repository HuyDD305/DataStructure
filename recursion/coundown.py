def recursive_countdown(number):
    number = int(number)
    print(number)
    if number <= 1:
        return
    else:
        recursive_countdown(number - 1)


if __name__ == '__main__':
    # aList = []
    # for i in range(1, 21):
    #     aList.append(i)
    #
    # print(aList)

    recursive_countdown(20)
