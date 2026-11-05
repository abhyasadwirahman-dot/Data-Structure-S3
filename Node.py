class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.jumlah = 0

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.jumlah

    def enqueue(self, data):
        baru = Node(data)
        if self.is_empty():
            self.front = baru
        else:
            self.rear.next = baru
        self.rear = baru
        self.jumlah += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Antrean kosong.")
        data = self.front.data
        self.front = self.front.next
        self.jumlah -= 1
        if self.is_empty():
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Antrean kosong.")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
            return
        sekarang = self.front
        urutan = 1
        while sekarang is not None:
            print(f"{urutan}. {sekarang.data}")
            sekarang = sekarang.next
            urutan += 1


if __name__ == "__main__":
    antrean = QueueLinkedList()
    antrean.enqueue("Andi")
    antrean.enqueue("Budi")
    antrean.enqueue("Agus")

    print("Antrean awal:")
    antrean.display()
    print("Terdepan:", antrean.peek())
    print("Jumlah:", antrean.size())

    while not antrean.is_empty():
        print("Dilayani:", antrean.dequeue())

    print("Kosong:", antrean.is_empty())
    print("Jumlah:", antrean.size())

    try:
        antrean.dequeue()
    except IndexError as error:
        print(error)

    antrean.enqueue("Bagus")
    print("Terdepan setelah diisi lagi:", antrean.peek())