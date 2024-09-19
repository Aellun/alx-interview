#!/usr/bin/python3
'''Calculate the fewest number of coins
needed to meet a given total'''


def makeChange(coins, total):
    '''
    Parameters:
    coins (list): A list of coin denominations
    available (positive integers).
    total (int): The target amount to achieve.

    Returns:
    int: The min number of coins needed to make the total,
         or -1 if the total cannot be met.
    '''
    # Returns 0 if total is 0 or less
    if total <= 0:
        return 0

    # Initializes a list to store the min coins for each amount
    bc = [float('inf')] * (total + 1)

    # Base case: No coins are needed to make the total 0
    bc[0] = 0

    # Iterate through each coin
    for coin in coins:
        # Update the bc array for each amount from coin to total
        for amount in range(coin, total + 1):
            bc[amount] = min(bc[amount], bc[amount - coin] + 1)

    # If bc[total] is still inf, it means we cannot make the total
    return bc[total] if bc[total] != float('inf') else -1
