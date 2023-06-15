from text_operator import read_dictionary, read_compressed_text, decode_text


def decompress_file(input_file, output_file):
    # Dekompresuje plik skompresowany przy użyciu algorytmu Huffmana.
    with open(input_file, 'rb') as file:
        dictionary = read_dictionary(file)
        bit_string = read_compressed_text(file)
        decompressed_text = decode_text(bit_string, dictionary)

    with open(output_file, 'w') as file:
        file.write(decompressed_text)
