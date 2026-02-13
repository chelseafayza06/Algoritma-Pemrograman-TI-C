class Vehicle:
     def __init__(self, jenis, merk, tahun_rilis):
          self.jenis = jenis
          self.merk = merk 
          self.tahun_rilis = tahun_rilis

     def sound(self):
        return "suara"

     
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
         self.__tahun_rilis = tahun_rilis 

    def get_tahun_rilis(self):
        return self.__tahun_rilis

    def set_tahun_rilis(self):
        return self.__tahun_rilis

    def sound (self):
        return ("brommm")


class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis):
        self.__tahun_rilis = tahun_rilis 

    def get_tahun_rilis(self):
        return self.__tahun_rilis
    
    def get_tahun_rilis(self):
        return self.__tahun_rilis
    
    def sound (self):
        return ("ngenggg")
    
v1 = Vehicle ("avanza", "manual", 1990)
c1 = Motor ("scoopy", "karbu", 2012)
m1 = Mobil ("yaris", "matic" ,2000)

print(m1.sound())
print(c1.get_tahun_rilis())



