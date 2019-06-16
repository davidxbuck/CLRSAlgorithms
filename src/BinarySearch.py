import itertools


class BSNode(object):
    newid = itertools.count()

    def __init__(self, value):
        self.id = next(self.__class__.newid)
        self.key = value
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        return "Node ID {}, key {}, p {}, left {}, right {}".format(self.id, self.key, self.p, self.left, self.right)


class BSTree(object):

    def __init__(self):
        self.nullnode = BSNode(None)
        self.nodes = {self.nullnode.id: self.nullnode}
        self.root = self.nullnode

    def __str__(self):
        return "XXX \n{} \n{} \nXXX".format(self.root, len(self.nodes))

    def tree_insert(self, z):
        assert isinstance(z, BSNode)
        y = self.nullnode
        x = self.root
        while x.id != 0:
            y = x
            if z.key < x.key:
                x.key = x.left
            else:
                x.key = x.right
        z.p = y.key
        self.nodes[z.key] = z
        if y.key is None:
            self.root = z
        elif z.key > y.key:
            self.nodes[y.key].right = z.key
        else:
            self.nodes[y.key].left = z.key

def print_tree(tree):
    for key, node in tree.nodes.items():
        print(node)
    print(len(tree.nodes))
    print()

def main():
    tree = BSTree()
    print_tree(tree)
    tree.tree_insert(BSNode(2))
    print_tree(tree)
    tree.tree_insert(BSNode(3))
    print_tree(tree)
    tree.tree_insert(BSNode(4))
    print_tree(tree)




if __name__ == '__main__':
    main()
