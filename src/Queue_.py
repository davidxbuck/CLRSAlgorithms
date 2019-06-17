'''
QUEUE Algorithm
Directly following the pseudocode from CLRS
'''


class Underflow(Exception):
    pass


class Queue:

    def __init__(self, n=20):
        self.Q = [None] * n
        self.top = 0
        self.length = n
        self.tail = self.head = 0

    # ENQUEUE(Q, x)
    # if Q.tail + 1 == Q.head or (Q.tail == Q.length and Q.head == 1)
    #     error
    #     "Overflow"
    # else
    #     Q[Q.tail] = x
    #     if Q.tail == Q.length
    #         Q.tail = 1
    #     else
    #         Q.tail = Q.tail + 1
    # return
    def ENQUEUE(self, x):
        if self.tail + 1 == self.head or (self.tail == self.length - 1 and self.head == 0):
            raise OverflowError
        else:
            self.Q[self.tail] = x
            if self.tail == self.length - 1:
                self.tail = 0
            else:
                self.tail = self.tail + 1

    # DEQUEUE(Q)
    # if Q.tail = Q.head
    #     error "Underflow"
    #
    # else
    #     x = Q[Q.head]
    #     if Q.head == Q.length
    #         Q.head = 1
    #     else
    #         Q.head = Q.head + 1
    # return x

    def DEQUEUE(self):
        if self.tail == self.head:
            raise Underflow
        else:
            x = self.Q[self.head]
            if self.head == self.length - 1:
                self.head = 0
            else:
                self.head = self.head + 1
        return x
