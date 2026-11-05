# -*- coding: utf-8 -*-
"""Rumus segitiga: infix -> postfix -> hitung nilainya."""

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


PRIORITAS = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_ke_postfix(expr):
    s_stack = Stack()
    output = []          # list token postfix
    i = 0
    while i < len(expr):
        token = expr[i]

        if token == " ":
            pass

        elif token.isdigit() or token == ".":
            angka = token
            while i + 1 < len(expr) and (expr[i + 1].isdigit() or expr[i + 1] == "."):
                i += 1
                angka += expr[i]
            output.append(angka)

        elif token.isalpha():
            output.append(token)             # variabel: a, b, c, t, ...

        elif token == "(":
            s_stack.push(token)

        elif token == ")":
            while not s_stack.isEmpty() and s_stack.peek() != "(":
                output.append(s_stack.pop())
            s_stack.pop()

        elif token in PRIORITAS:
            while (not s_stack.isEmpty()
                   and s_stack.peek() != "("
                   and (PRIORITAS[s_stack.peek()] > PRIORITAS[token]
                        or (PRIORITAS[s_stack.peek()] == PRIORITAS[token]
                            and token != "^"))):   # ^ asosiatif kanan
                output.append(s_stack.pop())
            s_stack.push(token)

        i += 1

    while not s_stack.isEmpty():
        output.append(s_stack.pop())
    return output


def hitung_postfix(postfix, nilai):
    """nilai = dict variabel -> angka, mis. {"a": 6, "t": 4}"""
    st = Stack()
    for tok in postfix:
        if tok in PRIORITAS:
            b = st.pop()
            a = st.pop()
            if tok == "+": st.push(a + b)
            elif tok == "-": st.push(a - b)
            elif tok == "*": st.push(a * b)
            elif tok == "/": st.push(a / b)
            elif tok == "^": st.push(a ** b)
        elif tok.isalpha():
            st.push(nilai[tok])
        else:
            st.push(float(tok))
    return st.pop()


RUMUS = {
    "Luas":       ("(a*t)/2",        {"a": 6, "t": 4}),
    "Keliling":   ("a+b+c",          {"a": 3, "b": 4, "c": 5}),
    "Pythagoras": ("(a^2+b^2)^0.5",  {"a": 3, "b": 4}),
    "Heron":      ("(s*(s-a)*(s-b)*(s-c))^0.5", {"s": 6, "a": 3, "b": 4, "c": 5}),
}

if __name__ == "__main__":
    for nama, (infix, nilai) in RUMUS.items():
        pf = infix_ke_postfix(infix)
        hasil = hitung_postfix(pf, nilai)
        print(f"{nama}")
        print(f"  infix   : {infix}")
        print(f"  postfix : {' '.join(pf)}")
        print(f"  nilai   : {nilai}")
        print(f"  hasil   : {hasil}\n")