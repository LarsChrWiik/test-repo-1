def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_first_n_primes(n):
    """Generate the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def fibonacci(n):
    """Recursive Fibonacci function."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    """Print the first 100 prime numbers and first 10 Fibonacci numbers."""
    # Print prime numbers
    first_100_primes = get_first_n_primes(100)
    print("The first 100 prime numbers are:")
    for prime in first_100_primes:
        print(prime, end=" ")
    print("\n")

    # Print first 10 Fibonacci numbers
    print("The first 10 Fibonacci numbers are:")
    for i in range(10):
        print(fibonacci(i), end=" ")
    print()

if __name__ == "__main__":
    main()