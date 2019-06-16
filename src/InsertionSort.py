'''
INSERTION SORT Algorithm
Directly following the pseudocode from CLRS
'''


class Array:

    def __init__(self, values=[]):
        self.A = values

    def alen(self):
        return len(self.A)

    length = property(alen)

    # INSERTION-SORT(A)
    # for j = 2 to A.length
    #     key = A[j]
    #     // Insert A[j] into sorted sequence A[1... j-1]
    #     i = j - 1
    #     while i > 0 and A[i] > key
    #         A[i+1] = A[i]
    #         i = i-1
    #     A[i-1] = key

    def INSERTION_SORT(self):
        for j in range(2, self.length):
            key = self.A[j]
            # Insert self.A[j] into sorted sequence self.A[1... j-1]
            i = j - 1
            while i >= 0 and self.A[i] > key:  # reverse the second condition for descending sequence
                self.A[i + 1] = self.A[i]
                i = i - 1
            self.A[i + 1] = key
        return self.A
