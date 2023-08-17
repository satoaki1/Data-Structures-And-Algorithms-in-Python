import random

def linear_search(numbers, target):
  result = 0
  for i in range(len(numbers)):
    if numbers[i] == target:
      result = target  
  return target


if __name__ == "__main__":
  numbers = [random.randint(0, 1000) for _ in range(1000)]
  target = int(input())

  if linear_search(numbers, target) == target:
    print(target)
  else:
    print("The result is not found with the searched item.")
