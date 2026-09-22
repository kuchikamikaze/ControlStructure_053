nilai = int(input("Masukkan persentase nilai siswa: "))

if nilai >= 90:
    print("Excellent performance (Performa Sangat Baik)")
elif nilai >= 80:
    print("Very Good performance (Performa Baik)")
elif nilai >= 70:
    print("Good performance (Performa Cukup)")
elif nilai >= 60:
    print("Average performance (Performa Rata-rata)")
else:
    print("Performa di bawah rata-rata")