def linear_search(numbers, size, target):
    for i in range(size):
        if numbers[i] == target:
            return target
    return -1


if __name__ == "__main__":
    numbers = [23, 13, 4, 35, 17, 93, 52]
    size = len(numbers)
    target = 17
    result = linear_search(numbers, size, target)

    if result == -1:
        print("Element is not found.")
    else:
        print("Element found at index: ", result)
