import math

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)

    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)

    def __truediv__(self, other):
        if other.nilai == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return Kalkulator(self.nilai / other.nilai)

    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)

    def log(self):
        if self.nilai <= 0:
            raise ValueError("Logaritma tidak terdefinisi untuk nilai kurang dari atau sama dengan nol")
        return math.log(self.nilai)

    def __str__(self):
        return str(self.nilai)

def main():
    while True:
        nilai1 = float(input("Masukkan nilai pertama: "))
        a = Kalkulator(nilai1)

        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Eksponen")
        print("6. Logaritma")
        print("7. Keluar")

        pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6/7): "))

        if pilihan == 7:
            print("Terima kasih telah menggunakan kalkulator.")
            break

        if pilihan not in [1, 2, 3, 4, 5, 6]:
            print("Pilihan tidak valid")
            continue

        if pilihan == 6:
            try:
                print("Logaritma dari nilai:", a.log())
            except ValueError as e:
                print(e)
        else:
            nilai2 = float(input("Masukkan nilai kedua: "))
            b = Kalkulator(nilai2)

            try:
                if pilihan == 1:
                    print("Penjumlahan:", Kalkulator.__add__(a, b))
                elif pilihan == 2:
                    print("Pengurangan:", Kalkulator.__sub__(a, b))
                elif pilihan == 3:
                    print("Perkalian:", Kalkulator.__mul__(a, b))
                elif pilihan == 4:
                    print("Pembagian:", Kalkulator.__sub__(a, b))
                elif pilihan == 5:
                    print("Eksponen:", Kalkulator.__pow__(a, b))
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
