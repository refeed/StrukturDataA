'''
Biner to Bulat
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Diberikan suatu string kombinasi angka 1 dan 0 yang merupakan angka biner., ubahlah string tersebut menjadi angka bulat N(0 <= N <= 2147483647).
PETUNJUK MASUKAN

suatu string List angka kombinasi angka 1 dan 0 yang merupakan angka biner.
PETUNJUK KELUARAN

suatu angka N, yang menyatakan bilangan bulat dari string biner yang diinputkan
CONTOH MASUKAN

1111111111111111111111111111110

CONTOH KELUARAN

2147483646

CONTOH MASUKAN

0

CONTOH KELUARAN

0

CONTOH MASUKAN

111

CONTOH KELUARAN

7
'''
import sys

str_input = list(input())

power = 0
result = 0
while len(str_input) > 0:
    binary_num = int(str_input.pop())
    if binary_num == 0 and power == 0:
        power += 1
        continue
    result += (2 *  binary_num) ** power
    power += 1

sys.stdout.write(str(result))
