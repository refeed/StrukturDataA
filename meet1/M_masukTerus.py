'''
Masuk Terus5 Batas Run-time:     1 detik / test-case Batas Memori:   32 MB
DESKRIPSI SOAL

Buat program yang dapat menampung N data usia mahasiswa. sistem akan terus
menerus meminta input sampai pengguna memasukkan angka 0 atau kurang dari itu.
kemudian, minta input a(0<=a < N). outputkan: jumlah mahasiswa yang berumur
kurang dari a dan lebih dari a. PETUNJUK MASUKAN

Input terdiri atas 2 baris. baris pertama merupakan baris data dengan banyak
data yang diakhiri dengan 0 atau angka kurang dari 0, sedangkan baris kedua
berupa 1 bilangan bulat PETUNJUK KELUARAN

Outputkan jumlah mahasiswa yang berumur kurang dari a dan lebih dari a dari data
usia yang telah dimasukkan. CONTOH MASUKAN

1 2 3 4 5 6 7 8 9 0 3

CONTOH KELUARAN 1

2 6

CONTOH MASUKAN

3 5 5 4 -9 5

CONTOH KELUARAN 1

2 0

'''

number_list = list(map(int, input().split()))
the_a_num = int(input())

new_number_list = []

for num in number_list:
    if num <= 0:
        break
    new_number_list.append(num)

def count_how_many_values_below_and_over_the_a(num_list, a):
    below = 0
    over = 0
    for num in num_list:
        if num == a:
            continue
        if num < a:
            below += 1
        else:
            over += 1
    return below, over

for num in count_how_many_values_below_and_over_the_a(new_number_list, the_a_num):
    print(num)
