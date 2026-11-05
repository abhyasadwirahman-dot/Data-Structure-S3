# Single Linked List - versi ringkas (ASCII safe)

class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.link = link

class SinglyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for x in iterable:
                self.insert_at_end(x)

    # ---- util ----
    def to_list(self):
        out, p = [], self.head
        while p:
            out.append(p.info)
            p = p.link
        return out

    # ---- search (unsorted) ----
    def search(self, item):
        p = self.head
        while p:
            if p.info == item:
                return p
            p = p.link
        return None

    # ---- search_sorted (ascending, early stop) ----
    def search_sorted(self, item):
        p = self.head
        while p:
            if item < p.info:   # early stop
                return None
            if item == p.info:
                return p
            p = p.link
        return None

    # ---- insertions ----
    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        p = self.head
        while p.link:
            p = p.link
        p.link = new

    def insert_at_position(self, data, pos):
        # pos: 1-based; pos<=1 -> awal; >len -> di akhir
        if pos <= 1 or not self.head:
            self.insert_at_beginning(data)
            return
        prev = self.head
        for _ in range(1, pos-1):
            if not prev.link:
                break
            prev = prev.link
        prev.link = Node(data, prev.link)

    def delete_at_beginning(self):
      if not self.head:
        return None
      removed = self.head
      self.head = self.head.link
      return removed.info 
      
    def delete_at_end(self):
        if not self.head:
            return None
        if not self.head.link:              # cuma 1 node
            removed = self.head
            self.head = None
            return removed.info
        p = self.head
        while p.link.link:                  # berhenti di node ke-2 dari akhir
            p = p.link
        removed = p.link
        p.link = None
        return removed.info

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.link           # simpan dulu sebelum diputus
            cur.link = prev          # balik arah panah
            prev, cur = cur, nxt
        self.head = prev

    def length(self):
        count, p = 0, self.head
        while p:
            count += 1
            p = p.link
        return count

    def get_at(self, pos):              # ambil data di posisi tertentu (1-based)
        p, i = self.head, 1
        while p and i < pos:
            p, i = p.link, i + 1
        return p.info if p else None
# ---- demo ----
if __name__ == "__main__":
    lst = SinglyLinkedList(["Adams", "Dean", "Fields"])
    print("Awal         :", lst.to_list())

    lst.insert_at_beginning("Aaron")
    print("Insert awal  :", lst.to_list())

    lst.insert_at_end("Samuels")
    print("Insert akhir :", lst.to_list())

    lst.insert_at_position("Brown", 3)
    print("Posisi=3     :", lst.to_list())

    print("SEARCH 'Fields'      :", "Ketemu" if lst.search("Fields") else "Tidak ada")
    print("SEARCH_SORTED 'Cooper':", "Ketemu" if lst.search_sorted("Cooper") else "Tidak ada (early stop)")
    print("SEARCH_SORTED 'Samuels':", "Ketemu" if lst.search_sorted("Samuels") else "Tidak ada")

    print("\nhapus data bagian awal")
    print("Sebelum       :", lst.to_list())
    dihapus = lst.delete_at_beginning()
    print("Yang dihapus  :", dihapus)
    print("Sesudah       :", lst.to_list())
  
    print("\n hapus data di bagian akhir")
    print("Sebelum       :", lst.to_list())
    dihapus = lst.delete_at_end()
    print("Yang dihapus  :", dihapus)
    print("Sesudah       :", lst.to_list())
    
    print("\n--- Test reverse ---")
    print("Sebelum :", lst.to_list())
    lst.reverse()
    print("Sesudah :", lst.to_list())
     
    print("\n--- Test length & get_at ---")
    print("Length        :", lst.length())
    print("get_at(1)     :", lst.get_at(1))
    print("get_at(2)     :", lst.get_at(2))
    print("get_at(99)    :", lst.get_at(99))