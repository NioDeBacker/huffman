#!/usr/bin/python3

import sys
from huffman import decode_bytestring_to_tables, decode_data, decode_data_with_table, decode_file

input_path = sys.argv[1]

output_path = sys.argv[2]

data = decode_file(input_path)

print(data)

(table, counter) = decode_bytestring_to_tables(data)

print(table)
print(counter)

data = data[counter:]

result = decode_data_with_table(data, table)


print(f'result: {result}')





# printTree(tree)
# result_parsed = decode_data(result, tree)
# print(result_parsed)