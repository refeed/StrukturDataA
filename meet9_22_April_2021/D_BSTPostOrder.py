'''
Soal 1
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Diberikan n buah bilangan bulat, a1, a2, ..., an. Kemudian dibentuk binary
search tree dari barisan tersebut. Tugas Anda ialah mengoutputkan secara
postorder.
PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang
menyatakan a1, a2, ..., an
PETUNJUK KELUARAN

Outputkan secara preorder.
CONTOH MASUKAN

9
3 0 8 2 4 9 1 5 6

CONTOH KELUARAN 1

3
0
2
1
8
4
5
6
9

KETERANGAN

Pada contoh testcase, binary search tree yang terbentuk adalah sebagai berikut.
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

if __name__ == '__main__':
    input()  # Ignore the first input
    input_to_tree_list = list(map(int, input().split()))

    bst = BST()
    for num in input_to_tree_list:
        bst.insert(num)
    bst.postorder_print()
