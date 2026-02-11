import math #Menggunakan modul math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
    #fungsi di module math Python yang dipakai untuk menghitung akar kuadrat.
    
# Contoh
hasil = jarak(0, 0, 3, 4)
print("Jarak =", hasil) 