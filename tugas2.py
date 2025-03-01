# Meminta jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Inisialisasi dictionary kosong
data_siswa = {}

# Loop untuk mengisi data siswa
for i in range(1, jumlah_siswa + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ") #f pada input (f "")adalah format string, yang memungkinkan kita untuk menyisipkan variabel ke dalam string.
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    data_siswa[nama] = nilai

# Menampilkan dictionary
print("\ndictiorary =", data_siswa)