'''
HEAPSORT Algorithm
Directly following the pseudocode from CLRS
'''

from math import floor


#
# Because Python indexing starts from 0, not 1, the values of :LEFT, RIGHT and PARENT need to be modified according.y
#         0
#      1     2
#     3 4   5 6
#
#

class Heap:

    def __init__(self, values=[]):
        self.A = values
        self.heap_size = self.length

    @property
    def length(self):
        return len(self.A)

    # PARENT(A, i)
    #   return ⌊i/2⌋

    def PARENT(self, i):
        return floor((i - 1) / 2)

    # LEFT(A, i)
    #   return ⌊2i⌋

    def LEFT(self, i):
        return 2 * i + 1

    # RIGHT(A, i)
    #   return ⌊2i + 1⌋

    def RIGHT(self, i):
        return 2 * i + 2

    # HEAPSORT(A)
    #   BUILD-MAX-HEAP(A)
    #   for i = A.length downto 2
    #     exchange A[1] with A[i]
    #     A.heap-size = A.heap-size - 1
    #     MAX-HEAPIFY(A, 1)

    def HEAPSORT(self):
        self.BUILD_MAX_HEAP()
        for i in range(self.length - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.MAX_HEAPIFY(0)

    def MIN_HEAPSORT(self):
        self.BUILD_MIN_HEAP()
        for i in range(self.length - 1, 0, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.MIN_HEAPIFY(0)

    # BUILD-MAX-HEAP(A)
    #   A.heap-size = A.length
    #   for i = ⌊A.length/2⌋ downto 1
    #      MAX-HEAPIFY(A, i)

    def BUILD_MAX_HEAP(self):
        self.heap_size = self.length
        for i in range(floor((self.length - 2) / 2), -1, -1):
            self.MAX_HEAPIFY(i)

    def BUILD_MIN_HEAP(self):
        self.heap_size = self.length
        for i in range(floor((self.length - 2) / 2), -1, -1):
            self.MIN_HEAPIFY(i)

    # MAX-HEAPIFY(A, i)
    # l = LEFT(i)
    # r = RIGHT(i)
    # if l <= A.heap-size and A[l] > A[i]
    #     largest = l
    # else
    #     largest = i
    # if r <= A.heap-size and A[r] > A[largest]
    #     largest = r
    # if largest != i
    #     exchange
    #     A[i]
    #     with A[largest]
    #         MAX-HEAPIFY(A, largest)

    def MAX_HEAPIFY(self, i):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.MAX_HEAPIFY(largest)

    def MIN_HEAPIFY(self, i):
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heap_size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.A[r] < self.A[smallest]:
            smallest = r
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.MIN_HEAPIFY(smallest)
