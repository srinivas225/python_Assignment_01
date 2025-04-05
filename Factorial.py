number = int(input("Enter a number"))


def factorial(number):
    if number == 0:
        return 1
    else:

        return number * factorial(number - 1)


result = factorial(5)


print(f"Factorial of {number} is {result}")

