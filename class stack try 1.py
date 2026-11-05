class stack: 
    def __init__(self):
        self.items = []

    def isEmpty (self):
        return len(self.items) == 0
    
    def push (self,item):
        self.items.append (item)
        
    def pop (self):   
         if not self.isEmpty():
             return self.items.pop()
         else:
             return "tumpukkan kosong"
    
    def peek (self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "tumpukan kosong"
    
    def getsize (self):
        return len(self.items)

s = stack
print(s.isEmpty())

s.push(1)
s.push(2)
s.push(3)

print (s.peek)
print (s.pop)
print (s.getsize)