angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 >= angka2 and angka1 >= angka3:
    terbesar = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    terbesar = angka2
else:
    terbesar = angka3

print("Angka terbesar adalah:", terbesar)