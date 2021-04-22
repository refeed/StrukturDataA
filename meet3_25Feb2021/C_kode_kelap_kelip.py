'''

DESKRIPSI SOAL

Sebuah string dikatakan sebagai string kelap kelip jika tidak ada dua huruf yang
sama berjejer. Dua huruf dikatakan berbeda jika dibaca dengan cara yang berbeda.
Misalkan "AaAaA" adalah BUKAN string kelap kelip, karena terdapat banyak dua
huruf sama yang berjejer walaupun berbeda bentuk. PETUNJUK MASUKAN

Sebuah string dengan panjang maksimal 100 karakter yang hanya terdiri dari huruf
kapital dan non-kapital. PETUNJUK KELUARAN

"YA" jika string tersebut kelap kelip dan "TIDAK" jika tidak. CONTOH MASUKAN 1

ABbA

CONTOH KELUARAN 1

TIDAK

CONTOH MASUKAN 2

ABab

CONTOH KELUARAN 2

YA
'''

input_str = input()

def is_the_same_char(char1, char2):
    return char1.lower() == char2.lower()

# O(n) ops
def main():
    for i, char in enumerate(input_str):
        if not i > 0:
            continue
        if is_the_same_char(input_str[i-1], char):
            print('TIDAK')
            return

    print('YA')

if __name__ == '__main__':
    main()
