class node:
    def __init__(self, info, link = None):
        self.info = info
        self.next = None

global Ptrhead , Ptrnow

Ptrhead = None
def TambahData(isi):
    global Ptrhead , Ptrnow
    if  Ptrhead == None :
            PtrNow = node (isi)
            Ptrhead = PtrNow
    else : 
         PtrBef = Ptrnow
         PtrNow = node (isi)
         PtrBef.link = PtrNow

def Traversal():
    PtrTravesal = Ptrhead
    while PtrTravesal:
         print(PtrTravesal.isi)
         PtrTravesal = PtrTravesal.link

TambahData("A")
Traversal()
