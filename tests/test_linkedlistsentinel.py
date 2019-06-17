from LinkedListSentinel import LinkedList, ListElement


def test_list():
    L = LinkedList()
    assert L.nil.next == L.nil
    assert L.nil.prev == L.nil


def test_list_element():
    x = ListElement(0)
    assert x.key == 0
    assert x.next == None
    assert x.prev == None


def test_list_insert():
    L = LinkedList()
    x = ListElement(0)
    L.LIST_INSERT(x)
    assert x.next == L.nil
    assert x.prev == L.nil


def test_list_insert2():
    L = LinkedList()
    x = ListElement(0)
    L.LIST_INSERT(x)
    assert x.next == L.nil
    assert x.prev == L.nil
    y = ListElement(1)
    L.LIST_INSERT(y)
    assert x.next == L.nil
    assert x.prev == y
    assert L.nil.next == y
    assert y.next == x
    assert y.prev == L.nil


def test_list_insert3():
    L = LinkedList()
    x = ListElement(20)
    L.LIST_INSERT(x)
    assert x.next == L.nil
    assert x.prev == L.nil
    for i in range(10):
        y = ListElement(i)
        L.LIST_INSERT(y)
    assert L.nil.next == y
    assert y.prev == L.nil
    assert L.nil.next.next.next.next.next.next.next.next.next.next.next == x
    assert L.nil.prev == x
    assert x.prev.key == 0
    assert x.prev.prev.key == 1
    z = L.nil.next
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
    assert L.nil.next == L.nil
    assert L.nil.prev == L.nil


def test_insertanddelete100fromhead():
    L = LinkedList()
    for i in range(100):
        x = ListElement(i)
        L.LIST_INSERT(x)
    for i in range(100):
        assert L.nil.next.key == 99 - i
        L.LIST_DELETE(L.nil.next)
    assert L.nil.next == L.nil
    assert L.nil.prev == L.nil


def test_insertanddelete100fromtail():
    L = LinkedList()
    for i in range(0, 100):
        x = ListElement(i)
        L.LIST_INSERT(x)
        z = L.nil.prev
    for i in range(100):
        assert z.key == i
        L.LIST_DELETE(z)
        z = z.prev
    assert L.nil.next == L.nil
    assert L.nil.prev == L.nil


def test_list_search():
    L = LinkedList()
    for i in range(0, 100):
        x = ListElement(i)
        L.LIST_INSERT(x)
    x = L.LIST_SEARCH(50)
    assert x.prev.key == 51
    assert x.key == 50
    assert x.next.key == 49
