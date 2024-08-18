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

# Dictionary to keep track of counts for each status code
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0
           }
total_file_size = 0
counter = 0

try:
    # Read lines from standard input
    for line in sys.stdin:
        # Split the line into components based on spaces
        line_list = line.split(" ")

        # Process lines with at least 5 components
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in dict_sc.keys():
                dict_sc[status_code] += 1

            total_file_size += file_size

            counter += 1

        # Print statistics after every 10 lines
        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_file_size))

            # Print counts for each status code,
            # only if count is greater than zero
            for key, value in sorted(dict_sc.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

# Ensure final statistics are printed upon completion or interruption
finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
