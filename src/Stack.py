'''
STACK Algorithm
Directly following the pseudocode from CLRS
'''


class Underflow(Exception):
    pass


class Stack:

    def __init__(self, n=20):
        self.S = [None] * n
        self.top = 0
        self.n = n

    # PUSH(S, k) // O(1)
    # S[S.top] = k
    # S.top = S.top + 1
    # return

    def PUSH(self, k):
        if self.top >= self.n:
            self.STACK_OVERFLOW()
        self.S[self.top] = k
        self.top = self.top + 1

    # POP(S) // O(1)
    # if STACK-EMPTY
    #     error "Stack Underflow"
    # S.top = S.top - 1
    # return S[S.top + 1]

    def POP(self):
        print("Top", self.top)
        if self.STACK_EMPTY:
            print("Top", self.top)
            raise Underflow
        self.top = self.top - 1
        return self.S[self.top]

    # STACK-EMPTY(S) // O(1)
    # if S.top == -1
    #     return True
    # else
    #     return False

    @property
    def STACK_EMPTY(self):
        if self.top == 0:
            return True
        else:
            return False

    def STACK_OVERFLOW(self):
        self.S += [None] * self.n
        self.n += self.n
