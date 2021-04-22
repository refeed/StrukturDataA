'''
Air Botol
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Al-Kisah...

Suatu hari, ada 3 orang petualang dari Jogjakarta yang sedang melakukan
perjalanan ke Kota Merauke. Siang itu, mereka terlihat berjalan menyusuri
jalanan untuk mencari rumah makan agar dapat membeli minuman.

Dalam perjalanan itu, mereka telah kehabisan perbekalan minuman sejak pagi.

Setelah bertemu rumah makan, mereka segera memesan minuman yang cukup banyak dan
akan dimasukkan ke dalam beberapa botol yang mereka bawa. Terdapat 22 botol
dengan ukuran yang berbeda. 6 Botol besar (berukuran 1500ml), 7 botol sedang
(berukuran 600ml) dan 9 botol kecil (berukuran 200ml).

Air minum yang dibeli kemudian akan dituangkan ke dalam botol besar terlebih
dahulu sampai habis. Jika 6 botol besar terisi penuh semua dan air minum masih
ada(belum habis), maka air minum sisa akan diisikan ke botol sedang sampai
terisi penuh semua. Jika air minum masih ada lagi, maka air minum yang belum
masuk botol akan diisikan ke botol kecil. Jika air minum masih ada lagi, maka
air minum sisa ini akan dikembalikan kepada penjualnya.

Jika terdapat N ml air minum yang dibeli, Berapa banyak botol yang terisi penuh?
PETUNJUK MASUKAN

Input terdiri atas 1 buah angka yang merupakan banyak air minum yang dibeli
(dalam ml)
PETUNJUK KELUARAN

Output terdiri dari 1 angka yang menggambarkan banyak botol yang terisi penuh
CONTOH MASUKAN

5000

CONTOH KELUARAN

3

CONTOH MASUKAN

12000

CONTOH KELUARAN

11
'''
water_volume = int(input())

bottles_and_volume = [
    [6, 1500],
    [7, 600],
    [9, 200]
]

full_bottles_sum = 0
bottle_idx = 0
while water_volume > 0:
    num_bottle, volume = bottles_and_volume[bottle_idx]
    for _ in range(num_bottle):
        if water_volume < volume:
            water_volume = 0
            break
        else:
            water_volume -= volume
            full_bottles_sum +=1

    # Ganti botol
    bottle_idx += 1

    # Kalo semua botol udah keisi tapi masih belum abis water_volumenya
    # keluar dari while loop
    if bottle_idx > 2:
        break

print(full_bottles_sum)
