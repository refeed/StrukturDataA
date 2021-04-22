'''
Letter T Array
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Bayangkan sebuah tabung seperti gambar di atas. Tabung dengan tiga cabang dan
salah satunya menghadap ke atas. Kali ini kita akan bermain dengan sebuah array
yang bentuknya seperti di atas. Proses “Push” data baru seakan menjatuhkan bola
melalui cabang yang menghadap ke atas. Ketika banyak bola di bagian bawah adalah
genap, maka bola baru akan jatuh tepat di tengah, sedangkan jika banyak bola di
bagian bawah adalah ganjil maka bola jatuh akan berada di tepat sebelah kiri
bola paling tengah. (Contoh dapat dilihat bagian akhir soal)
PETUNJUK MASUKAN

Baris pertama adalah bilangan bulat N, banyak data yang akan di-”Push”. N buah
data selanjutnya adalah bilangan bulat yang akan di-”Push” pada array tersebut
secara terurut.
PETUNJUK KELUARAN

Outputkan dari kiri ke kanan data yang ditampilkan pada bagian bawah array
setelah semua data masuk
CONTOH MASUKAN 1

5
1 2 3 4 5

CONTOH KELUARAN 1

2 4 5 3 1

CONTOH MASUKAN 2

4
4 1 3 2

CONTOH KELUARAN 2

1 2 3 4

KETERANGAN
'''
num_of_data = int(input())
data_list = list(map(int, input().split()))

data_in_letter_t = []
for data in data_list:
    data_in_letter_t.insert((len(data_in_letter_t) // 2), data)

print(' '.join(list(map(str, data_in_letter_t))) + ' ')
