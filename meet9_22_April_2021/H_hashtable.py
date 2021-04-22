'''
Hash Table
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Hashing merupakan teknik yang secara khusus digunakan untuk mengidentifikasi
obyek tertentu dari sekumpulan obyek yang serupa. Sebagai contoh, di
universitas, setiap mahasiswa diberi nomor identifikasi khusus yang dapat
digunakan untuk mendapatkan informasi mengenai mereka. Pada kedua contoh
tersebut, mahasiswa diproses menggunakan hashing dengan nomor unik.

Pada kasus ini, akan digunakan fungsi menggunakan nim mahasiswa. nim mahasiswa
akan di modulo n (n adalah banyak mahasiswa). Panjang Array yang akan digunakan
adalah n.

Jika fungsi modulo ini menghasilkan collusion, maka digunakan metode linier,
yaitu diletakkan pada index Array yang masih kosong disetelah index yang
seharusnya.

Buatlah Program yang meminta input deret angka nim, tampilkan sesuai dengan
isinya
PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak mahasiswa. Baris kedua berisi n buah bilangan bulat nim,
yang menyatakan a1, a2, ..., an
PETUNJUK KELUARAN

Outputkan isi Array.
CONTOH MASUKAN

9
8 9 4 6 5 2 1 3 7

CONTOH KELUARAN

0=9
1=1
2=2
3=3
4=4
5=5
6=6
7=7
8=8

CONTOH MASUKAN

3
1 4 7

CONTOH KELUARAN

0=7
1=1
2=4
'''

class ModuloHashTable:
    def __init__(self, num_of_buckets):
        self._num_of_buckets = num_of_buckets
        self._buckets = []
        for _ in range(num_of_buckets):
            self._buckets.append(None)

    def put(self, number):
        original_hash = self._hash(number)
        offset = 0
        while (
            self._buckets[
                (original_hash + offset) % (self._num_of_buckets - 1)
                ] is not None):
            offset += 1
        self._buckets[original_hash + offset] = number

    def get(self, numbucket):
        return self._buckets[numbucket]

    def _hash(self, number):
        return number % self._num_of_buckets

if __name__ == '__main__':
    num_of_buckets = int(input())
    nim_list = list(map(int, input().split()))

    hashtable = ModuloHashTable(num_of_buckets)

    for nim in nim_list:
        hashtable.put(nim)

    for numbucket in range(num_of_buckets):
        value = hashtable.get(numbucket)
        if value is None:
            continue
            # value = ''

        print('{0}={1}'.format(numbucket, value))
