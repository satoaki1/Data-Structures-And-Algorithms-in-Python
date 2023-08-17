def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Pushed item: " + str(item))

def pop(stack):
    if (is_empty(stack)):
        return "stack is empty"

    return stack.pop()

def sort_stack(stack):
    size = len(stack)
    for i in range(size):
        for j in range(size - i - 1):
            if stack[j] > stack[j + 1]:
                stack[j], stack[j + 1] = stack[j + 1], stack[j]

    return stack


if __name__ == "__main__":
    import random
    
    stack = create_stack()
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))
    push(stack, random.randint(0, 10))

    print(stack)
    print(sort_stack(stack))
    
