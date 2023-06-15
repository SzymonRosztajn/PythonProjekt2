from compression import compress_file
from decompression import decompress_file


def main():
    # Funkcja main do kompresji plików
    input_file = "input.txt"
    compressed_file = "compressed.bin"
    decompressed_file = "decompressed.txt"

    # Kompresja pliku
    print("Kompresowanie pliku...")
    compress_file(input_file, compressed_file)
    print("Plik został skompresowany i zapisany jako", compressed_file)

    # Dekompresja pliku
    print("Dekompresowanie pliku...")
    decompress_file(compressed_file, decompressed_file)
    print("Plik został zdekompresowany i zapisany jako", decompressed_file)


if __name__ == "__main__":
    main()
