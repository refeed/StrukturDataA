'''
Max 3 angka
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Buatlah program yang menerima 3 buah input nilai, outputkan nilai paling besar
diantara ketiga input tersebut.
PETUNJUK MASUKAN

Input terdiri atas 3 angka dalam 1 baris
PETUNJUK KELUARAN

Outputkan angka terbesar dari 3 angka yang dimasukkan
CONTOH MASUKAN

10 9 11

CONTOH KELUARAN

11
'''

input_int_list = list(map(int, input().split()))

biggest = input_int_list[0]

for num in input_int_list:
    if num > biggest:
        biggest = num

print(biggest)
