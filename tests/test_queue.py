import pytest

import Queue


def test_empty():
    queue = Queue.Queue()
    assert queue.Q == [None] * 20
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.length == 20


def test_enqueue():
    queue = Queue.Queue()
    queue.ENQUEUE(5)
    assert queue.Q == [5] + [None] * 19
    assert queue.head == 0
    assert queue.tail == 1
    assert queue.length == 20


def test_enqueue2():
    queue = Queue.Queue()
    queue.ENQUEUE(5)
    queue.ENQUEUE(6)
    assert queue.Q == [5, 6] + [None] * 18
    assert queue.head == 0
    assert queue.tail == 2
    assert queue.length == 20


def test_enqueue19():
    queue = Queue.Queue()
    for i in range(0, 19):
        queue.ENQUEUE(i)
    assert queue.Q == list(range(0, 19)) + [None]
    assert queue.head == 0
    assert queue.tail == 19
    assert queue.length == 20


def test_enqueue20():
    with pytest.raises(OverflowError):
        queue = Queue.Queue()
        for i in range(0, 20):
            queue.ENQUEUE(i)


def test_enqueuedequeue():
    queue = Queue.Queue()
    queue.ENQUEUE(5)
    deq = queue.DEQUEUE()
    assert queue.Q == [5] + [None] * 19
    assert deq == 5
    assert queue.head == 1
    assert queue.tail == 1
    assert queue.length == 20


def test_enqueuedequeue2():
    with pytest.raises(Queue.Underflow):
        queue = Queue.Queue()
        queue.ENQUEUE(5)
        deq = queue.DEQUEUE()
        deq = queue.DEQUEUE()


def test_enqueuedequeue19():
    queue = Queue.Queue()
    for i in range(0, 19):
        queue.ENQUEUE(i)
        deq = queue.DEQUEUE()
        assert deq == i
    assert queue.Q == list(range(0, 19)) + [None]
    assert queue.head == 19
    assert queue.tail == 19
    assert queue.length == 20


def test_enqueuedequeue20():
    queue = Queue.Queue()
    for i in range(0, 20):
        queue.ENQUEUE(i)
        deq = queue.DEQUEUE()
        assert deq == i
    assert queue.Q == list(range(0, 20))
    assert queue.head == 0
    assert queue.tail == 0
    assert queue.length == 20


def test_enqueuedequeue19b():
    queue = Queue.Queue()
    for i in range(0, 19):
        queue.ENQUEUE(i)
    for i in range(0, 19):
        deq = queue.DEQUEUE()
        assert deq == i
    assert queue.Q == list(range(0, 19)) + [None]
    assert queue.head == 19
    assert queue.tail == 19
    assert queue.length == 20


def test_enqueuedequeue21():
    queue = Queue.Queue()
    for i in range(0, 21):
        queue.ENQUEUE(i)
        deq = queue.DEQUEUE()
        assert deq == i
    assert queue.Q == [20] + list(range(1, 20))
    assert queue.head == 1
    assert queue.tail == 1
    assert queue.length == 20
