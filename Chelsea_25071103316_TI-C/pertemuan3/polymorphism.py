class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


#polimorpism

menu = [["Nasi Goreng",15000],
        ["Mie Goreng",14000],
        ["Ayam Goreng",18000],
        ["Es Teh",5000],
        ["Jus Jeruk",8000]]

print("Menu Warung Barokah")

for i in range(len(menu)):
    print(i+1, menu[i][0],menu[i][1])

pilih = int(input("Pilih menu: "))

if pilih >=1 and pilih <=5:
    print("Menu yg dipilih:", menu[pilih-1][0])
    print("Harga:", menu[pilih-1][1])
else:
    print("Menu tidak ada")

# poli 2
menu = [["Nasi Goreng",15000],
        ["Mie Goreng",14000],
        ["Ayam Goreng",18000],
        ["Es Teh",5000],
        ["Jus Jeruk",8000]]

pesanan = []
total = 0

while True:
    print("Menu:")
    for i in range(len(menu)):
        print(i+1, menu[i][0], "-", menu[i][1])

    pilih = int(input("Pilih menu: "))

    if pilih == 0:
        break

    jumlah = int(input("Jumlah: "))

    nama = menu[pilih-1][0]
    harga = menu[pilih-1][1]

    subtotal = harga * jumlah
    total = total + subtotal

    pesanan.append([nama, jumlah, subtotal])

print("Daftar Pesanan")
for p in pesanan:
    print(p[0], "x", p[1], "=", p[2])

print("Total =", total)

#poli 3
total = int(input("Masukkan total belanja: "))

bayar = int(input("Masukkan uang: "))

while bayar < total:
    print("Uang kurang")
    bayar = int(input("Masukkan uang lagi: "))

kembalian = bayar - total

print("Total:", total)
print("Bayar:", bayar)

if kembalian == 0:
    print("Uang pas")
else:
    print("Kembalian:", kembalian)


#poli 4
hari = int(input("Jumlah hari: "))
menu = int(input("Jumlah menu: "))

data = []

for i in range(hari):
    baris = []
    for j in range(menu):
        x = int(input("Jumlah porsi: "))
        baris.append(x)
    data.append(baris)

print("Data Penjualan")

for i in range(hari):
    for j in range(menu):
        print(data[i][j], end=" ")
    print()

print("Total per hari")
for i in range(hari):
    print(sum(data[i]))

print("Total per menu")
for j in range(menu):
    total = 0
    for i in range(hari):
        total = total + data[i][j]
    print(total)
    

#poli 5
class Menu:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print(self.nama,"- Rp",self.harga)

class Transaksi:
    def __init__(self):
        self.total = 0

    def tambah(self,menu,jumlah):
        self.total = self.total + menu.harga * jumlah

    def struk(self):
        print("Total belanja:",self.total)


m1 = Menu("Nasi Goreng",15000)
m2 = Menu("Mie Goreng",14000)
m3 = Menu("Es Teh",5000)

daftar = [m1,m2,m3]

for m in daftar:
    m.tampilkan()

t = Transaksi()

pilih = int(input("Pilih menu (1-3): "))
jumlah = int(input("Jumlah: "))

t.tambah(daftar[pilih-1],jumlah)

t.struk()