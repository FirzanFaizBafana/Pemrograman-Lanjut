# Definisikan variabel
p = 11
q = 5
r = 4

# Ekspresi pertama
a1 = 15 % 5
b1 = (12 + 3 * 5) == 75
c1 = "PML" + "15523"
try:
    d1 = "100" + 234
except TypeError:
    d1 = "Error"
e1 = ((11 % 3) + 2) != 8 / 2

# Ekspresi dengan variabel
a2 = (p - r) == (r + q)
b2 = ((p % 3) + q) != (r % 2)
c2 = (q - 3) == (p % 2 + q)
d2 = (r + q) != ((p * 2) % 2)
e2 = ((q % 3) + p) > (r % 2)
f2 = (r + p) <= (q * 5)

# hasilnya
print("a1 =", a1)  # 15 mod 5
print("b1 =", b1)  # 12 + 3 * 5 == 75
print("c1 =", c1)  # "PML" + "15523"
print("d1 =", d1)  # "100" + 234
print("e1 =", e1)  # ((11 % 3) + 2) != 8 / 2
print("a2 =", a2)  # (p - r) == (r + q)
print("b2 =", b2)  # ((p % 3) + q) != (r % 2)
print("c2 =", c2)  # (q - 3) == (p % 2 + q)
print("d2 =", d2)  # (r + q) != ((p * 2) % 2)
print("e2 =", e2)  # ((q % 3) + p) > (r % 2)
print("f2 =", f2)  # (r + p) <= (q * 5)
