#!/usr/bin/python3
def canUnlockAll(boxes):
    # Total number of boxes
    n = len(boxes)
    unlocked = set([0])
    # Initialize the queue with the first box
    queue = [0]

    # run until there are no more boxes to process
    while queue:
        current_box = queue.pop(0)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # Check if the key opens a new box within the valid range
            if key not in unlocked and key < n:
                unlocked.add(key)
                queue.append(key)

    # Return True if all boxes are unlocked, otherwise False
    return len(unlocked) == n
