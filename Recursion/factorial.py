def factorial(num):
    if not isinstance(num , int) or num < 0:
        return "input must be a valid integer no"
    if num == 1 or num == 0:
        return 1

    return num * factorial(num - 1)


print(factorial(-5))

