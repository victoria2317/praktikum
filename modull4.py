for i in range(7, 2, -1):
    print(str(i) * i)
    # Program menentukan jumlah hari dalam suatu bulan menggunakan while

# Input dari user dengan validasi menggunakan while
bulan = 0
while bulan < 1 or bulan > 12:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("Bulan harus antara 1 sampai 12. Silakan coba lagi.")

tahun = 0
while tahun <= 0:
    tahun = int(input("Masukkan tahun: "))
    if tahun <= 0:
        print("Tahun harus lebih dari 0. Silakan coba lagi.")

# Menentukan jumlah hari menggunakan while
hari = 0
i = 0

while i == 0:
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        hari = 31
    elif bulan in [4, 6, 9, 11]:
        hari = 30
    elif bulan == 2:
        # Cek tahun kabisat
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            hari = 29
        else:
            hari = 28
    i = 1  # Keluar dari loop

# Output
print(f"\nJumlah hari dalam bulan {bulan} tahun {tahun} adalah {hari} hari.")