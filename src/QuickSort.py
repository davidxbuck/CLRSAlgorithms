'''
QUICKSORT Algorithm
Directly following the pseudocode from CLRS
'''


class Array:

    def __init__(self, values=[]):
        self.A = values

    # QUICKSORT(A, p, r)
    # 1 if p < r
    # 2     q = PARTITION(A, p, r)
    # 3     QUICKSORT(A, p, q-1)
    # 4     QUICKSORT(A, q+1, r)

    def QUICKSORT(self, p, r):
        if p < r:
            q = self.PARTITION(p, r)
            self.QUICKSORT(p, q - 1)
            self.QUICKSORT(q + 1, r)

    # PARTITION(A, p, r)
    # 1  v = A[r]
    # 2  i = p − 1
    # 3  for j = p to r − 1
    # 4        if A[j ] ≤ v
    # 5             i =i + 1
    # 6             exchange A[i] withA[j]
    # 7  exchange A[i + 1] with A[r]
    # 8  return i + 1

    def PARTITION(self, p, r):
        v = self.A[r]
        i = p - 1
        for j in range(p, r):
            if self.A[j] <= v:
                i += 1
                self.A[i], self.A[j] = self.A[j], self.A[i]
        self.A[i + 1], self.A[r] = self.A[r], self.A[i + 1]
        return i + 1
