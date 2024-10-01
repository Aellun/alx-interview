#!/usr/bin/python3
"""This function simulates a game where players take turns
choosing a number n, and the player who chooses the number
with the odd count of prime numbers wins."""


def isWinner(x, nums):
    """
    A function to determine who wins a game based on prime numbers.

    Args:
        x (int): Number of rounds played.
        nums (list): List of integers(max value of n for each round).

    Returns:
        str:    "Maria" if Maria wins,
                "Ben" if Ben wins,
                None if it's a tie.
    """

    def sieve_of_eratosthenes(max_n):
        """
        Generate all prime numbers up to max_n
        using the Sieve of Eratosthenes algorithm.

        Args:
            max_n (int): max value up to which prime numbers
            should be generated.

        Returns:
            list: Boolean array rep primality status of numbers
            from 0 to max_n.
        """
        count_prime = [True] * (max_n + 1)
        count_prime[0] = count_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if count_prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    count_prime[multiple] = False
        return count_prime

    # Find the maximum value of n
    max_n = max(nums)

    # Get prime numbers up to the largest n
    primes = sieve_of_eratosthenes(max_n)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        prime_count = sum(primes[2:n+1])

        # If prime_count is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
