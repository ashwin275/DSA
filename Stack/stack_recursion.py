def stack_recursion(stack, item):
    if not stack:
        stack.append(item)
    else:
        top_item = stack.pop()
        stack_recursion(stack, item)
        stack.append(top_item)


def stack_pop(stack):
    if not stack:
        return None
    elif len(stack) == 1:
        return stack.pop()
    else:
        top_item = stack.pop()
        result = stack_pop(stack)
        stack.append(top_item)
        return result


stack = []

stack_recursion(stack, 10)
stack_recursion(stack, 20)
stack_recursion(stack, 30)
print(stack)

print(stack_pop(stack))
print(stack)
