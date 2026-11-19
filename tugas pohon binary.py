import re

PREC = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
RIGHT = {'^'}  # operator right-associative


def tokenize(s):
    return re.findall(r'\d+\.?\d*|[A-Za-z_]\w*|[-+*/^()]', s)


def shunting(tokens, prefix=False):
    """Infix -> postfix. Jika prefix=True: balik token, tukar kurung,
    asosiatif dibalik, lalu hasil dibalik lagi (jadi prefix)."""
    if prefix:
        swap = {'(': ')', ')': '('}
        tokens = [swap.get(t, t) for t in reversed(tokens)]
    out, st = [], []
    for t in tokens:
        if t in PREC:
            while st and st[-1] in PREC:
                sama = PREC[st[-1]] == PREC[t]
                # postfix: pop jika sama & left-assoc; prefix: pop jika sama & right-assoc
                pop_saat_sama = (t in RIGHT) if prefix else (t not in RIGHT)
                if PREC[st[-1]] > PREC[t] or (sama and pop_saat_sama):
                    out.append(st.pop())
                else:
                    break
            st.append(t)
        elif t == '(':
            st.append(t)
        elif t == ')':
            while st[-1] != '(':
                out.append(st.pop())
            st.pop()
        else:
            out.append(t)
    out += st[::-1]
    return out[::-1] if prefix else out


class Node:
    def __init__(self, v, l=None, r=None):
        self.v, self.l, self.r = v, l, r


def build(postfix):
    st = []
    for t in postfix:
        if t in PREC:
            r, l = st.pop(), st.pop()
            st.append(Node(t, l, r))
        else:
            st.append(Node(t))
    return st[0]


def preorder(n):
    return [] if not n else [n.v] + preorder(n.l) + preorder(n.r)


def postorder(n):
    return [] if not n else postorder(n.l) + postorder(n.r) + [n.v]


def inorder(n):
    if not n:
        return []
    if not n.l:  # daun
        return [n.v]
    return ['('] + inorder(n.l) + [n.v] + inorder(n.r) + [')']


def evaluate(n):
    if n.v not in PREC:
        return float(n.v)  # ValueError jika variabel
    a, b = evaluate(n.l), evaluate(n.r)
    return {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}[n.v]


def proses(nama, ekspr):
    tok = tokenize(ekspr)
    post = shunting(tok)
    pref = shunting(tok, prefix=True)
    root = build(post)

    ino = ''.join(inorder(root))
    ok_a = preorder(root) == pref
    ok_b = shunting(tokenize(ino)) == post
    ok_c = postorder(root) == post

    print(f"== {nama}: {ekspr}")
    print("Token  :", tok)
    print("Postfix:", ' '.join(post))
    print("Prefix :", ' '.join(pref))
    print("Inorder:", ino)
    print("Verifikasi (pre/in/post):", ok_a, ok_b, ok_c)
    try:
        print("Nilai  :", evaluate(root))
    except ValueError:
        print("Nilai  : - (ada operand non-numerik)")
    print()


if __name__ == "__main__":
    proses("E1", "(a-b)/((c+d)*e)")
    proses("E2", "3+4*2/(1-5)^2^3")   # ^ right-assoc: (1-5)^(2^3)
    proses("E3", "(x+y)*(p-q)")