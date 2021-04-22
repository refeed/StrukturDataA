'''

DESKRIPSI SOAL

Erwin sedang belajar memasak suatu menu. Ketika ia melihat resep, dibutuhkan N bahan dan masing-masing bahan membutuhkan sebanyak B1, B2, ... , BN. Ternyata, setelah mengecek di dapur, Erwin hanya memiliki sebanyak K1, K2, ... , KN. Dengan bahan-bahan yang ada, bisakah Erwin memasak?
PETUNJUK MASUKAN

Input terdiri atas tiga baris. Baris pertama berisi satu buah bilangan bulat N (1 ≤ N ≤ 1000) yang menyatakan banyak bahan. Baris kedua berisi N buah bilangan yang menyatakan B1, B2, ... , BN. Baris ketiga berisi N buah bilangan yang menyatakan K1, K2, ... , KN.
PETUNJUK KELUARAN

Outputkan "YA" jika Erwin bisa memasak, atau "TIDAK" jika kekurangan bahan.
CONTOH MASUKAN 1

4
4 3 4 6
5 5 10 10

CONTOH KELUARAN 1

YA

CONTOH MASUKAN 2

4
4 3 4 6
5 5 10 5

CONTOH KELUARAN 2

TIDAK

KETERANGAN

Pada contoh pertama, Erwin bisa memasak. Pada contoh kedua, Erwin tidak bisa memasak karena bahan keempat tidak cukup (Erwin hanya mempunyai 5, sedangkan dibutuhkan 6).
'''

num_material_int = int(input())
needed_int_list = list(map(int, input().split()))
available_int_list = list(map(int, input().split()))

def main():
    for i in range(num_material_int):
        if needed_int_list[i] > available_int_list[i]:
            print('TIDAK')
            return
    print('YA')

if __name__ == '__main__':
    main()
