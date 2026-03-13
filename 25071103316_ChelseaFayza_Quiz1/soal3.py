buku = [["Algoritma",2000],
        ["Basis Data", 2500],
        ["Biologi", 5000],
        ["Kalkulus", 3000],
        ["Aljabar", 6000]]

Jumlah_hari = int(input("Masukkan jumlah hari keterlambatan: "))

total_denda = int(input("Masukkan: "))

while hari < Jumlah_hari:
    print("hari keterlambatan tdk kurang dari 0")
    hari = int(input("Masukkan hari keterlambatan: "))

total_denda = Jumlah_hari - hari 

print("Jumlah hari:", Jumlah_hari)
print("hari:", hari)

if total_denda == 0:
    print("tdk ada denda")
else:
    print("total denda anda:", total_denda)
