#!/usr/bin/python3

def validUTF8(data):
    # Function to check if a byte is a valid leading byte in UTF-8
    def is_valid_start(byte):
        return bin(byte).startswith('0b' + '1' * (8 - num_bytes) + '0' * num_bytes)

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b0:
                continue  
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
