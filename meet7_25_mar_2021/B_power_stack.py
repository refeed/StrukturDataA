'''
Power Stack Batas Run-time:     1 detik / test-case Batas Memori:   32 MB
DESKRIPSI SOAL

Buat sebuah program visualisasi Stack. Anda akan diberikan 4 jenis inputan
sebanyak N kali. Tampilkan kondisi setiap akhir eksekusi perintah tersebut.
Daftar perintahnya sebagai berikut:

    PUSH X

    : Melakukan proses push pada stack nilai X

    POP

    : Melakukan proses pop pada stack

    POWPUSH Y X

    : Melakukan proses push pada stack nilai X sebanyak Y kali

    POWPOP Y

    : Melakukan proses pop pada stack sebanyak Y kali

PETUNJUK MASUKAN

Baris pertama adalah bilangan bulat N, banyak perintah yang akan diinputkan. N
baris berikutnya terdapat salah satu dari perintah di atas. N < 30. PETUNJUK
KELUARAN

Sebuah visualisasi stack sesuai format contoh. Tangani juga ketika user
melakukan pop pada stack kosong. CONTOH MASUKAN

12 PUSH 6 PUSH 4 POP POWPUSH 4 2 POP POWPOP 3 POP POP PUSH 3 POP POWPUSH 2 2
POWPOP 4

CONTOH KELUARAN

[ 6 ] [ 6 4 ] [ 6 ] [ 6 2 2 2 2 ] [ 6 2 2 2 ] [ 6 ]
[ ]
ERROR: STACK KOSONG [ 3 ]
[ ]
[ 2 2 ] ERROR: STACK KOSONG

KETERANGAN

Untuk mengoutputkan tidak harus dilakukan bersamaan diakhir. Outputkan satu
persatu setiap setelah malakukan aksi akan dianggap jawaban yang benar. Untuk
perintah yang diawali POW, cukup tampilkan tampilan terakhir. PENILAIAN

Untuk mendapatkan 100% kerjakan ketiga poin dibawah. Tapi mengerjakan salah
satunya sudah cukup untuk mendapat nilai.

Jika program sanggup menghandle PUSH dan POP = 20 poin

Jika program sanggup menghandle POWPUSH dan POWPOP = 20 poin

Jika program sanggup menghandle tampilan eror ketika pop = 20 poin
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


class StackInt:
    def __init__(self):
        self._stack = LinkedList()

    def push(self, number):
        self._stack.add_head(Node(int(number)))

    def pop(self):
        head = self._stack.head
        self._stack.remove_head()
        return head

    def is_empty(self):
        return self._stack.is_empty()

    def display(self):
        if self._stack.is_empty():
            print('[ ]')
            return

        stack_data_str_list = map(str, reversed(self._stack.get_all_data()))
        output_str_list = ' '.join(stack_data_str_list)
        output_str_list = '[ ' + output_str_list + ' ]'
        print(output_str_list)


class StackKosongException(Exception):
    pass

def evaluate_command(stack, command_str):
    command_str = command_str.split()
    command = command_str[0]
    params_str_list = command_str[1:]

    if command == 'PUSH':
        stack.push(params_str_list[0])
    elif command == 'POP':
        if stack.is_empty():
            raise StackKosongException()
        stack.pop()
    elif command == 'POWPUSH':
        for _ in range(int(params_str_list[0])):
            stack.push(int(params_str_list[1]))
    elif command == 'POWPOP':
        for _ in range(int(params_str_list[0])):
            if stack.is_empty():
                raise StackKosongException()
            stack.pop()
    stack.display()


if __name__ == '__main__':
    num_commands = int(input())

    stack = StackInt()
    commands_str_list = []
    for _ in range(num_commands):
        commands_str_list.append(input())

    for command in commands_str_list:
        try:
            evaluate_command(stack, command)
        except StackKosongException:
            print('ERROR: STACK KOSONG')
