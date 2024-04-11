def calculate_factorial(n):
    if n == 1:
        return 1
    return calculate_factorial(n - 1) * n
 
 
print(calculate_factorial(6))
