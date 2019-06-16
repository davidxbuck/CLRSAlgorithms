from LinkedList import LinkedList, ListElement


def test_list():
    L = LinkedList()
    assert L.head == None


def test_list_element():
    x = ListElement(0)
    assert x.key == 0
    assert x.next == None
    assert x.prev == None


def test_list_insert():
    L = LinkedList()
    x = ListElement(0)
    assert L.head == None
    L.LIST_INSERT(x)
    assert x.next == None
    assert L.head == x
    assert x.prev == None


def test_list_insert2():
    L = LinkedList()
    x = ListElement(0)
    assert L.head == None
    L.LIST_INSERT(x)
    assert x.next == None
    assert L.head == x
    assert x.prev == None
    y = x
    x = ListElement(1)
    L.LIST_INSERT(x)
    assert x.next == y
    assert L.head == x
    assert x.prev == None
    assert L.head.next == y
    assert L.head.next.prev == x


def test_list_insert3():
    L = LinkedList()
    x = ListElement(20)
    assert L.head == None
    L.LIST_INSERT(x)
    assert x.next == None
    assert L.head == x
    assert x.prev == None
    y = x
    for i in range(10):
        x = ListElement(i)
        L.LIST_INSERT(x)
    assert L.head == x
    assert x.prev == None
    assert L.head.next.next.next.next.next.next.next.next.next.next == y
    assert y.prev.key == 0
    assert y.prev.prev.key == 1
    z = L.head
    for i in range(10):
        assert z.key == 9 - i
        z = z.next
    assert z.key == 20
    z = z.prev
    for i in range(10):
        assert z.key == i
        z = z.prev


def test_delete():
    L = LinkedList()
    x = ListElement(0)
    L.LIST_INSERT(x)
    y = ListElement(1)
    L.LIST_INSERT(y)
    z = ListElement(2)
    L.LIST_INSERT(z)
    assert z.next == y
    assert y.prev == z
    assert y.next == x
    assert x.prev == y
    L.LIST_DELETE(y)
    assert z.next == x
    assert x.prev == z


def test_insertanddelete():
    L = LinkedList()
    x = ListElement(0)
    L.LIST_INSERT(x)
    L.LIST_DELETE(x)
    assert L.head == None


def test_insertanddelete100fromhead():
    L = LinkedList()
    for i in range(100):
        x = ListElement(i)
        L.LIST_INSERT(x)
    for i in range(100):
        assert L.head.key == 99 - i
        L.LIST_DELETE(L.head)
    assert L.head == None


def test_insertanddelete100fromtail():
    L = LinkedList()
    z = ListElement(0)
    L.LIST_INSERT(z)
    for i in range(1, 100):
        x = ListElement(i)
        L.LIST_INSERT(x)
    for i in range(100):
        assert z.key == i
        L.LIST_DELETE(z)
        z = z.prev
    assert L.head == None


def test_list_search():
    L = LinkedList()
    for i in range(0, 100):
        x = ListElement(i)
        L.LIST_INSERT(x)
    x = L.LIST_SEARCH(50)
    assert x.prev.key == 51
    assert x.key == 50
    assert x.next.key == 49
