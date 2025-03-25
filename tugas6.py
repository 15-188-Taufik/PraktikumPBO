import math

while True:
    try:
        # Meminta input dari pengguna
        user_input = input("Masukkan angka: ")
        
        # Mencoba mengonversi input menjadi float
        number = float(user_input)
        
        # Memeriksa apakah angka negatif
        if number < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif number == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            # Menghitung akar kuadrat jika input valid
            result = math.sqrt(number)
            print(f"Akar kuadrat dari {number} adalah {result}.")
            break
    except ValueError:
        # Menangani input yang bukan angka
        print("Input tidak valid. Harap masukkan angka yang valid.")