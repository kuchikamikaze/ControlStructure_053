batas_maksimal = int(input("Masukkan batas maksimal angka Fibonacci: "))

angka1 = 0
angka2 = 1

print("Deret Fibonacci:")
while angka1 <= batas_maksimal:
    print(angka1, end=" ")
    
    selanjutnya = angka1 + angka2
    
    angka1 = angka2
    angka2 = selanjutnya