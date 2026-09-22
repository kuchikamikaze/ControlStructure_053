n = int(input("Masukkan berapa banyak bilangan Fibonacci yang ingin ditampilkan: "))

angka1 = 0
angka2 = 1

print("Deret Fibonacci:")
for i in range(n):
    print(angka1, end=" ")
    
    # Menghitung angka berikutnya
    selanjutnya = angka1 + angka2
    
    # Menggeser posisi angka untuk perhitungan selanjutnya
    angka1 = angka2
    angka2 = selanjutnya