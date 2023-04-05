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
    while len(nodes) > 1:
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

def bitstring_to_bytes(s):
    while len(s) % 8 != 0:
        s += '0'
    bitlist = list(map(''.join, zip(*[iter(s)]*8)))   
    bytess = bytearray([int(i,2) for i in bitlist])
    return bytess
def encode_file(data, codes, output_path):
    bit_string = ""
    for d in data:
        bit_string += codes[d]
    
    bytes_array = bitstring_to_bytes(bit_string)

    with open(output_path, 'wb') as file_obj:
        file_obj.write(bytes_array)


def tree_to_canonical_tree(tree):
    raise NotImplementedError

def decode_file(input_path):
    raise NotImplementedError

def bytes_to_tree(bytes_data):
    raise NotImplementedError

def decode_data(data, tree):
    raise NotImplementedError
