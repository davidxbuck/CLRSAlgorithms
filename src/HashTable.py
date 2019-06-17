'''
HASHTABLE Algorithm (with chaining)
Directly following the pseudocode from CLRS
'''

from math import floor, sqrt

from LinkedList import LinkedList, ListElement


class Underflow(Exception):
    pass


class HashTable:

    def __init__(self, m=59):
        self.T = [None] * m
        self.m = m
        self.A = (sqrt(5) - 1) / 2

    def h(self, key):
        return floor(self.m * ((key * self.A) % 1))

    # CHAINED-HASH-INSERT (T, key)
    # insert x at the head of list T[h(key)]

    def CHAINED_HASH_INSERT(self, k):
        x = ListElement(k)
        hash = self.h(x.key)
        if not isinstance(self.T[hash], LinkedList):
            self.T[hash] = LinkedList()
        self.T[hash].LIST_INSERT(x)

    # CHAINED-HASH-SEARCH(T, k)
    # search for an element with key k in T[h(k)]
    def CHAINED_HASH_SEARCH(self, k):
        hash = self.h(k)
        return self.T[hash].LIST_SEARCH(k) if isinstance(self.T[hash], LinkedList) else None

    # CHAINED-HASH-DELETE(T, x)
    # delete x from the list T[h(x.key)]
    def CHAINED_HASH_DELETE(self, x):
        if x.key != None:
            hash = self.h(x.key)
            self.T[hash].LIST_DELETE(x)
