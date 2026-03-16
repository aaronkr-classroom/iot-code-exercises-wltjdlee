# factorial.py
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print(factorial(5))

# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example
print(fibonacci(7))

# fibonacci-sequence.py
def fibonacci_sequence(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example
fibonacci_sequence(10)