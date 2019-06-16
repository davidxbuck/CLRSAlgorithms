import InsertionSort


def test_insertionsort1():
    ins = InsertionSort.Array([1, 7, 6, 5, 4, 3, 2, 12, 11, 65, 45, 34, 22, 19, 78, 101])
    ins.INSERTION_SORT()
    assert ins.A == [1, 2, 3, 4, 5, 6, 7, 11, 12, 19, 22, 34, 45, 65, 78, 101]


def test_insertionsort2():
    ins = InsertionSort.Array([])
    ins.INSERTION_SORT()
    assert ins.A == []


def test_insertionsort3():
    ins = InsertionSort.Array([1])
    ins.INSERTION_SORT()
    assert ins.A == [1]
