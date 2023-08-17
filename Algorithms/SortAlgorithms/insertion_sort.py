def insertion_sort(numbers, size):
    for i in range(1, size):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j = j - 1

        numbers[j + 1] = temp

    return numbers


if __name__ == "__main__":
    import random
    numbers = [random.randint(0, 100) for _ in range(15)]
    size = len(numbers)
    print(insertion_sort(numbers, size))
