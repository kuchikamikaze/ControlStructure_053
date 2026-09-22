angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
angka3 = float(input("Masukkan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    print("Angka terbesar adalah:", angka1)
elif angka2 > angka1 and angka2 > angka3:
    print("Angka terbesar adalah:", angka2)
elif angka3 > angka1 and angka3 > angka2:
    print("Angka terbesar adalah:", angka3)
else:
    print("Terdapat angka yang sama atau tidak ada angka terbesar.")