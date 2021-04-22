'''
Cross Over (simplified)
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Dalam ilmu genetika, penyebab terjadinya keberagaman makhluk hidup adalah karena
adanya persilangan pada suatu gen (crossover). Anda diberikan 2 buah gen yang
akan disilangkan beserta string penanda bagian dari gen akan disilangkan atau
tidak, outputkan gen akhirnya. PETUNJUK MASUKAN

2 buah string beda baris yang menunjukan 2 gen yang akan disilangkan, panjang
gen maksimal 20 karakter dan hanya terdiri dari alfabet kapital. Lalu sebuah
string penanda bagian yang akan disilangkan terdiri dari karakter '1' dan '0'.
Ketika string penanda bernilai '1' maka bagian dari string gen pertama akan
ditukarkan dengan bagian yang sejajar pada gen kedua. Jika string penanda
bernilai '0' maka tidak terjadi penukaran. PETUNJUK KELUARAN

Kondisi gen pertama setelah terjadi crossover
CONTOH MASUKAN 1

AAAAA
ZZZZZ
00100

CONTOH KELUARAN 1

AAZAA

CONTOH MASUKAN 2

ABCDEFGHI
UUJJKRIAN
000101111

CONTOH KELUARAN 2

ABCJERIAN
'''

dna_1 = input()
dna_2 = input()
crossOverOrnot = input()

new_dna = []

for i in range(len(dna_1)):
    if crossOverOrnot[i] == '1':
        new_dna.append(dna_2[i])
    else:
        new_dna.append(dna_1[i])

new_dna_str = ''.join(new_dna)

print(new_dna_str)
