def build_huffman_codes(node, code, huffman_codes):
    # Rekurencyjnie buduje kody Huffmana dla znaków na podstawie drzewa Huffmana.
    if node.char:
        huffman_codes[node.char] = code
        return

    build_huffman_codes(node.left, code + '0', huffman_codes)
    build_huffman_codes(node.right, code + '1', huffman_codes)


def write_dictionary(file, huffman_codes):
    # Zapisuje słownik kodów Huffmana do pliku.
    dictionary = str(huffman_codes)
    file.write(dictionary.encode('ascii') + b'\n')


def write_compressed_text(file, text, huffman_codes):
    # Zapisuje skompresowany tekst do pliku.
    compressed_text = ''.join(huffman_codes[char] for char in text)
    padding_length = 8 - (len(compressed_text) % 8)
    compressed_text += '0' * padding_length
    binary_data = bytearray(int(compressed_text[i:i + 8], 2) for i in range(0, len(compressed_text), 8))
    file.write(bytes(binary_data))


def read_dictionary(file):
    # Odczytuje słownik kodów Huffmana z pliku.
    dictionary = eval(file.readline().decode('ascii'))
    return dictionary


def read_compressed_text(file):
    # Odczytuje skompresowany tekst z pliku.
    binary_data = file.read()
    bit_string = ''.join(format(byte, '08b') for byte in binary_data)
    padding_length = bit_string[-8:].count('0')
    bit_string = bit_string[:-padding_length]
    return bit_string


def decode_text(bit_string, dictionary):
    # Odkodowuje skompresowaną sekwencję bitów na podstawie słownika kodów Huffmana.
    inverse_dictionary = {code: char for char, code in dictionary.items()}
    decompressed_text = ''
    current_code = ''
    for bit in bit_string:
        current_code += bit
        if current_code in inverse_dictionary:
            char = inverse_dictionary[current_code]
            decompressed_text += char
            current_code = ''
    return decompressed_text
