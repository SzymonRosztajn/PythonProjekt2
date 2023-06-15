from huffman_node import HuffmanNode
from min_heap import MinHeap


def build_huffman_tree(frequency):
    # Buduje drzewo Huffmana na podstawie częstotliowści znaków.
    heap = MinHeap()
    for char, freq in frequency.items():
        heap.push(HuffmanNode(char, freq))

    while not heap.is_empty():
        node1 = heap.pop()
        if heap.is_empty():
            return node1

        node2 = heap.pop()
        merged = HuffmanNode(None, node1.frequency + node2.frequency)
        merged.left = node1
        merged.right = node2
        heap.push(merged)
