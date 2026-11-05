import re
import operator

PRIORITAS = {"+": 1, "-": 1, "*": 2, "/": 2}
OPERASI = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def ambil_token(ekspresi):
    return re.findall(r"\d+\.?\d*|[-+*/()]", ekspresi)


def infix_ke_postfix(tokens):
    postfix = []
    st = []
    for t in tokens:
        if t[0].isdigit():
            postfix.append(t)
        elif t == "(":
            st.append(t)
        elif t == ")":
            while st[-1] != "(":
                postfix.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != "(" and PRIORITAS[st[-1]] >= PRIORITAS[t]:
                postfix.append(st.pop())
            st.append(t)

    while st:
        postfix.append(st.pop())
    return postfix


def hitung_postfix(postfix):
    angka = []
    langkah = []
    for t in postfix:
        if t[0].isdigit():
            angka.append(float(t))  
        else:
            b, a = angka.pop(), angka.pop()
            angka.append(OPERASI[t](a, b))
            langkah.append(f"{a:g} {t} {b:g} = {angka[-1]:g}")
    return angka[0], langkah


s = "(2+4)/(6*(4-2))"

postfix = infix_ke_postfix(ambil_token(s))
hasil, langkah = hitung_postfix(postfix)

print("Hasil konversi infix ke postfix = [" + " ".join(postfix) + "]")
print("\nProses menghitung:")
for baris in langkah:
    print(baris)
print("\nHasil akhir =", f"{hasil:g}")