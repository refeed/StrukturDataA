'''

DESKRIPSI SOAL

Erwin memiliki dua orang teman, Eko dan Wahyudi. Eko sangat menyukai bilangan
ganjil, sehingga barang-barang yang dipunyai pasti banyaknya merupakan bilangan
ganjil. Sedangkan Wahyudi sangat menyukai bilangan genap, sehingga barang-barang
yang dipunyai pasti banyaknya merupakan bilangan genap.

Erwin memiliki N buah permen dan ingin memberikan N buah permen tersebut kepada
Eko dan Wahyudi. Perhatikan bahwa Eko dan Wahyudi harus mendapat permen, karena
jika ada yang tidak mendapat permen, Erwin akan dimusuhi. Bisakah Erwin
membaginya kepada kedua orang temannya tersebut? PETUNJUK MASUKAN

Input terdiri atas sebuah bilangan bulat N (1 ≤ N ≤ 1000) yang menyatakan banyak
permen yang dipunyai Erwin. PETUNJUK KELUARAN

Outputkan "YA" (tanpa tanda kutip) jika Erwin bisa membagi permen kepada kedua
temannya tersebut, atau outputkan "TIDAK" (tanpa tanda kutip) jika Erwin tidak
bisa membagi permen kepada kedua temannya tersebut.

Perhatikan bahwa di akhir output, harus diberi enter. CONTOH MASUKAN 1

5

CONTOH KELUARAN 1

YA

CONTOH MASUKAN 2

10

CONTOH KELUARAN 2

TIDAK

KETERANGAN

Pada Contoh 1, Erwin bisa membagi permen kepada kedua temannya dengan cara
memberi 3 permen kepada Eko dan 2 permen kepada Wahyudi.

Pada Contoh 2, Erwin tidak akan bisa membagi permen kepada kedua temannya,
bagaimanapun caranya.
'''

input_num = int(input())

if input_num % 2 == 0 or input_num < 3:
    print('TIDAK')
else:
    print('YA')
