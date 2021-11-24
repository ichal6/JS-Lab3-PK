def fibonacci_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, b+a
    return a
    
def fibonacci_r(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_r(n-1) + fibonacci_r(n - 2))