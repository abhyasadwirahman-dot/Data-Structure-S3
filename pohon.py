class Node:
    def __init__(self, info, parent=None):
        self.info = info
        self.parent = parent
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.cur = None

    def MakeRoot(self, info):
        self.root = Node(info)
        self.cur = self.root

    def AddNode(self, info, side):
        child = Node(info, parent=self.cur)

        if side == "L":
            self.cur.left = child
        else:
            self.cur.right = child

        self.cur = child
        return self.cur

    def UpToParent(self):
        if self.cur is not None and self.cur.parent is not None:
            self.cur = self.cur.parent
        return self.cur

    def Traversal(self, node, kunjungi):
        if node is None:
            return

        self.Traversal(node.left, kunjungi)
        self.Traversal(node.right, kunjungi)
        kunjungi(node.info)


def Postorder(tree):
    hasil = []
    tree.Traversal(tree.root, hasil.append)
    return hasil


tree = BinaryTree()
tree.MakeRoot("A")
tree.AddNode("B", "L")
tree.UpToParent()
tree.AddNode("C", "R")

print("Postorder =", *Postorder(tree))
