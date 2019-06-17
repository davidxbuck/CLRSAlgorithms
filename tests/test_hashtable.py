from HashTable import HashTable
from LinkedList import ListElement, LinkedList


def test_init():
    ht = HashTable()
    assert ht.m == 59
    assert ht.T == [None] * ht.m


def test_h():
    ht = HashTable()
    hashes = [ht.h(x) for x in range(1000)]
    assert max(hashes) == 58
    assert min(hashes) == 0
    assert 20 <= sum(hashes) / 1000 <= 30
    hash2 = [ht.h(x) for x in range(1000)]
    assert hashes == hash2


def test_insert():
    ht = HashTable()
    hash = ht.h(5)
    assert isinstance(ht.T[hash], type(None))
    ht.CHAINED_HASH_INSERT(5)
    assert isinstance(ht.T[hash], LinkedList)
    assert ht.T[hash].head.key == 5
    assert ht.T.count(None) == ht.m - 1


def test_failed_search():
    ht = HashTable()
    assert ht.CHAINED_HASH_SEARCH(10) == None


def test_successful_hash_search():
    ht = HashTable()
    ht.CHAINED_HASH_INSERT(5)
    assert ht.CHAINED_HASH_SEARCH(5).key == 5
    assert isinstance(ht.CHAINED_HASH_SEARCH(5), ListElement)


def test_successful_hash_search2():
    ht = HashTable()
    ht.CHAINED_HASH_INSERT(5)
    assert ht.CHAINED_HASH_SEARCH(5).key == 5
    assert isinstance(ht.CHAINED_HASH_SEARCH(5), ListElement)


def test_successful_hash_add_and_delete():
    ht = HashTable()
    hash = ht.h(5)
    ht.CHAINED_HASH_INSERT(5)
    x = ht.CHAINED_HASH_SEARCH(5)
    ht.CHAINED_HASH_DELETE(x)
    assert ht.T[hash].head == None


def test_successful_hash_multiadd_and_delete():
    ht = HashTable()
    n = 0
    i = 0
    keys = []
    while n < 5:
        hash = ht.h(i)
        if hash == 5:
            n += 1
            keys.append(i)
        i += 1
    listelements = []
    for key in keys:
        assert ht.h(key) == hash
        ht.CHAINED_HASH_INSERT(key)
        listelements.append(ht.T[hash].head)
    for ix, key in enumerate(keys):
        assert listelements[ix] == ht.CHAINED_HASH_SEARCH(key)
    x = ht.CHAINED_HASH_SEARCH(keys[1])
    y = ht.CHAINED_HASH_SEARCH(keys[2])
    z = ht.CHAINED_HASH_SEARCH(keys[3])
    assert x.prev == y
    assert z.next == y
    ht.CHAINED_HASH_DELETE(y)
    assert x.prev == z
    assert z.next == x
