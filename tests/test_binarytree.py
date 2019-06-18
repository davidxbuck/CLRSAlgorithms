import random

from BinaryTree import BinaryTree, Node


def test_initnode():
    x = Node(5)
    assert x.key == 5
    assert x.p == None
    assert x.left == None
    assert x.right == None


def test_inittree():
    T = BinaryTree()
    assert T.root == None


def test_insert():
    T = BinaryTree()
    z = Node(5)
    T.TREE_INSERT(z)
    assert T.root.key == 5
    assert T.root.p == None
    assert T.root.left == None
    assert T.root.right == None


def test_insert2():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    assert T.root.key == 5
    assert T.root.p == None
    assert T.root.left.key == 3
    assert T.root.left.left.key == 2
    assert T.root.right.key == 7
    assert T.root.right.left.key == 6
    assert T.root.left == T.root.left.left.p
    assert T.root.right.left.p == T.root.right


def test_min():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    assert T.TREE_MINIMUM(T.root).key == 2


def test_max():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    assert T.TREE_MAXIMUM(T.root).key == 7


def test_successor():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    a = T.TREE_MINIMUM(T.root)
    assert a.key == 2
    b = T.TREE_SUCCESSOR(a)
    c = T.TREE_SUCCESSOR(b)
    d = T.TREE_SUCCESSOR(c)
    e = T.TREE_SUCCESSOR(d)
    assert b.key == 3
    assert c.key == 5
    assert d.key == 6
    assert e.key == 7
    x = T.TREE_SUCCESSOR(e)
    assert x == None


def test_inorder_tree_walk():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    T.INORDER_TREE_WALK(T.root)

def test_inorder_tree_walk_stack():
    T = BinaryTree()
    T.TREE_INSERT(Node(5))
    T.TREE_INSERT(Node(3))
    T.TREE_INSERT(Node(2))
    T.TREE_INSERT(Node(7))
    T.TREE_INSERT(Node(6))
    T.INORDER_TREE_WALK_WITH_STACK(T.root)

def test_inorder_tree_walk2(capsys):
    T = BinaryTree()
    for key in random.sample(range(1000), 1000):
        T.TREE_INSERT(Node(key))
    T.INORDER_TREE_WALK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == list(range(1000))

def test_inorder_tree_walk_with_stack2(capsys):
    T = BinaryTree()
    for key in random.sample(range(1000), 1000):
        T.TREE_INSERT(Node(key))
    T.INORDER_TREE_WALK_WITH_STACK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == list(range(1000))


def test_preorder_tree_walk(capsys):
    T = BinaryTree()
    keys = [5, 3, 2, 7, 6]
    for key in keys:
        T.TREE_INSERT(Node(key))
    T.PREORDER_TREE_WALK_WITH_STACK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == keys


def test_preorder_tree_walk2(capsys):
    T = BinaryTree()
    keys = [5, 3, 2, 7, 6]
    for key in keys:
        T.TREE_INSERT(Node(key))
    T.PREORDER_TREE_WALK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == keys


def test_preorder_tree_walk_compare(capsys):
    T = BinaryTree()
    keylist = [2, 3, 1, 6, 5] # list(random.sample(range(10), 5))
    # keylist = list(random.sample(range(1000), 1000))
    for key in keylist:
        T.TREE_INSERT(Node(key))
    T.PREORDER_TREE_WALK_WITH_STACK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    T.PREORDER_TREE_WALK(T.root)
    capture2 = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == capture2


def test_postorder_tree_walk_compare(capsys):
    T = BinaryTree()
    keylist = [2, 3, 1, 6, 5] # list(random.sample(range(10), 5))
    for key in keylist:
        T.TREE_INSERT(Node(key))
    T.POSTORDER_TREE_WALK(T.root)
    captured = list(map(int, capsys.readouterr().out.strip().split("\n")))
    assert captured == [1, 5, 6, 3, 2]
