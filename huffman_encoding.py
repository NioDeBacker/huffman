#!/usr/bin/python3

import sys

input_path = sys.argv[0]

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
    sorted_nodes = sorted(nodes)
    while len(sorted_nodes > 1):
        # get two nodes with lowest probability
        min_node_1 = sorted_nodes[0]
        min_node_2 = sorted_nodes[1]

        root_node = Node(min_node_1.prob + min_node_2.prob, '', min_node_1, min_node_2)

        sorted_nodes.remove(min_node_1)
        sorted_nodes.remove(min_node_2)
        sorted_nodes.append(root_node)
        sorted_nodes = sorted(sorted_nodes)
    return sorted_nodes[0]

def write_encoded(data, output_path):
    print("Writing to file...") 
