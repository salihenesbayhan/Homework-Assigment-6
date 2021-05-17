import math

# returns True if n is prime number
#    returns False otherwise
def is_prime(n):

        # n is less than 2
    if n < 2:
        return False

    # compute square root + 1
    sq = int(math.sqrt(n)) + 1

    # check if divisible by any other number
    for i in range(2, sq):
        if n % i == 0:
            return False

    return True


# returns a list of the first 20 primes
def primes_list():
        p = []
        i = 2
        while len(p) < 20:
                if is_prime(i):
                        p.append(i)
                i += 1  # increment i
        return p

# returns the list of first 19 fake primes
def fake_primes_list(primes):
        fake_primes = []
        for i in range(len(primes) - 1):
                fake_primes.append(primes[i] * primes[i + 1])
        return fake_primes


def fakePrimes():
        print("done")
        primes = primes_list()
        fake_primes = fake_primes_list(primes)
        for i in range(len(primes) - 1):
                print(f'Fake prime in position { i + 1 } is { fake_primes[i] }. It is generated using { primes[i] } and { primes[i + 1] }.')

fakePrimes()