'''
Antri
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Bagian pembayaran SPP di suatu sekolah ANEH, diberlakukan sistem informasi yang
unik. setiap ada siswa yang akan membayar spp diharuskan memasukkan nis dan
namanya kemudian menekan tombol pada suatu mesin yang telah disiapkan. Setelah
tombol tersebut ditekan, maka akan keluar suatu kertas yang berisi nama-nama
siswa yang sudah mengantri sebelumnya

Buatlah program untuk mensimulasikan cara kerja sistem tersebut
PETUNJUK MASUKAN

Baris pertama berisi bilangan bulat N yang menyatakan banyaknya siswa yang telah
mengantri.

N baris berikutnya adalah list siswa yang antri spp

Baris terakhir berisi nis siswa yang akan dicetak kertas antrinya
PETUNJUK KELUARAN

Jika nis merupakan antrian awal, maka outputkan "langsung bayar", akan tetapi
jika ada antrian sebelumnya maka outputkan list nama siswa yang mengantri
sebelum nis siswa yang dimasukkan dibaris terakhir input program (nis siswa
dipastikan ada di N baris input). urutan nama silahkan diperhatikan di contoh
CONTOH MASUKAN

6
111 agus
222 budi
333 susi
444 iman
555 nudya
666 ito
111

CONTOH KELUARAN

langsung bayar

CONTOH MASUKAN

6
111 agus
222 budi
333 susi
444 iman
555 nudya
666 ito
555

CONTOH KELUARAN

iman
susi
budi
agus
'''
import sys

num_data = int(input())
data = []

for _ in range(num_data):
    data.append(input().split())

nis_str = input()

index = None
for i, data_i in enumerate(data):
    if data_i[0] != nis_str:
        continue

    if i == 0:
        print('langsung bayar')
        sys.exit(0)

    index = i
    break

for i in range(index-1, -1, -1):
    print(data[i][1])
