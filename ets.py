# ETS
# Nrp  : 5024251089
# Nama : Muhamad Abhyasa Dwi Rahman
#

MAX = 100


class Stack:
    def __init__(self):
        self.data = [None] * MAX
        self.top = -1

    def push(self, x):
        self.data[self.top + 1] = x
        self.top += 1

    def pop(self):
        x = self.data[self.top]
        self.top -= 1
        return x

    def peek(self):
        return self.data[self.top]

    def kosong(self):
        return self.top == -1


def prioritas(op):
    if op in "*/":
        return 2
    if op in "+-":
        return 1
    return 0


def terapkan(angka, operator):
    b = angka.pop()
    a = angka.pop()
    op = operator.pop()
    if op == "+":
        angka.push(a + b)
    elif op == "-":
        angka.push(a - b)
    elif op == "*":
        angka.push(a * b)
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Pembagian dengan nol")
        angka.push(a / b)


def Hitung(str):
    angka = Stack()
    operator = Stack()
    i = 0

    while i < len(str):
        c = str[i]

        if c == " ":
            i += 1
            continue

        if c.isdigit() or c == ".":
            j = i
            while j < len(str) and (str[j].isdigit() or str[j] == "."):
                j += 1
            angka.push(float(str[i:j]))
            i = j
            continue

        if c == "(":
            operator.push(c)
        elif c == ")":
            while not operator.kosong() and operator.peek() != "(":
                terapkan(angka, operator)
            operator.pop()  
        elif c in "+-*/":
            while not operator.kosong() and prioritas(operator.peek()) >= prioritas(c):
                terapkan(angka, operator)
            operator.push(c)
        i += 1

    while not operator.kosong():
        terapkan(angka, operator)

    result = angka.peek()
    return int(result) if result == int(result) else result


if __name__ == "__main__":
    ekspresi = input("Masukkan ekspresi: ")
    print("Output :", Hitung(ekspresi))
