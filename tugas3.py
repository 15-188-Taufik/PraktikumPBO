# Membuat file bernama "Me.txt" dan menuliskan beberapa baris teks ke dalamnya
with open("Me.txt", "w") as file:
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    resolusi = input("Masukkan resolusi di tahun ini: ")

    file.write(f"masukan nama : {nama} \n")
    file.write(f"masukan nim  : {nim}\n")
    file.write(f"masukan resolusi ditahun ini : {resolusi}\n")

print("File 'Me.txt' telah berhasil dibuat dan diisi dengan teks.")