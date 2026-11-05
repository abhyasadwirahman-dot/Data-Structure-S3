#program simple menghitung persegi
def luas_persegi (sisi = 5):
    luas = sisi * sisi
    return luas
sisi = int(input("panjang sisi = "))
print("luas persegi = ", luas_persegi(sisi))
