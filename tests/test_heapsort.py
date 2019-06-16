import HeapSort


def test_init():
    hs = HeapSort.Heap([1, 3, 4])
    assert hs.A == [1, 3, 4]
    assert hs.heap_size == 3
    assert hs.length == 3
    assert hs.length == 3
    hs.heap_size -= 1
    assert hs.heap_size == 2
    assert hs.length == 3


def test_parent():
    hs = HeapSort.Heap()
    assert hs.PARENT(1) == 0
    assert hs.PARENT(2) == 0
    assert hs.PARENT(3) == 1
    assert hs.PARENT(4) == 1
    assert hs.PARENT(5) == 2


def test_left():
    hs = HeapSort.Heap()
    assert hs.LEFT(0) == 1
    assert hs.LEFT(1) == 3
    assert hs.LEFT(2) == 5
    assert hs.LEFT(3) == 7
    assert hs.LEFT(4) == 9


def test_right():
    hs = HeapSort.Heap()
    assert hs.RIGHT(0) == 2
    assert hs.RIGHT(1) == 4
    assert hs.RIGHT(2) == 6
    assert hs.RIGHT(3) == 8
    assert hs.RIGHT(4) == 10


def test_max_heapify1():
    hs = HeapSort.Heap([1, 3, 4])
    assert hs.LEFT(0) == 1
    assert hs.RIGHT(0) == 2
    assert hs.A == [1, 3, 4]
    hs.MAX_HEAPIFY(0)
    assert hs.A == [4, 3, 1]


def test_max_heapify2():
    hs = HeapSort.Heap([1, 4, 3])
    assert hs.LEFT(0) == 1
    assert hs.RIGHT(0) == 2
    assert hs.A == [1, 4, 3]
    hs.MAX_HEAPIFY(0)
    assert hs.A == [4, 1, 3]


def test_max_heapify3():
    hs = HeapSort.Heap([1, 7, 6, 5, 4, 3, 2])
    assert hs.A == [1, 7, 6, 5, 4, 3, 2]
    hs.MAX_HEAPIFY(0)
    assert hs.A == [7, 5, 6, 1, 4, 3, 2]


def test_min_heapify1():
    hs = HeapSort.Heap([4, 3, 1])
    hs.MIN_HEAPIFY(0)
    assert hs.A == [1, 3, 4]


def test_min_heapify2():
    hs = HeapSort.Heap([3, 4, 1])
    hs.MIN_HEAPIFY(0)
    assert hs.A == [1, 4, 3]


def test_min_heapify3():
    hs = HeapSort.Heap([8, 7, 6, 5, 4, 3, 2])
    hs.MIN_HEAPIFY(0)
    assert hs.A == [6, 7, 2, 5, 4, 3, 8]


def test_build_max_heap():
    hs = HeapSort.Heap([1, 7, 6, 5, 4, 3, 2])
    hs.BUILD_MAX_HEAP()
    assert hs.A == [7, 5, 6, 1, 4, 3, 2]


def test_build_min_heap():
    hs = HeapSort.Heap([8, 7, 6, 5, 4, 3, 2])
    hs.BUILD_MIN_HEAP()
    assert hs.A == [2, 4, 3, 5, 7, 8, 6]


def test_heapsort():
    hs = HeapSort.Heap([1, 7, 6, 5, 4, 3, 2])
    hs.HEAPSORT()
    assert hs.A == [1, 2, 3, 4, 5, 6, 7]


def test_heapsort2():
    hs = HeapSort.Heap([1, 7, 6, 5, 4, 3, 2, 12, 11, 65, 45, 34, 22, 19, 78, 101])
    hs.HEAPSORT()
    assert hs.A == [1, 2, 3, 4, 5, 6, 7, 11, 12, 19, 22, 34, 45, 65, 78, 101]


def test_heapsort3():
    hs = HeapSort.Heap([])
    hs.HEAPSORT()
    assert hs.A == []


def test_heapsort4():
    hs = HeapSort.Heap([1])
    hs.HEAPSORT()
    assert hs.A == [1]


def test_heapsort5():
    hs = HeapSort.Heap([2, 1])
    hs.HEAPSORT()
    assert hs.A == [1, 2]


def test_min_heapsort():
    hs = HeapSort.Heap([1, 7, 6, 5, 4, 3, 2])
    hs.MIN_HEAPSORT()
    assert hs.A == [7, 6, 5, 4, 3, 2, 1]
