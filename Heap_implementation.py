from _heapq import heappop
import random


class Heap:
    def __init__(self):
        self.heap_array = []
        self.current_size = []

    def percolate_up(self, i):
        while i > 0:  # parents nodes index
            parent = (i - 1) // 2
            if self.heap_array[i] < self.heap_array[parent]:  # Checks there's no violation in min_heap
                print("   percolate up() swap: %d for %d \n" % (self.heap_array[i], self.heap_array[parent]))  # swap
                tmp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[parent]
                self.heap_array[parent] = tmp
            # loop i on parents node
            i = parent

    def insert(self, k):
        self.heap_array.append(k)

        self.percolate_up(len(self.heap_array) - 1)  # ​​TODO: Complete implementation

    def extract_min(self):
        return heappop(self.heap_array)

    def is_empty(self):
        return len(self.heap_array) == 0


h = Heap()
print(h.current_size)
for r in range(random.randint(1, 10)):  # generate random ints
    for item in range(random.randrange(0, 5, 2)):  # generate a random range
        h.insert(item)
        print('   --> array: %s\n' % h.heap_array)

print('   --> Extracted value: %d  ' % h.extract_min())
print('   --> original array: %s' % h.heap_array)
