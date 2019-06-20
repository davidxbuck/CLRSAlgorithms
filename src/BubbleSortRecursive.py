'''
BUBBLESORT Algorithm with recursion
NOT directly following pseudocode from CLRS
Uses recursion rather than nested for loops
'''


class Array:

    def __init__(self, values=[]):
        self.A = values

    @property
    def length(self):
        return len(self.A)

    # BUBBLESORT(A)
    # for i = 1 to A.length - 1
    #     for j = A.length down to i + 1
    #         if A[j] < A[j - 1]
    #         exchange A[j] with A[j - 1]

    def BUBBLESORT(self, i=0):
        if i < self.length - 1:
            for j in range(self.length - 1, i, -1):
                if self.A[j] < self.A[j - 1]:
                    self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
            self.BUBBLESORT(i + 1)
