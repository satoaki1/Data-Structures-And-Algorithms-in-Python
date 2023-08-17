import random

def bubble_sort(numbers, size):
  for step in range(size):
    for i in range(size - step - 1):
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

  return numbers


if __name__ == "__main__":
  numbers = [random.randint(0, 1000) for _ in range(5)]
  size = len(numbers)
  print(bubble_sort(numbers, size))
