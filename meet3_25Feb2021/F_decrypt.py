'''
DESKRIPSI SOAL

Pengkodean A1Z26 adalah metode enkripsi subtitusi sederhana yang mengubah huruf “A” menjadi angka 1, “B” menjadi angka 2, dan seterusnya hingga “Z” menjadi 26, atau sebaliknya. Buatlah program yang menerima masukan angka-angka, lalu kodekan menjadi huruf yang bersesuaian.
PETUNJUK MASUKAN

Input adalah sekumpulan angka yang diinputkan dengan format berikut:

n t
a1 a2 a3 ... an

Nilai n (0 < n ≤ 30) adalah banyak angka yang akan diinputkan dan a1 sampai an adalah angka yang harus dikodekan. Nilai t antara 1 atau 0, jika t bernilai 1 artinya outputkan dalam huruf tidak kapital, dan jika nilai t adalah 0 outputkan dalam huruf kapital.
PETUNJUK KELUARAN

Sebuah string hasil pengkodean, ditulis sambung tanpa spasi
CONTOH MASUKAN

6 0
22 15 11 1 19 9

CONTOH KELUARAN

VOKASI
'''

UPPERCASE_LETTER_OFFSET = ord('A') - 1
LOWERCASE_LETTER_OFFSET = ord('a') - 1

def decrypt_A1Z26(num_list, lowercase_or_not):
    char_list = []
    offset = LOWERCASE_LETTER_OFFSET if lowercase_or_not else UPPERCASE_LETTER_OFFSET
    for num in num_list:
        char_list.append(chr(offset + num))
    return ''.join(char_list)

_, t = list(map(int, input().split()))
numbers_list = list(map(int, input().split()))

print(decrypt_A1Z26(numbers_list, t))
