'''

DESKRIPSI SOAL

Di suatu toko, terdapat suatu sistem yang memprioritaskan perempuan dalam
antriannya. Sistem Prioritas perempuan ini akan diaktifkan ketika jumlah
perempuan yang mengantri lebih sedikit dari pada antrian laki-laki. Buatlah
suatu sistem yang menerima masukan list jenis kelamin dari para pengantri
kemudian tentukan, sistem aktif atau tidak PETUNJUK MASUKAN

list huruf P dan L (menggunakan huruf kapital) dan diakhiri dengan huruf N
dengan dipisahkan dengan spasi. Panjang input tidak dibatasi. PETUNJUK KELUARAN

output ada 2 kemungkinan, "aktif" dan "tidak aktif" (menggunakan huruf kecil)
CONTOH MASUKAN

P L L P L L P L L P L P L P P N

CONTOH KELUARAN

tidak aktif
'''

input_char_list = input().split()

sum_of_p = 0
sum_of_l = 0

for char in input_char_list:
    if char == 'N':
        break
    if char == 'P':
        sum_of_p += 1
    elif char == 'L':
        sum_of_l += 1

if sum_of_l >= sum_of_p:
    print('tidak aktif')
else:
    print('aktif')
