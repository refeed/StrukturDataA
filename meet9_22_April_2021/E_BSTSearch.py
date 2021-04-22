'''
Soal 4
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary
search tree dari barisan tersebut. Tugas Anda ialah menentukan apakah terdapat
bilangan k pada binary search tree yang terbentuk. Untuk lebih jelasnya,
perhatikan contoh testcase di bawah.
PETUNJUK MASUKAN

Input terdiri atas 3 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang
menyatakan a1, a2, ..., an. Baris ketiga berisi sebuah bilangan bulat k yang
menyatakan bilangan yang akan ditanyakan.
PETUNJUK KELUARAN

Outputkan "YA" jika terdapat bilangan k pada binary search tree yang terbentuk,
atau outputkan "TIDAK" jika tidak terdapat bilangan k pada binary search tree
yang terbentuk.
CONTOH MASUKAN 1

9
3 0 8 2 4 9 1 5 6
0

CONTOH KELUARAN 1

YA

CONTOH MASUKAN 2

9
3 0 8 2 4 9 1 5 6
7

CONTOH KELUARAN 2

TIDAK

KETERANGAN

Pada kedua contoh, binary search tree yang terbentuk adalah sebagai berikut.

Pada contoh pertama, outputnya adalah "YA", karena terdapat bilangan 0 pada
binary search tree yang terbentuk.

Pada contoh kedua, outputnya adalah "TIDAK", karena tidak terdapat bilangan 7
pada binary search tree yang terbentuk.
'''


class Node:
    def __init__(self, number=None):
        self.number = number
        self.left = None  # type: BST
        self.right = None  # type: BST


class BST:
    def __init__(self):
        self.root = None  # type: Node

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

    def get_leaf_num(self):
        if self.root is None:
            return 0
        elif self.root.left.root is None and self.root.right.root is None:
            return (1 +
                    self.root.left.get_leaf_num() + self.root.right.get_leaf_num())
        return (self.root.left.get_leaf_num() + self.root.right.get_leaf_num())

    def postorder_print(self):
        if self.root is None:
            return
        self.root.left.postorder_print()
        self.root.right.postorder_print()
        print(self.root.number)

    def preorder_print(self):
        if self.root is None:
            return
        print(self.root.number)
        self.root.left.preorder_print()
        self.root.right.preorder_print()

    def check_does_num_exist(self, number):
        if self.root is None:
            return False
        elif self.root.number == number:
            return True
        elif self.root.number > number:
            return self.root.left.check_does_num_exist(number)
        return self.root.right.check_does_num_exist(number)


if __name__ == '__main__':
    input()  # Ignore the first input
    input_to_tree_list = list(map(int, input().split()))
    num_to_search = int(input())

    bst = BST()
    for num in input_to_tree_list:
        bst.insert(num)

    if bst.check_does_num_exist(num_to_search):
        print('YA')
    else:
        print('TIDAK')
