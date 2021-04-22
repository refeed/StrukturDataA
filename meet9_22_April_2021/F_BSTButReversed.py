'''
Cermin Tree
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Membentuk Cermin Tree dari N data (N<=0), tp tidak boleh ada angka yang sama.

Cermin Tree adalah efek Tree yang dicerminkan. Kita tahu efek dari suatu cermin
adalah membalik yang kanan menjadi kiri dan sebaliknya. Sehingga Cermin Tree
adalah suatu Tree dimana node dengan angka yang lebih besar berada di kiri dan
yang lebih kecil berada di kanan

Anda diminta untuk menampilkan cermin tree ini dalam preOrder, InOrder dan
PostOrder
PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak angka. Baris kedua berisi n buah bilangan bulat, yang
akan digunakan untuk membentuk tree
PETUNJUK KELUARAN

outputkan 3 baris.

baris 1: output preorder, pisahkan setiap angka dengan spasi

baris 2: output inorder, pisahkan setiap angka dengan spasi

baris 3: output postorder, pisahkan setiap angka dengan spasi
CONTOH MASUKAN

5
4 5 5 6 2

CONTOH KELUARAN

4 5 6 2
6 5 4 2
6 5 2 4

CONTOH MASUKAN

6
1 1 1 1 1 1

CONTOH KELUARAN

1
1
1

'''
import sys


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
        elif number == self.root.number:
            return
        elif number < self.root.number:  # The whole point of this solution
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
        sys.stdout.write(str(self.root.number) + ' ')

    def preorder_print(self):
        if self.root is None:
            return
        sys.stdout.write(str(self.root.number) + ' ')
        self.root.left.preorder_print()
        self.root.right.preorder_print()

    def inorder_print(self):
        if self.root is None:
            return
        self.root.left.inorder_print()
        sys.stdout.write(str(self.root.number) + ' ')
        self.root.right.inorder_print()


if __name__ == '__main__':
    input()  # Ignore the first input
    input_to_tree_list = list(map(int, input().split()))

    bst = BST()
    for num in input_to_tree_list:
        bst.insert(num)
    bst.preorder_print()
    print()
    bst.inorder_print()
    print()
    bst.postorder_print()
    print()
