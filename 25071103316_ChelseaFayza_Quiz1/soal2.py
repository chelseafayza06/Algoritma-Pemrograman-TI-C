buku = [["Algoritma",2000],
        ["Basis Data", 2500],
        ["Biologi", 5000],
        ["Kalkulus", 3000],
        ["Aljabar", 6000]]

judul_buku = []
lama_pinjam = "hari"

while True: 
    print("Daftar Buku:")
    for i in range(len(buku)):
        print(i+1, buku[i][0], buku[i][0])

    pilih = int(input("Pilih Buku Yang Ingin Anda Pinjam: "))

    if pilih == 0:
        break

    lama_pinjam = int(input("Lama Pinjam: "))

    denda = buku[pilih-1][0]
    lama_pinjam = buku[pilih-1][1]

    denda_hari = 1

    if denda_hari > 1 :
        print("Anda Harus Membayar ")
    else:
        print("Silahkan Pinjam Buku")

    judul_buku.append([denda, denda_hari])

print("Daftar Pesanan")
for p in judul_buku:
    print(p[0], "x", p[1], "=", p[2])

print("mendapatkan denda =", denda_hari)

# maaf kak / bang saya ngestuck hehe gaktau lagi mau gimana caranya







