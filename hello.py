def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)

number = 5
result = factoriel(number)
print(f"The factorial of {number} is {result}.")

