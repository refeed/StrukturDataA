'''
CariDeleteNode
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Binary Search Tree (BST) adalah suatu keadaan dimana setiap node X, semua elemen
di subpohon kirinya bernilai lebih kecil dari nilai X dan semua elemen di
subpohon kanannya bernilai lebih besar dari nilai X. Oleh Karena itu, saat akan
menghapus sebuah node, kita juga harus memikirkan seluruh node anak dari node
tsb. Hal penting adalah agar pohon setelah dihapus tetap merupakan BST

Ada 3 kasus dalam penghapusan Node.

1. Node merupakan leaf/daun. Pada kasus ini, penghapusan bisa langsung
   dilakukan.

2. Pada kasus Node memiliki degree 1, maka node anak bisa langsung menggantikan
   posisinya.

3. Kasus terakhir menjadi sedikit rumit, yaitu ketika Node memiliki degree 2.
   Pada kasus ini, maka harus dipilih node yang bisa menggantikan. Node yang
   dapat menggantikan adalah Node yang nilainya terbesar dari dari subpohon
   sebelah kirinya. perlu diingat, jika suatu Node digunakan untuk menggantikan
   posisi dari suatu node lain, maka posisinya seperti dilakukan penghapusan.

Buatlah Program yang meminta input deret angka, kemudian susunlah menjadi suatu
tree, kemudian pilihlah Node mana yang layak menggantikan.
PETUNJUK MASUKAN

Input terdiri atas 3 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak bilangan. Baris kedua berisi n buah bilangan bulat, yang
menyatakan a1, a2, ..., an

Baris 3 menunjukkan Node yang akan dihapus
PETUNJUK KELUARAN

Outputkan Node mana yang layak menggantikan. Jika tidak perlu digantikan Node
lain, maka outputkan -1
CONTOH MASUKAN

9
8 9 4 6 5 2 1 3 7
1

CONTOH KELUARAN

-1

CONTOH MASUKAN

9
8 9 4 6 5 2 1 3 7
6

CONTOH KELUARAN

5

CONTOH MASUKAN

9
8 9 4 6 5 2 1 3 7
8

CONTOH KELUARAN

7
'''
import math


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
        if get_node_with_number(number) is not None:
            return True
        return False

    def get_node_with_number(self, number):
        # type: (int) -> Optional[Node]
        if self.root is None:
            return None
        elif self.root.number == number:
            return self.root
        elif self.root.number > number:
            return self.root.left.get_node_with_number(number)
        return self.root.right.get_node_with_number(number)

    def get_max(self):
        if self.root is None:
            return -math.inf
        return max(self.root.number, self.root.left.get_max(),
                   self.root.right.get_max())

    def get_min(self):
        if self.root is None:
            return math.inf
        return min(self.root.number, self.root.left.get_min(),
                   self.root.right.get_min())

    def decide_which_node_should_replace_it(self, number_tobe_deleted):
        node = self.get_node_with_number(number_tobe_deleted)
        if node is None:
            # If the node isn't found
            return -1
        elif node.right.root is None and node.left.root is None:
            # If it's leaf
            return -1
        elif node.left.root is not None and node.right.root is not None:
            return node.left.get_max()
        elif node.left.root is not None:
            return node.left.root.number
        elif node.right.root is not None:
            return node.right.root.number


if __name__ == '__main__':
    input()  # Ignore the first input
    input_to_tree_list = list(map(int, input().split()))
    number_tobe_deleted = int(input())

    bst = BST()
    for num in input_to_tree_list:
        bst.insert(num)

    print(bst.decide_which_node_should_replace_it(number_tobe_deleted))
