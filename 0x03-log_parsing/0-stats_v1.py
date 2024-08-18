#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics
    After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear or is not an integer,
            don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
'''
import sys


def print_msg(dict_sc, total_file_size):
    '''
    Print the statistics of the processed data:
        - Total file size
        - Number of occurrences for each status code

    Args:
        dict_sc (dict): Dictionary with status codes
        as keys and counts as values.
        total_file_size (int): The total size of all processed files.
    '''
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables
total_file_size = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0
           }

try:
    for line in sys.stdin:
        # Split the line into components and reverse it
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                try:
                    file_size = int(parsed_line[0])
                except ValueError:
                    continue

                status_code = parsed_line[1]

                if status_code in dict_sc:
                    dict_sc[status_code] += 1

            if counter == 10:
                # Print statistics after every 10 lines
                print_msg(dict_sc, total_file_size)
                counter = 0
finally:
    # Print final statistics when processing is complete
    print_msg(dict_sc, total_file_size)
