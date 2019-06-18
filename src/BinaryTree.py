'''
BINARY-TREE Algorithm
Directly following the pseudocode from CLRS
'''

import Stack


#
# Because Python indexing starts from 0, not 1, the values of :LEFT, RIGHT and PARENT need to be modified according.y
#         0
#      1     2
#     3 4   5 6
#
#
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None  # parent


class BinaryTree:
    def __init__(self):
        self.root = None

    # TREE-INSERT(T, z)
    # y = NIL
    # x = T.root
    # while x != NIL
    #     y = x
    #     if z.key < x.key
    #         x = x.left
    #     else
    #         x = x.right
    # z.p = y
    # if y == NIL
    #     T.root = z
    # elseif z.key < y.key
    #     y.left = z
    # else
    #     y.right = z

    def TREE_INSERT(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    # TREE-MINIMUM(x)
    # while x.left != NIL
    #     x = x.left
    # return x

    def TREE_MINIMUM(self, x):
        while x.left != None:
            x = x.left
        return x

    # TREE-MAXIMUM(x)
    # while x.right != NIL
    #     x = x.right
    # return x

    def TREE_MAXIMUM(self, x):
        while x.right != None:
            x = x.right
        return x

    # TREE-SUCCESSOR(x)
    # if x.right != NIL
    #     return TREE-MINIMUM(x.right)
    # y = x.p
    # while y != NIL and x == y.right:
    #     x = y
    #     y = y.p
    # return y

    def TREE_SUCCESSOR(self, x):
        if x.right != None:
            return self.TREE_MINIMUM(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    # INORDER_TREE_WALK(self, x):
    # if x != NIL
    #     INORDER_TREE_WALK(x.left)
    #     print(x.key)
    #     INORDER_TREE_WALK(x.right)

    def INORDER_TREE_WALK(self, x):
        if x != None:
            self.INORDER_TREE_WALK(x.left)
            print(x.key)
            self.INORDER_TREE_WALK(x.right)

    def INORDER_TREE_WALK_WITH_STACK(self, x):
        stack = Stack.Stack()
        while True:
            if x != None:
                stack.PUSH(x)
                x = x.left
            elif not stack.STACK_EMPTY:
                x = stack.POP()
                print(x.key)
                x = x.right
            else:
                break

    # ITERATIVE_TREE_SEARCH(x, k):

    # PREORDER-TREE-WALK-WITH-STACK(x)
    #
    # 1    create a new stack S
    # 2   if x≠NIL
    # 3       PUSH (S, x)
    # 4   while STACK-EMPTY(S)==false
    # 5       x= POP(S)
    # 6       print x.key
    # 7       if x.right ≠NIL
    # 8           PUSH (S, x.right)
    # 9       if x.left ≠ NIL
    # 10          PUSH (S, x.left)

    def PREORDER_TREE_WALK_WITH_STACK(self, x):
        stack = Stack.Stack()
        if x != None:
            stack.PUSH(x)
        while not stack.STACK_EMPTY:
            x = stack.POP()
            print(x.key)
            if x.right != None:
                stack.PUSH(x.right)
            if x.left != None:
                stack.PUSH(x.left)

    # PREORDER-TREE-WALK(x)
    # 1 if x ≠ NIL
    # 2     print x.key
    # 3     PREORDER-TREE-WALK(x.left)
    # 4     PREORDER-TREE-WALK(x.right)

    def PREORDER_TREE_WALK(self, x):
        if x != None:
            print(x.key)
            self.PREORDER_TREE_WALK(x.left)
            self.PREORDER_TREE_WALK(x.right)

    # POSTORDER-TREE-WALK(x)
    # 1 if x ≠ NIL
    # 2     PREORDER-TREE-WALK(x.left)
    # 3     PREORDER-TREE-WALK(x.right)
    # 4     print x.key

    def POSTORDER_TREE_WALK(self, x):
        if x != None:
            self.POSTORDER_TREE_WALK(x.left)
            self.POSTORDER_TREE_WALK(x.right)
            print(x.key)

