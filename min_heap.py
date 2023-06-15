import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        # Dodaje element do stosu minimalnego.
        heapq.heappush(self.heap, item)

    def pop(self):
        # Usuwa i zwraca najmniejszy element ze stosu minimalnego.
        return heapq.heappop(self.heap)

    def is_empty(self):
        #  Sprawdza, czy stos minimalny jest pusty.
        return len(self.heap) == 0
