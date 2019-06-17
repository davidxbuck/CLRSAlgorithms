import MergeSort


def test_merge1():
    ms = MergeSort.Array([1, 2])
    assert ms.A == [1, 2]
    ms.MERGE(0, 1, 1)
    assert ms.A == [1, 2]


def test_merge2():
    ms = MergeSort.Array([2, 1])
    ms.MERGE(0, 1, 1)
    assert ms.A == [1, 2]


def test_merge3():
    ms = MergeSort.Array([3, 4, 1, 2])
    ms.MERGE(0, 2, 3)
    assert ms.A == [1, 2, 3, 4]


def test_merge4():
    ms = MergeSort.Array([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
    ms.MERGE(0, 5, 9)
    assert ms.A == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_mergesort1():
    ms = MergeSort.Array([1, 7, 6, 5, 4, 3, 2, 12, 11, 65, 45, 34, 22, 19, 78, 101])
    ms.MERGE_SORT(0, len(ms.A) - 1)
    assert ms.A == [1, 2, 3, 4, 5, 6, 7, 11, 12, 19, 22, 34, 45, 65, 78, 101]


def test_mergesort2():
    ms = MergeSort.Array([])
    ms.MERGE_SORT(0, len(ms.A) - 1)
    assert ms.A == []


def test_mergesort3():
    ms = MergeSort.Array([1])
    ms.MERGE_SORT(0, len(ms.A) - 1)
    assert ms.A == [1]
