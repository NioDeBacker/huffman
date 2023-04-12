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

def encode_canonical_file(data, codes, encoded_codes, output_path):
    bit_string = ""

    codes_dict = dict()

    for code in codes:
        codes_dict[code.symbol] = code.code
    
    for d in data:
        bit_string += codes_dict[d]
    
    print(encoded_codes + bit_string)

    bytes_array = bitstring_to_bytes(encoded_codes + bit_string)

    with open(output_path, 'wb') as file_obj:
        file_obj.write(bytes_array)

def encode_file(data, codes, output_path):
    bit_string = ""
    for d in data:
        bit_string += codes[d]
    
    bytes_array = bitstring_to_bytes(bit_string)

    with open(output_path, 'wb') as file_obj:
        file_obj.write(bytes_array)

class CanonicalCode:

    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

    def __str__(self):
        return f'{self.symbol}: {self.code}'
    
    def __repr__(self):
        return f'{self.symbol}: {self.code}'

    def __lt__(self, other):
        return len(self.code) < len(other.code) if len(self.code) != len(other.code) else self.symbol < other.symbol

def binary_string_add_one(code):
    return bin(sum(int(x, 2) for x in [code, '1']))[2:]



def encoding_to_bytestring(codes):
    lengths = [0]*8

    bytestring = ""

    for code in codes:
        lengths[len(code.code)] += 1

    for length in lengths:
        byte = "{0:b}".format(length)
        byte = ('0' * (8 - len(byte))) + byte
        print(byte)
        bytestring += byte

    
    for code in codes:
        bytecode = f"{ord(code.symbol):08b}"
        bytestring += bytecode
    
    bytestring += ("1" * 8)
    return bytestring


def canonical_huffman_codes(codes):

    # sorting part
    canonical_codes = []
    for key in codes:
        canonical_codes.append(CanonicalCode(key, codes[key]))
    canonical_codes.sort()
    
    canonical_codes[0] = CanonicalCode(canonical_codes[0].symbol, len(canonical_codes[0].code) * "0" )

    # transforming part
    prev_code = canonical_codes[0].code
    for code in canonical_codes[1:]:
        new_code = binary_string_add_one(prev_code)
        len_diff = len(code.code) - len(new_code)
        new_code += ("0" * len_diff)
        code.code = new_code
        prev_code = new_code
    return canonical_codes
    

def decode_file(input_path):
    with open(input_path, mode='rb') as file:
        fileContent = file.read()

    data = ''.join(map('{:08b}'.format, fileContent))

    return data

def bytestring_to_frequencies(bytestring):
    freqencies = []
    for elem in range(0, 64, 8):
        freq = int(bytestring[elem:elem+8], 2)
        freqencies.append(freq)

    return freqencies
        

def decode_bytestring_to_tables(bytestring):
    
    counter = 8*8

    # get first eight
    freq = bytestring_to_frequencies(bytestring[:counter])
    
    # build codes
    len_counter = 0
    cur_code = '0'
    canonical_codes = dict()

    next_byte = bytestring[counter:counter+8]

    while next_byte != '11111111':
        print(freq)
        print(next_byte)
        print(canonical_codes)
        if freq[len_counter] > 0:
            freq[len_counter] -= 1
        else:
            len_counter += 1

        symbol = chr(int(next_byte, 2))

        code = cur_code
        len_diff = len_counter + 1 - len(code)
        code = cur_code + ('0' * len_diff)
        cur_code = binary_string_add_one(code)

        canonical_codes[code] = symbol

        counter += 8
        next_byte = bytestring[counter:counter+8]

    return (canonical_codes, counter) 

def decode_data_with_table(data, table):
    result = ''
    current_str = ''
    print(data)
    data = data[8:]
    print(data)
    for bit in data:
        current_str += bit
        print(f'current_str {current_str}, {"1" * 8}, {current_str == "1" * 8}')
        if current_str in table:
            result += table[current_str]
            current_str = ''
        

    return result

        

def decode_data(data, tree):
    result = ''
    current_node = tree
    for char in data:
        if char == '1':
            if current_node.left.symbol != '':
                result += current_node.left.symbol
                current_node = tree
            else:
                current_node = current_node.left
        elif char == '0':
            if current_node.right.symbol != '':
                result += current_node.right.symbol
                current_node = tree
            else:
                current_node = current_node.right
    return result
