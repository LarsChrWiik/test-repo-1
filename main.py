def digit_sum(n):
    """Calculate the sum of digits in a number."""
    return sum(int(digit) for digit in str(n))

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_filtered_primes(count):
    """
    Generate a list of primes with two constraints:
    1. Total primes generated is equal to the count
    2. Excludes primes whose digit sum is 5
    """
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num) and digit_sum(num) != 5:
            primes.append(num)
        num += 1
    return primes

def main():
    """Print the first 1000 prime numbers (excluding those with digit sum of 5)."""
    first_1000_primes = get_filtered_primes(1000)
    print("The first 1000 prime numbers (excluding those with digit sum of 5):")
    for prime in first_1000_primes:
        print(prime)

if __name__ == "__main__":
    main()
