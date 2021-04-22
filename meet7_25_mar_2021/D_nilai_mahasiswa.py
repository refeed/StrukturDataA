'''
Nilai Mahasiswa
Batas Run-time: 	1 detik / test-case
Batas Memori: 	32 MB
DESKRIPSI SOAL

Buat program yang dapat menampung N data nilai mahasiswa (nilai).Nilai yang
diperbolehkan masuk adalah nilai yang berada diantara 0-100 (0<=nilai<=100).
kemudian, tampilkan kembali(yang dimasukkan terakhir ditampilkan terlebih
dahulu).
PETUNJUK MASUKAN

Input terdiri atas 2 baris. Baris pertama berisi sebuah bilangan bulat positif n
yang menyatakan banyak mahasiswa. Baris kedua berisi n buah bilangan bulat, yang
menyatakan nilai mahasiswa
PETUNJUK KELUARAN

Outputkan kembali data yang sesuai aturan, dan yang dimasukkan terakhir
ditampilkan terlebih dahulu
CONTOH MASUKAN

5
-1 2 -3 4 -5

CONTOH KELUARAN 1

4
2
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
    input_num = int(input())
    num_list = list(map(int, input().split()))[:input_num]

    stack = StackStr()
    for num in num_list:
        if 0 <= num <= 100:
            stack.push(num)

    while not stack.is_empty():
        print(stack.pop().data)
