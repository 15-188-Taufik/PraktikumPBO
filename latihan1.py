# Kelas Induk Kendaraan
class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum): #constructor yang mendefinisikan diri sendiri
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis Kendaraan: {self.jenis}")
        print(f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam")

    def bergerak(self):
        print("Kendaraan sedang bergerak")

# Kelas Turunan Mobil yang mewarisi sifat dan atribut dari Kendaraan
class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum) # super() digunakan untuk mengakses method dari parent class
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        self.info_kendaraan()
        print(f"Merek Mobil: {self.merk}")
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        print("Klakson mobil berbunyi: Beep Beep!")

# Kelas Turunan MobilSport yang mewarisi sifat dan atribut dari Mobil
class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        self.info_mobil()
        print(f"Tenaga Kuda: {self.__tenaga_kuda} HP")
        print(f"Harga: {self.__harga} juta rupiah")

    def mode_balap(self):
        print("Mobil sport masuk ke mode balap!")


#contoh penggunaan hingga turunannya
mobil1 = MobilSport("Mobil Sport", 300, "Ferrari", 2, 500, 1000) #cara mengakses turunan dengan parameter
#"mobil sport " adalah jenis, 300 adalah kecepatan maksimum, "Ferrari" adalah merk, 2 adalah jumlah pintu, 500 adalah tenaga kuda, 1000 adalah harga

#contoh penggunaan 
mobil1.info_mobil_sport()
mobil1.mode_balap()
mobil1.bergerak()
mobil1.bunyikan_klakson()
mobil1.info_kendaraan()
print(mobil1.get_tenaga_kuda())
print(mobil1.get_harga())
mobil1.set_tenaga_kuda(600)
mobil1.set_harga(2000)
print(mobil1.get_tenaga_kuda())
print(mobil1.get_harga())

#menggunakan getter dan setter
print ("Menggunakan getter dan setter")
mobil1.__tenaga_kuda = 1000
print(mobil1.__tenaga_kuda)
mobil1.__harga = 3000
print(mobil1.__harga)


