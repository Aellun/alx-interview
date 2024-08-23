#!/usr/bin/python3
'''
Determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    Args:
        data (list[int]): A list of integers representing bytes of data.
            Each integer is in the range 0-255.
    Returns:boolean
    '''
    # The number of expected continuation bytes for the current character
    expected_continuation_bytes = 0

    # Bit masks for checking the most significant bits of a byte
    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    # Iterate over each byte in the input data
    for byte in data:
        # Mask to check for leading 1's in the current byte
        leading_one_mask = 1 << 7

        if expected_continuation_bytes == 0:
            # Determine the number of leading 1's to figure out how many
            # continuation bytes are expected
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask >>= 1

            # If no leading 1's were found, this is a single-byte character
            if expected_continuation_bytes == 0:
                continue

            # If the number of leading 1's is 1 or more than 4, it's invalid
            if (expected_continuation_bytes == 1 or
                    expected_continuation_bytes > 4):
                return False

        else:
            # For continuation bytes, the first bit must be 1
            # and the second bit must be 0
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # Decrement the number of expected continuation bytes
        expected_continuation_bytes -= 1

    # Return True if all bytes were processed correctly
    # and no continuation bytes are left
    return expected_continuation_bytes == 0
