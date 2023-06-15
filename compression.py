from counter import count_frequency
from huffman_tree import build_huffman_tree
from text_operator import build_huffman_codes, write_dictionary, write_compressed_text


def compress_file(input_file, output_file):
    # Kompresuje plik wejściowy przy użyciu algorytmu Huffmana.
    with open(input_file, 'r') as file:
        text = file.read()

    frequency = count_frequency(text)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, '', huffman_codes)

    with open(output_file, 'wb') as file:
        write_dictionary(file, huffman_codes)
        write_compressed_text(file, text, huffman_codes)
