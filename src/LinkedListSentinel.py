'''
LINKED LIST' Algorithm with sentinel
Directly following the pseudocode from CLRS
'''


class ListElement:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.nil = ListElement(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    # LIST-INSERT'(L, x)
    # x.next = L.nil.next
    # L.nil.next.prev = x
    # L.nil.next = x
    # x.prev = L.nil

    def LIST_INSERT(self, x):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    # LIST-DELETE(L, x)
    # x.prev.next = x.next
    # x.next.prev = x.prev

    def LIST_DELETE(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    # LIST-SEARCH(L, k)
    # x = L.nil.next
    # while x != NIL and x.key != k
    #     x = x.next
    # return x

    def LIST_SEARCH(self, k):
        x = self.nil.next
        while x != None and x.key != k:
            x = x.next
        return x
