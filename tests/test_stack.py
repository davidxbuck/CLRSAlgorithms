import pytest

import Stack


def test_empty():
    stack = Stack.Stack()
    assert stack.S == [None] * 20
    assert stack.top == 0
    assert stack.n == 20


def test_stack_empty():
    stack = Stack.Stack()
    assert stack.STACK_EMPTY == True


def test_stack_pop():
    with pytest.raises(Stack.Underflow):
        stack = Stack.Stack()
        popped = stack.POP()


def test_stack_push():
    stack = Stack.Stack()
    stack.PUSH(5)
    assert stack.S == [5] + [None] * 19
    assert stack.top == 1
    assert stack.STACK_EMPTY == False


def test_stack_pushpop():
    stack = Stack.Stack()
    stack.PUSH(5)
    assert stack.S == [5] + [None] * 19
    assert stack.top == 1
    assert stack.STACK_EMPTY == False
    popped = stack.POP()
    assert stack.S == [5] + [None] * 19
    assert stack.top == 0
    assert popped == 5
    assert stack.STACK_EMPTY == True


def test_stack_pushpoppop():
    with pytest.raises(Stack.Underflow):
        stack = Stack.Stack()
        stack.PUSH(5)
        assert stack.S == [5] + [None] * 19
        assert stack.top == 1
        assert stack.STACK_EMPTY == False
        popped = stack.POP()
        assert stack.S == [5] + [None] * 19
        assert stack.top == 0
        assert popped == 5
        assert stack.STACK_EMPTY == True
        popped = stack.POP()
        assert stack.S == [5] + [None] * 19
        assert stack.top == 0
        assert popped == None
        assert stack.STACK_EMPTY == True


def test_stack_pushpushpop():
    stack = Stack.Stack()
    stack.PUSH(5)
    assert stack.S == [5] + [None] * 19
    assert stack.top == 1
    assert stack.STACK_EMPTY == False
    stack.PUSH(7)
    assert stack.S == [5, 7] + [None] * 18
    assert stack.top == 2
    assert stack.STACK_EMPTY == False
    popped = stack.POP()
    assert stack.S == [5, 7] + [None] * 18
    assert stack.top == 1
    assert popped == 7
    assert stack.STACK_EMPTY == False


def test_stack_overflow():
    stack = Stack.Stack()
    assert stack.n == 20
    for i in range(0, stack.n):
        stack.PUSH(i)
    assert len(stack.S) == 20
    assert stack.S == [x for x in range(0, 20)]
    assert stack.top == 20
    assert stack.STACK_EMPTY == False
    stack.PUSH(20)
    assert len(stack.S) == 40
    assert stack.S == [x for x in range(0, 21)] + [None] * 19
    assert stack.top == 21
    assert stack.STACK_EMPTY == False
