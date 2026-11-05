# -*- coding: utf-8 -*-
"""Konversi infix ke postfix memakai Stack (Shunting-yard)."""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def getSize(self):
        return len(self.items)

    def Cetak(self):
        print(" ".join(self.items))


PRIORITAS = {"+": 1, "-": 1, "*": 2, "/": 2}


def infix_ke_postfix(expr):
    s_stack = Stack()    # menyimpan operator dan "("
    s_output = Stack()   # hasil postfix

    i = 0
    while i < len(expr):
        token = expr[i]

        if token.isdigit():
            # gabungkan digit berurutan jadi satu angka (mis. "12")
            angka = token
            while i + 1 < len(expr) and expr[i + 1].isdigit():
                i += 1
                angka += expr[i]
            s_output.push(angka)

        elif token == "(":
            s_stack.push(token)

        elif token == ")":
            # keluarkan operator sampai ketemu "("
            while not s_stack.isEmpty() and s_stack.peek() != "(":
                s_output.push(s_stack.pop())
            s_stack.pop()  # buang "("

        elif token in PRIORITAS:
            # operator di stack yang prioritasnya >= token keluar dulu
            while (not s_stack.isEmpty()
                   and s_stack.peek() != "("
                   and PRIORITAS[s_stack.peek()] >= PRIORITAS[token]):
                s_output.push(s_stack.pop())
            s_stack.push(token)

        i += 1

    # sisa operator di stack pindah ke output
    while not s_stack.isEmpty():
        s_output.push(s_stack.pop())

    return s_output


if __name__ == "__main__":
    for expr in ["((4*3)+1)", "4+3*2", "(12+3)*5-6/2"]:
        print(expr, "->", end=" ")
        infix_ke_postfix(expr).Cetak()