class Node:
    def __init__(self, info, parent=None):
        self.info = info
        self.parent = parent    
        self.left = None        
        self.right = None       


class BTree:
    MAX_ANAK = 4

    def __init__(self):
        self.root = None
        self.cur = None

    def AddRoot(self, info):
        self.root = Node(info)
        self.cur = self.root

    def AddLeft(self, info):
        if self.cur.left is not None:
            raise ValueError("anak pertama sudah ada, pakai AddRight")
        self.cur.left = Node(info, self.cur)
        self.cur = self.cur.left

    def AddRight(self, info):
        if self.cur.parent is None:
            raise ValueError("root tidak punya saudara")
        if self.cur.right is not None:
            raise ValueError("saudara berikutnya sudah ada")
        if self.jumlah_anak(self.cur.parent) >= self.MAX_ANAK:
            raise ValueError("anak sudah penuh (maksimal 4)")
        self.cur.right = Node(info, self.cur.parent)
        self.cur = self.cur.right

    def up(self):
        if self.cur is not None and self.cur.parent is not None:
            self.cur = self.cur.parent

    def jumlah_anak(self, nd):
        n = 0
        c = nd.left
        while c is not None:
            n += 1
            c = c.right
        return n

    def traversal(self, nd):
        if nd is None:
            return
        print(nd.info)
        self.traversal(nd.left)
        self.traversal(nd.right)


T = BTree()
T.AddRoot("A")
T.AddLeft("B")      
T.AddLeft("C")      
T.AddRight("D")     
T.up()               
T.AddRight("E")     
T.AddRight("F")     
T.traversal(T.root)