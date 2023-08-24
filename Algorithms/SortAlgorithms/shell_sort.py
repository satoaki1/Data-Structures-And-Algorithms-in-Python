def shell_sort(numbers, size, gap):
    while gap > 0:
        for i in range(gap, size):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    size = len(nums)
    gap = size // 2
    print(shell_sort(nums, size, gap))


# Path: practices/quick_sort.py

# Best case: O(n * log(n))
# Worst case: O(n ^ 2)
# Average case: O(n * log(n))
