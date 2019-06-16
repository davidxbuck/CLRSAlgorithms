import QuickSort


def test_init():
    qs = QuickSort.Array([1, 3, 4])
    assert qs.A == [1, 3, 4]


def test_partition():
    qs = QuickSort.Array([1, 4, 3])
    qs.PARTITION(0, len(qs.A) - 1)
    assert qs.A == [1, 3, 4]


def test_partition2():
    qs = QuickSort.Array([1, 4, 3, 5, 2])
    qs.PARTITION(0, len(qs.A) - 1)
    assert qs.A == [1, 2, 3, 5, 4]


def test_partition3():
    qs = QuickSort.Array([1, 4, 3, 5, 6])
    qs.PARTITION(0, len(qs.A) - 1)
    assert qs.A == [1, 4, 3, 5, 6]


def test_partition4():
    qs = QuickSort.Array([2, 4, 3, 5, 1])
    qs.PARTITION(0, len(qs.A) - 1)
    assert qs.A == [1, 4, 3, 5, 2]


def test_mini_sort1():
    qs = QuickSort.Array([5, 4, 3, 2, 1])
    qs.PARTITION(0, 4)
    assert qs.A == [1, 4, 3, 2, 5]
    qs.PARTITION(0, 3)
    assert qs.A == [1, 2, 3, 4, 5]
    qs.PARTITION(0, 2)
    assert qs.A == [1, 2, 3, 4, 5]
    qs.PARTITION(0, 1)
    assert qs.A == [1, 2, 3, 4, 5]


def test_mini_sort2():
    qs = QuickSort.Array([5, 3, 4, 2, 1])
    qs.PARTITION(0, 4)
    assert qs.A == [1, 3, 4, 2, 5]
    qs.PARTITION(1, 3)
    assert qs.A == [1, 2, 4, 3, 5]
    qs.PARTITION(2, 3)
    assert qs.A == [1, 2, 3, 4, 5]


def test_actual_sort1():
    qs = QuickSort.Array([5, 3, 4, 2, 1])
    qs.QUICKSORT(0, len(qs.A) - 1)
    assert qs.A == [1, 2, 3, 4, 5]


def test_quicksort1():
    qs = QuickSort.Array([1, 7, 6, 5, 4, 3, 2, 12, 11, 65, 45, 34, 22, 19, 78, 101])
    qs.QUICKSORT(0, len(qs.A) - 1)
    assert qs.A == [1, 2, 3, 4, 5, 6, 7, 11, 12, 19, 22, 34, 45, 65, 78, 101]


def test_quicksort2():
    qs = QuickSort.Array([])
    qs.QUICKSORT(0, len(qs.A) - 1)
    assert qs.A == []


def test_quicksort3():
    qs = QuickSort.Array([1])
    qs.QUICKSORT(0, len(qs.A) - 1)
    assert qs.A == [1]


def test_quicksort4():
    qs = QuickSort.Array([2, 1])
    qs.QUICKSORT(0, len(qs.A) - 1)
    assert qs.A == [1, 2]
