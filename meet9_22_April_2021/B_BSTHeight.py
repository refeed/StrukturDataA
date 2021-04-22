'''
Soal 1
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary
search tree dari barisan tersebut. Tugas Anda ialah menentukan tinggi dari
binary search tree tersebut.
PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang
menyatakan a1, a2, ..., an
PETUNJUK KELUARAN

Outputkan sebuah bilangan bulat yang merupakan tinggi dari binary search tree
yang terbentuk.
CONTOH MASUKAN

9
3 0 8 2 4 9 1 5 6

CONTOH KELUARAN 1

5

KETERANGAN

Pada contoh testcase, binary search tree yang terbentuk adalah sebagai berikut.

Sehingga, tingginya adalah 5.

'''

class Node:
    def __init__(self, number=None):
        self.number = number
        self.left = None # type: BST
        self.right = None # type: BST


class BST:
    def __init__(self):
        self.root = None # type: Node

    def insert(self, number):
        if self.root is None:
            self.root = Node(number)
            self.root.left = BST()
            self.root.right = BST()
        elif number > self.root.number:
            self.root.right.insert(number)
        else:
            self.root.left.insert(number)

    def get_height(self):
        if self.root is None:
            return 0
        return (
            1 + max(self.root.right.get_height(), self.root.left.get_height()))


if __name__ == '__main__':
    input()  # Ignore the first input
    input_to_tree_list = list(map(int, input().split()))

    bst = BST()
    for num in input_to_tree_list:
        bst.insert(num)
    print(bst.get_height())
