# Input nilai variable
a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")

# Cetak nilai variable
print("Variable a =", a)
print("Variable b =", b)

# Cetak hasil operasi kedua variable dengan string format
print("Hasil penggabungan {0} & {1} ={2}".format(a,b, a+b))

# Anda harus mengonversi a dan b ke tipe data int sebelum melakukan operasi matematika
a = int(a)
b = int(b)
print("Hasil penjumlahan {0} + {1} = {2}".format(a,b, a + b))

# Konversi nilai variable sudah dilakukan di atas, jadi tidak perlu dilakukan lagi
# Perhatikan bahwa operasi pembagian akan menghasilkan float, bukan int
print("Hasil pembagian {0} / {1} = {2:.2f}".format(a,b, a / b))
