'''
LINKED LIST Algorithm
Directly following the pseudocode from CLRS
'''


class ListElement:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None

    # LIST-INSERT(L, x)
    # x.next = L.head
    # if L.head != NIL
    #     L.head.prev = x
    # L.head = x
    # x.prev = NIL

    def LIST_INSERT(self, x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    # LIST-DELETE(L, x)
    # if x.prev != NIL
    #     x.prev.next = x.next
    # else
    #     L.head = x.next
    # if x.next != NIL
    #     x.next.prev = x.prev

    def LIST_DELETE(self, x):
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

    # LIST-SEARCH(L, k)
    # x = L.head
    # while x != NIL and x.key != k
    #     x = x.next
    # return x

    def LIST_SEARCH(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x
