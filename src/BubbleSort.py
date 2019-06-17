'''
BUBBLESORT Algorithm
Directly following the pseudocode from CLRS
'''


class Array:

    def __init__(self, values=[]):
        self.A = values

    def alen(self):
        return len(self.A)

    length = property(alen)

    # BUBBLESORT(A)
    # for i = 1 to A.length - 1
    #     for j = A.length down to i + 1
    #         if A[j] < A[j - 1]
    #         exchange A[j] with A[j - 1]

    def BUBBLESORT(self):
        for i in range(0, self.length - 1):
            for j in range(self.length - 1, i, -1):
                if self.A[j] < self.A[j - 1]:
                    self.A[j], self.A[j - 1] = self.A[j - 1], self.A[j]
