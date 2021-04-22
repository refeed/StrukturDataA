'''
CELENGAN KOIN
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Pak Blangkon baru saja membelikan hadiah celengan kepada anaknya, Blengki.
Celengan ini akan digunakan untuk menyimpan uang koin pecahan 10, 50, 100, 200,
500, dan 1000. Celengan yang dimiliki Blengki berbentuk tabung dan memiliki dua
buah penutup di atas dan di bawah, sehingga Blengki bisa memasukan dan mengambil
uang koin dari penutup tersebut, seperti pada gambar berikut:

Selama memiliki celengan tersebut, Blengki melakuan beberapa kegiatan yaitu
menggunakan uang koinnya untuk jajan maupun meletakan uang koin baru ke
celengan. Kegiatan-kegiatan yang dilakukan Blengki didefinisikan dengan kode
sebagai berikut:

Asumsi anda mengetahui kegiatan-kegiatan yang dilakukan Blengki tersebut,
buatlah program untuk menghitung berapa banyak uang yang ada dalam celengan yang
dimiliki Blengki setelah kegiatan itu dilakukan.
PETUNJUK MASUKAN

Baris pertama berisi dua bilangan bulat N yang menyatakan banyaknya kegiatan
yang dilakukan oleh Blengki. N baris berikutnya masing-masing baris terdiri
kegiatan yang dilakukan oleh Blengki.
PETUNJUK KELUARAN

Banyaknya uang yang ada pada celengan setelah kegiatan-kegiatan tersebut selesai
dilakukan dengan nilai awal celengan adalah 0.
CONTOH MASUKAN 1

5
0 1000
1 100
1 50
2 0
3 0

CONTOH KELUARAN 1

100

CONTOH MASUKAN 2

10
0 1000
0 100
1 50
1 200
2 0
0 100
3 0
2 0
1 50
3 0

CONTOH KELUARAN 1

1050
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListEmptyException(Exception):
    pass

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, node):
        if not self.head:
            self._add_first_node(node)
            return
        node.next = self.head
        self.head = node

    def add_tail(self, node):
        if not self.tail:
            self._add_first_node(node)
            return
        self.tail.next = node
        self.tail = node

    def is_empty(self):
        return (self.head == None) and (self.tail == None)

    def remove_head(self):
        if self.is_empty():
            raise LinkedListEmptyException()
        elif self.head == self.tail:
            self._remove_all_node()
            return
        self.head = self.head.next

    def remove_tail(self):
        if self.is_empty():
            raise LinkedListEmptyException()
        elif self.head == self.tail:
            self._remove_all_node()
            return

        # Iterate from head until we find the tail - 1 node (O(n))
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node

    def get_all_data(self):
        current_node = self.head

        output_data_list = []
        while current_node:
            output_data_list.append(current_node.data)
            current_node = current_node.next

        return output_data_list

    def calculate_length(self):
        current_node = self.head
        length = 0
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def _add_first_node(self, node):
        self.head = node
        self.tail = node

    def _remove_all_node(self):
        self.head = None
        self.tail = None


def evaluate_command(linkedlist, command_str):
    command, param = command_str.split()

    if command == '0':
        linkedlist.add_head(Node(int(param)))
    elif command == '1':
        linkedlist.add_tail(Node(int(param)))
    elif command == '2':
        linkedlist.remove_head()
    elif command == '3':
        linkedlist.remove_tail()


if __name__ == '__main__':
    num_commands = int(input())

    linkedlist = LinkedList()
    for _ in range(num_commands):
        try:
            evaluate_command(linkedlist, input())
        except LinkedListEmptyException:
            continue

    money_sum = 0
    for data in linkedlist.get_all_data():
        money_sum += data

    print(money_sum)
