class Node:
  def __init__ (self, data):
    self.data=data
    self.next=None

class QuenueLinkedList:
  def __init__ (self):
    self.front = None
    self.rear = None
    self.jumlah = 0

  def is_empty (self):
    return self.jumlah == 0

  def enquenue (self, data):
    baru = Node (data)
    if self.is_empty ():
      self.front = baru
      self.rear = baru
    else:
      self.rear.next = baru
      self.rear = baru
    self.jumlah += 1

  def dequenue (self):
    if self.is_empty():
      raise IndexError ("antrean kosong")
    data=self.front.data
    self.front=self.front.next
    self.jumlah -=1
    if self.is_empty():
      self.rear= None
    return data

  def size(self):
    return self.jumlah

  def peek(self):
    if self.is_empty():
      raise IndexError ("antrian kosong")
    return self.front.data

  def display(self):
    if self.is_empty():
      print ("antrian kosong")
      return
    sekarang = self.front
    urutan = 1
    while sekarang is not None:
      print(f"{urutan}. {sekarang.data}")
      sekarang=sekarang.next
      urutan +=1

if __name__ == "__main__":
  antrean = QuenueLinkedList()
  antrean.enquenue("andi")
  antrean.enquenue("budi")
  antrean.enquenue("agus")

  print ("antrean awal")
  antrean.display()
  print("Terdepan:", antrean.peek())
  print("Jumlah", antrean.size())

  while not antrean.is_empty():
    print ("dilayani:", antrean.dequenue())

  print ("kosong:", antrean.is_empty()) 
  print ("Jumlah:", antrean.size())
  try:
    antrean.dequenue()
  except IndexError as Error:
    print (Error)

  antrean.enquenue("bagus")
  print("Terdepan setelah diisi lagi:", antrean.peek())