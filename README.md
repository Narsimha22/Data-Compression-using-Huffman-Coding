# Data-Compression-using-Huffman-Coding
This is a code to compress a text file into a binary file using Huffman Coding algorithm.

The Huffman Coding is a lossless data compression algorithm, developed by David Huffman in the early of 50s while he was a PhD student at MIT. The algorithm is based on a binary-tree frequency-sorting method that allow encode any message sequence into shorter encoded messages and a method to reassemble into the original message without losing any data.

The algorithm is based on the frequency of occurrence of the data item(byte). The most frequent data items will be represented and encoded with a lower number of bits.
The main idea of the algorithm is create a binary tree, called Huffman tree, based on the bytes frequency on the data, where the leafs are the bytes symbols, and the path from the root to a leaf determines the new representation of that leaf byte.

This code is complete implementation of huffman coding compression and decompression with comments to get a clear idea about the code.
**Use forward slash in the path of the file**
