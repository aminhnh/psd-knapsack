# Tugas Praktikum Struktur Data - 0/1 Knapsack
# 25 Mei 2023 Pukul 08.00 s.d 1 Juni 2023 Pukul 12.00 

import numpy as np
def knapsack(n, uang):
    if arr[n][uang] != 0:
        # Jika hasil terdapat pada array (telah dikalkulasi sebelumnya), return hasil tersebut
        return arr[n][uang]
    if n < 0:
        # Jika seluruh buah telah di cek
        hasil = 0 
    elif harga[n] > uang:
        # Jika harga buah > sisa uang
        hasil = knapsack(n-1, uang)
    else:
        val1 = knapsack(n-1, uang)                      # Jika item tidak dimasukkan
        val2 = kalori[n] + knapsack(n-1, uang - harga[n]) # Jika item dimasukkan
        hasil = max(val1, val2)                         # Mengambil nilai terbesar diantara val1 & val2
    arr[n][uang] = hasil                                # Menyimpan hasil ke array
    return hasil

# Harga dan kalori dari masing-masing buah dikalikan stoknya, dan disimpan di dalam list
harga = 3*[2360] + 3*[2120] + 5*[1890] + 10*[3770] + 5*[2870]
kalori = 3*[91] + 3*[71] + 5*[105] + 10*[103] + 5*[96]

# n digunakan sebagai index untuk mengakses list harga dan list kalori (26 item) 
n = len(harga)
uang = 25000

# Array untuk menyimpan hasil
arr = np.zeros((n, uang))

hasil = knapsack(n-1, uang-1)
print(hasil)