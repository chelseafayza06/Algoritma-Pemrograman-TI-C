def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)

# Contoh
print(pangkat_rekursif(2, 5))