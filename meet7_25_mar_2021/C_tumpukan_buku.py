'''
Tumpukan Buku
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Di rumah Pak Blangkon akan diadakan syukuran. Dengan demikian Pak Blangkon
melakukan bersih-bersih ruang bukunya. Pak Blangkon akan dibantu oleh anaknya.
Karena sang anak tidak mengetahui mana buku yang penting atau tidak, maka sang
anak akan menumpuk buku-buku tersebut, kemudian, ketika buku yang ditumpuk
merupakan buku yang tidak penting, maka Pak Blangkon akan segera mengambilnya.

Kegiatan tersebut dikodekan dengan cara berikut ini:

T a1 aku => taruh buku dengan kode a1 dan judul aku ditumpukan paling atas.

A => ambil buku ditumpukan paling atas.
PETUNJUK MASUKAN

Baris pertama berisi bilangan bulat N yang menyatakan banyaknya aksi.

N baris berikutnya masing-masing terdiri dari kode kegiatan seperti pada aturan
soal.
PETUNJUK KELUARAN

List kode buku dan judul buku penting urut dari buku paling atas
CONTOH MASUKAN

4
T 3 H
A
T 2 P
T 1 S

CONTOH KELUARAN

1 S
2 P

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            raise Exception('The LinkedList is empty')
        elif self.head == self.tail:
            self._remove_all_node()
            return
        self.head = self.head.next

    def remove_tail(self):
        if self.is_empty():
            raise Exception('The LinkedList is empty')
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


class StackStr:
    def __init__(self):
        self._stack = LinkedList()

    def push(self, data):
        self._stack.add_head(Node(data))

    def pop(self):
        head = self._stack.head
        self._stack.remove_head()
        return head

    def is_empty(self):
        return self._stack.is_empty()

    def display(self):
        for data in self._stack.get_all_data():
            print(data)


def evaluate_command(stack, command_str):
    command_str = command_str.split()
    command = command_str[0]
    params_str_list = command_str[1:]

    if command == 'T':
        stack.push(' '.join(params_str_list))
    elif command == 'A':
        if stack.is_empty():
            return
        stack.pop()


if __name__ == '__main__':
    num_commands = int(input())

    stack = StackStr()
    commands_str_list = []
    for _ in range(num_commands):
        evaluate_command(stack, input())

    stack.display()
