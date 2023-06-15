def count_frequency(text):
    # Zlicza częstość występowania znaków w tekście.
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
