#!/usr/bin/python3
"""Script will unlock list of lists
    by determining if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """This function will determine if boxes can be unlocked
        each box is numbered sequentially from 0 to n-1
        each boxx may contain keys to other boxes
        The first box (boxes[0]) is unlocked
            Args:boxes (list of lists)
            Returns:bool: True if all boxes can be unlocked, False otherwise.
    """

    keys = [0]
    for key in keys:
        # Iterate through each key in the current box
        for boxKey in boxes[key]:
            # If the key is new and within the valid range
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    # Check if the number of unlocked boxes matches the total number of boxes
    return len(keys) == len(boxes)
