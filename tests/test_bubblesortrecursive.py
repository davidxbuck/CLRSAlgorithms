import BubbleSortRecursive as BubbleSort


def test_bubblesort1():
    ins = BubbleSort.Array([9, 7, 6, 5, 4, 3, 2, 12, 11, 65, 45, 34, 22, 19, 78, 101])
    ins.BUBBLESORT()
    assert ins.A == [2, 3, 4, 5, 6, 7, 9, 11, 12, 19, 22, 34, 45, 65, 78, 101]


def test_bubblesort2():
    ins = BubbleSort.Array([])
    ins.BUBBLESORT()
    assert ins.A == []


def test_bubblesort3():
    ins = BubbleSort.Array([1])
    ins.BUBBLESORT()
    assert ins.A == [1]


def test_bubblesort4():
    ins = BubbleSort.Array([4, 3, 2, 1])
    ins.BUBBLESORT()
    assert ins.A == [1, 2, 3, 4]
