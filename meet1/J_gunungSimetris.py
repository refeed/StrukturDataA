'''
Gunung Simetris
Batas Run-time: 	1 detik / test-case
Batas Memori: 	64 MB
DESKRIPSI SOAL

Buatlah sebuah deret gunung seperti contoh di bawah.
PETUNJUK MASUKAN

Sebuah bilangan bulat N. (1≤N≤100)
PETUNJUK KELUARAN

keluarkan deret gunung dengan tampilan horizontal (satu angka per baris).
CONTOH MASUKAN 1

5

CONTOH KELUARAN 1

1
2
3
4
5
4
3
2
1

CONTOH MASUKAN 2

8

CONTOH KELUARAN 2

1
2
3
4
5
6
7
8
7
6
5
4
3
2
1
'''

batas_int = int(input())

for i in range(1, batas_int):
    print(i)
for i in range(batas_int, 0, -1):
    print(i)
