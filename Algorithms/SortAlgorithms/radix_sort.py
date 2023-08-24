def radix_sort(numbers):
    RADIX = 10
    placement = 1
    max_digit = max(numbers)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in numbers:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                numbers[a] = i
                a += 1
        placement *= RADIX
    return numbers


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for i in range(10)]
    print(radix_sort(nums))
    

# Path: practices/selection_sort.py

# Best case: O(n ^ 2)
# Worst case: O(n ^ 2)
# Average case: O(n ^ 2)
