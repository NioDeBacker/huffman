#!/usr/bin/python3

import sys
from huffman import decode_bytestring_to_tables, decode_data, decode_data_with_table, decode_file

input_path = sys.argv[1]

output_path = sys.argv[2]

(data, trailing_ones, max_code_length) = decode_file(input_path)


(table, counter) = decode_bytestring_to_tables(data, max_code_length)

print(table)

data = data[counter:]

result = decode_data_with_table(data, table, trailing_ones)



print(f'result: {result}')

with open(output_path, 'w') as file_obj:
        file_obj.write(result)
