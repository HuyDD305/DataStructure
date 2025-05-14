def sum(arr):
    if isinstance(arr, list):
        if arr:
            return arr.pop() + sum(arr)
        else:
            return 0



if __name__ == "__main__":
    print(sum([2, 4, 6]))
    print("just testing")
