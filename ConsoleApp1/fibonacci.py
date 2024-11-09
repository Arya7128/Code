def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    n = 10  # Get first 10 Fibonacci numbers
    results = list(fibonacci(n))
    print("Fibonacci sequence:", results)

if __name__ == "__main__":
    main()
