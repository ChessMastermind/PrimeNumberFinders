def is_prime(n,primes):
    if n < 2:
        return False
    for i in primes:
        if n % i == 0:
            return False
    return True

def generate_primes(limit, file_path):
    primes = [2,3]
    num = 3
    while len(primes) < limit:
        if is_prime(num,primes):
            primes.append(num)
        num += 1

    with open(file_path, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")

if __name__ == "__main__":
    file_path = "1_million_primes.txt"  # Output file
    limit = 1000  # Number of primes to generate

    print(f"Generating {limit} prime numbers...")
    generate_primes(limit, file_path)
    print(f"Prime numbers saved to {file_path}.")