def sieve_of_eratosthenes(min_val, max_val):

    primes = [True] * (max_val + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_val**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_val + 1, i):
                primes[j] = False

    return [i for i in range(min_val, max_val + 1) if primes[i]]


if __name__ == '__main__':
    print(*sieve_of_eratosthenes(10, 20))
