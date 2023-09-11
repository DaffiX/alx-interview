#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        primes = []

        for p in range(2, int(n**0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False

        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)

        return primes

    def can_win(n, primes):
        # Create a list of primes up to n
        primes = sieve_of_eratosthenes(n)

        # Calculate the cumulative sum of prime counts
        prime_count = [0] * (n + 1)
        total = 0
        for i in range(2, n + 1):
            if i in primes:
                total += 1
            prime_count[i] = total

        # Check if Maria or Ben can win with the given n
        if prime_count[n] % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = can_win(n, [])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
