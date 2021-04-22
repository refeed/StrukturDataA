"""
DESKRIPSI SOAL

Tahun kabisat (bahasa Inggris: Leap year) merupakan tahun yang mengalami
penambahan satu hari dengan tujuan untuk menyesuaikan penanggalan dengan tahun
astronomi.

Dalam satu tahun tidak secara persis terdiri dari 365 hari, tetapi 365 hari 5
jam 48 menit 45,1814 detik. Jika hal ini tidak dihiraukan, maka setiap empat
tahun akan kekurangan hampir 1 hari (tepatnya 23 jam 15 menit 0,7256 detik).

Maka untuk mengkompensasi hal ini, setiap 4 tahun sekali (tahun yang bisa
dibagi 4), diberi 1 hari ekstra: 29 Februari. Tetapi karena 5 jam 48 menit
45,1814 detik kurang dari 6 jam, maka tahun-tahun yang bisa dibagi 100 (seperti
tahun 1900), bukan tahun kabisat, kecuali bisa dibagi dengan 400 (seperti tahun
2000).

Buatlah program yang menerima input sebuah tahun dan menentukan apakah tahun
tersebut kabisat atau bukan

https://id.wikipedia.org/wiki/Tahun_kabisat

PETUNJUK MASUKAN

Input terdiri atas 1 angka, yaitu tahun

PETUNJUK KELUARAN

Outputkan kabisat jika tahun yang dimasukkan merupakan tahun kabisat, outputkan
Bukan kabisat jika tahun yang dimasukkan merupakan tahun kabisat
"""

year = int(input())


NOT_KABISAT_STR = 'Bukan kabisat'
KABISAT_STR = 'kabisat'


if year % 4 == 0:
    if year % 100 == 0 and not year % 400 == 0:
        print(NOT_KABISAT_STR)
    else:
        print(KABISAT_STR)
else:
    print(NOT_KABISAT_STR)
