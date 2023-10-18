# Input nilai variable
a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")

# Cetak nilai variable
print("Variable a =", a)
print("Variable b =", b)

# Cetak hasil operasi kedua variable dengan string format
# Anda harus mengonversi a dan b ke tipe data int sebelum melakukan operasi matematika
a = int(a)
b = int(b)
print("Hasil penggabungan {} & {} = {}".format(a, b, a + b))

# Konversi nilai variable sudah dilakukan di atas, jadi tidak perlu dilakukan lagi
# Hapus baris berikut
# a = int(a)
# b = int(b)

# Perhatikan bahwa operasi pembagian akan menghasilkan float, bukan int
print("Hasil penjualan {} / {} = {}".format(a, b, a / b))
