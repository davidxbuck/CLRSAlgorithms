'''
MERGE SORT Algorithm
Directly following the pseudocode from CLRS
'''

from math import floor

from numpy import inf


class Array:

    def __init__(self, values=[]):
        self.A = values

    # MERGE(A, p, q, r)
    # n1 = q - p + 1
    # n2 = r - q
    # let L[1 ... n1+1] and R[1 ... n2+1] be new arrays
    # for i = 1 to n1
    #     L[i] = A[p + i - 1]
    # for j = 1 to n2
    #     R[j] = A[q + j]
    # L[n1 + 1] = ꚙ
    # R[n2 + 1] = ꚙ
    # i = 1
    # j = 1
    # for k = p to r
    #     if L[i] <= R[j]
    #         A[k] = L[i]
    #         i = i + 1
    #     else
    #         A[k] = R[j]
    #         j = j + 1

    # Adjusted to account for Python 0 indexing

    def MERGE(self, p, q, r):
        print("Merge called on ranges {}-{} and {}-{}".format(p, q - 1, q, r))
        L = self.A[p:q] + [inf]  # the first 11 lines of the pseudocode
        R = self.A[q:r + 1] + [inf]  # can be written in 3 lines of Python

        i = j = 0  #
        for k in range(p, r + 1):
            if L[i] <= R[j]:
                self.A[k] = L[i]
                i += 1
            else:
                self.A[k] = R[j]
                j += 1

    # MERGE-SORT(A, p, r)
    # if p < r
    #     q = └ (p + r) / 2 ┘
    #     MERGE-SORT(A, p, q)
    #     MERGE-SORT(A, q+1, r)
    #     MERGE(A, p, q, r)
    #
    def MERGE_SORT(self, p, r):
        print("Merge_sort called from {} to {}".format(p, r))
        if p < r:
            q = floor((p + r + 1) / 2)
            print("Splits are {}-{} and {}-{}".format(p, q - 1, q, r))
            print("Pre-merge {} and {}".format(self.A[p:q], self.A[q:r + 1]))
            self.MERGE_SORT(p, q - 1)
            self.MERGE_SORT(q, r)
            print("Post sub-sort {} and {}".format(self.A[p:q], self.A[q:r + 1]))
            self.MERGE(p, q, r)
            print("Post-merge {}".format(self.A))
            print("")
