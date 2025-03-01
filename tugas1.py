# meminta input dari user
n = int(input("Masukkan tinggi segitiga: "))

# membuat segitiga sama sisi
for i in range(1, n + 1): # parameter pertama untuk range() adalah 1, 
                          #dan parameter kedua adalah n + 1. Ini berarti kita akan melakukan loop dari 1 hingga n.
    print(' ' * (n - i) + '*' * (2 * i - 1)) #untuk setiap baris i, 
                                             #kita cetak n - i spasi diikuti dengan 2 * i - 1 bintang.
    # simbol * akan terus bertambah sebanyak 2 * i - 1, dimulai dari 1, 3, 5, 7, dan seterusnya.
    # spasi akan terus berkurang sebanyak n - i, dimulai dari n - 1, n - 2, n - 3, dan seterusnya.
  