#!/usr/bin/python3
from huffman import binary_string_add_one, calculate_probability, canonical_huffman_codes, create_tree, Node, decode_data, encode_canonical_file, encode_file, encoding_to_bytestring
import sys

def calculate_code(node, value=''):
    new_value = value + str(node.code)
    
    if(node.left):
        calculate_code(node.left, new_value)
    if(node.right):
        calculate_code(node.right, new_value)

    if(not node.left and not node.right):
        codes[node.symbol] = new_value
    
    return codes
input_path = sys.argv[1]

output_path = sys.argv[2]

codes = dict()

# read file
with open(input_path, 'r') as file:
    data = file.read()

# calculate probabilities
probabilities = calculate_probability(data)

nodes = []

for key in probabilities:
    nodes.append(Node(probabilities[key], key))

# create tree
tree = create_tree(nodes)

# nice function for if we want to see the tree
def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.symbol))
        printTree(node.right, level + 1)


codes = probabilities

printTree(tree)

# calculate codes
codes_x = calculate_code(tree, '')

# calculate canonical codes
can_codes = canonical_huffman_codes(codes_x)

# encode table
can_code_string = encoding_to_bytestring(can_codes)

# write file
encode_canonical_file(data, can_codes, can_code_string, output_path)



