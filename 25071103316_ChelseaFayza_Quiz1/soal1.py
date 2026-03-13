buku = [["Algoritma",2000],
        ["Basis Data", 2500],
        ["Biologi", 5000],
        ["Kalkulus", 3000],
        ["Aljabar", 6000]]

print("Daftar Buku")

for i in range(len(buku)):
    print(i+1, buku[i][0],buku[i][1])

pilih = int(input("Pilih Buku: "))

if pilih >=1 and pilih <=5:
    print("Buku yg dipilih:", buku[pilih-1][0])
    print("Harga:", buku[pilih-1][1])
else:
    print("Tidak ada buku tsb")