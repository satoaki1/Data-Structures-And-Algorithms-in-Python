def bucket_sort(numbers):
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size - 1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


def insertion_sort(numbers):
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers


if __name__ == "__main__":
    import random

    numbers = [random.randint(0, 1000) for _ in range(11)]
    print(bucket_sort(numbers))

# Path: practices/heap.py

# Best case: O(n * log(n))
# Worst case: O(n * log(n))
# Average case: O(n * log(n))
