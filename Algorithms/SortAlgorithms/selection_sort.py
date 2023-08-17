import random

def selection_sort(numbers, size):
  for i in range(size):
    minimum_index = i
    for j in range(i + 1, size):
      if numbers[minimum_index] > numbers[j]:
        minimum_index = j
    numbers[i], numbers[minimum_index] = numbers[minimum_index], numbers[i]
  return numbers


if __name__ == "__main__":
  numbers = [random.randint(0, 1000) for _ in range(10)]
  size = len(numbers)
  print(selection_sort(numbers))
