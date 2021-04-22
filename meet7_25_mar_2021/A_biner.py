'''
Int to Biner Batas Run-time:     1 detik / test-case Batas Memori:   32 MB
DESKRIPSI SOAL

Diberikan suatu angka integer N (0 <= N <= 32000), ubahlah angka tersebut
menjadi angka biner.

PETUNJUK MASUKAN

Terdapat satu baris bilangan bulat N yang menyatakan angka yang akan diubah
menjadi biner.

PETUNJUK KELUARAN

List angka kombinasi angka 1 dan 0 yang merupakan angka biner dari N CONTOH
MASUKAN

8

CONTOH KELUARAN

1000

CONTOH MASUKAN

0

CONTOH KELUARAN

0

CONTOH MASUKAN

7

CONTOH KELUARAN

111
'''
import sys

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


class StackInt:
    def __init__(self):
        self._stack = LinkedList()

    def push(self, number):
        self._stack.add_head(Node(number))

    def pop(self):
        head = self._stack.head
        self._stack.remove_head()
        return head

    def is_empty(self):
        return self._stack.is_empty()

if __name__ == '__main__':
    num_int = int(input())

    if num_int == 0:
        print('0')
        sys.exit(0)

    stack = StackInt()
    while num_int != 0:
        if num_int % 2 == 0:
            stack.push(0)
        else:
            stack.push(1)
        num_int = num_int // 2

    binary_repr_str_list = []
    while not stack.is_empty():
        binary_repr_str_list.append(str(stack.pop().data))

    print(''.join(binary_repr_str_list))

