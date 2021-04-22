'''
Fibonacci
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Al-Kisah...

Buatlah program dengan input suatu angka integer yang menghasilkan urutan angka
pada deret fibonacci
PETUNJUK MASUKAN

Input terdiri atas 1 buah angka
PETUNJUK KELUARAN

Output terdiri dari 1 angka yang merupakan angka ke i pada deret fibonacci
CONTOH MASUKAN

5

CONTOH KELUARAN

5

CONTOH MASUKAN

7

CONTOH KELUARAN

13

'''

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(int(input())))
