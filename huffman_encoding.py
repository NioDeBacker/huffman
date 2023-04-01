#!/usr/bin/python3

class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        
        # probability
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right
        
        # tree direction (0 or 1)
        self.code = ''

    # make nodes sortable (by probability)
    def __lt__(self, other):
        return self.prob < other.prob
    
# returns a dictionary with the probability for each symbol
def calculate_probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


# a list of nodes merged together untill there is a tree, returns the root node
def create_tree(nodes):
    while len(nodes > 1):
        nodes = sorted(nodes, key=lambda x: x.prob)
        # get two nodes with lowest probability
        right_node = nodes[0]
        left_node = nodes[1]

        right_node.code = 1
        left_node.code = 0

        # merge them under one parent node
        parent_node = Node(right_node.prob + left_node.prob, '', right_node, left_node)

        nodes.remove(right_node)
        nodes.remove(left_node)
        nodes.append(parent_node)
    return nodes[0]


def calculate_code(node, value=''):
    new_value = value + str(node.code)
    
    if(node.left):
        calculate_code(node.left, new_value)
    if(node.right):
        calculate_code(node.right, new_value)

    if(not node.left and not node.right):
        codes[node.symbol] = new_value
    
    return codes
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def encode_file(data, codes, output_path):
    bit_string = ""
    for d in data:
        bit_string += codes[d]
    
    bytes_array = bitstring_to_bytes(bit_string)

    with open(output_path, 'wb') as file_obj:
        file_obj.write(bytes_array)


import sys

input_path = sys.argv[0]

output_path = sys.argv[0]

codes = dict()

with open(input_path, 'r') as file:
    data = file.read()

probabilities = calculate_probability(data)

# create an array with nodes

# calculate codes

# encode file
