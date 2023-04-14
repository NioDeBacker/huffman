# Huffman

This is an implementation of the Huffman code using Python. Using *huffman_encoding.py* and *huffman_decoding.py* users can compress and decompress (text)files.

## What is the Huffman Code

In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.

Basically a Huffman code is a binary code that represents a certain character. The special thing about the Huffan code is that characters frequently appearing in the file get represented by shorter codes and less frequent characters by longer codes.

For example if we have a file with contents "AAABBC" the Huffman code table would be something like  ```1: A, 01: B, 00: C```. The encoding of the file would be ```111010100```. 

This code is often represented by a *binary tree* with each '0' representing a right child and each '1' a left child. The leafs of the tree contain the different symbols. This tree can be used to decode the file.

It is mathematically proven that a well constructed Huffman encode results in about a little more than a 2/1 compress rate.

### Canonical Huffman Code

A lot of examples on the internet of the Huffman Code work in a single file where the code table or tree constructed in the encoding can be passed as a variable to the decoding function. In a practial sense this is impossible because we need a way to store the table or code aswell. Saving this as plain objects would nullify all compression gained and would be programming language depended aswell. Therefore for practical effecient compression we can transform our code to a *Canonical Huffman Code*. The main requirement is that our symbols that we are encoding are sortable. The canonical code is based of a normal huffman code sorted by code length, symbol. It has three properties.

- The first/shortest code is equal in length to its normal code but all "0"s
- Subsequent codes are equal to the previous code but + 1
- If this resulting code is shorter than the original code "0"s are appended

### Implementation

If all symbols are known beforehand, using the canonical encoding, the bitlenghts of each symbol's Canonical code can be appended and the Canonical Huffman code can be reconstructed with only this information.

This implementation offers the flexibility for unknown symbols. The code is encoded as (#of symbols with code length 1, #of symbols with code length 2, ...) (symbol 1, symbol 2, symbol 3, ...) and the Canonical Code is reconstructed this way. 

Since python can only write bytes to files and not bits "0"s are appended at the end of the encoding. To know when this "0"s are reached a byte containing the number of "0"s is prepended to the encoding. Similarly a byte is added containing the largest code length. Between the last symbol and the start of the encoding a "11111111" byte is added to signal the start of the encoding.

## Usage

### encoding files

``` ./huffman_encoding.py [input_path][output_path] ```

### decoding files

``` ./huffman_decoding.py [input_path] [output_path] ```
