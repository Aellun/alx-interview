#!/usr/bin/python3
'''Calculates the minimum number of operations needed to achieve
    exactly n H characters in the file, starting from a single H.

        Operations allowed:
        1. Copy All - Copies all characters in the file.
        2. Paste - Pastes the copied characters.

        Args:
        n (int): The desired number of H characters.

        Returns:
        int: The minimum number of operations needed to achieve
        exactly n H characters.
            Returns 0 if n is impossible to achieve (i.e., if n <= 1).
'''


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
