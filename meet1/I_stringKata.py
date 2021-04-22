'''
Tulis Ke Bawah
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Petruk menuliskan sebuah kata yang cukup panjang. Anda diminta menampilkan
perkata ke bawah.
PETUNJUK MASUKAN

Input terdiri atas 1 baris, yaitu kata dari Petruk
PETUNJUK KELUARAN

Outputkan kata petruk menurun
CONTOH MASUKAN

ayam goreng

CONTOH KELUARAN

ayam
goreng

'''

input_str_list = input().split()

for word in input_str_list:
    print(word)
