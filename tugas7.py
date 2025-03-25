def main():
    to_do_list = []

    while True:
        try:
            print("\nPilih aksi:")
            print("1. Tambah tugas")
            print("2. Hapus tugas")
            print("3. Tampilkan daftar tugas")
            print("4. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3/4): ")

            if pilihan == '1':
                tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
                if not tugas:
                    raise ValueError("Tugas tidak boleh kosong.")
                to_do_list.append(tugas)
                print("Tugas berhasil ditambahkan!")

            elif pilihan == '2':
                if not to_do_list:
                    print("Daftar tugas kosong, tidak ada yang bisa dihapus.")
                    continue
                try:
                    nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                    if nomor < 1 or nomor > len(to_do_list):
                        raise IndexError("Tugas dengan nomor tersebut tidak ditemukan.")
                    removed_task = to_do_list.pop(nomor - 1)
                    print(f"Tugas '{removed_task}' berhasil dihapus!")
                except ValueError:
                    print("Error: Masukkan nomor tugas yang valid.")
                except IndexError as e:
                    print(f"Error: {e}")

            elif pilihan == '3':
                if not to_do_list:
                    print("Daftar Tugas kosong.")
                else:
                    print("Daftar Tugas:")
                    for i, tugas in enumerate(to_do_list, start=1):
                        print(f"- {i}. {tugas}")

            elif pilihan == '4':
                print("Keluar dari program.")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka 1, 2, 3, atau 4.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__": 
    main()