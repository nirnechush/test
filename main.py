def fibonacci_series(n):
    """Generate a Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
if __name__ == "__main__":
    terms = int(input("Enter the number of terms: "))
    print("Fibonacci Series:", fibonacci_series(terms))