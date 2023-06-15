class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        # Porównanie dwóch węzłów Huffmana na podstawie ich częstotliwości.
        return self.frequency < other.frequency
