class Node:
    def __init__(self, nama_lengkap, nama_panggilan, niu):
        self.nama_lengkap = nama_lengkap
        self.nama_panggilan = nama_panggilan
        self.niu = niu
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_head(self, node: Node):
        if not self.head:
            self._add_first_node(node)
            return
        node.next = self.head
        self.head = node

    def add_tail(self, node: Node):
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

    def display_all_data(self):
        current_node = self.head
        index = 0
        while current_node:
            print(
                'Indeks ke-%d:\n'
                'nama_lengkap: %s\n'
                'nama_panggilan: %s\n'
                'niu: %d\n' % (
                    index, current_node.nama_lengkap,
                    current_node.nama_panggilan, current_node.niu))
            current_node = current_node.next
            index += 1

    def calculate_length(self):
        current_node = self.head
        length = 0
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def _add_first_node(self, node: Node):
        self.head = node
        self.tail = node

    def _remove_all_node(self):
        self.head = None
        self.tail = None


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.add_tail(Node('a', 'b', 123))
    linkedlist.add_tail(Node('b', 'b', 123))
    linkedlist.add_tail(Node('c', 'b', 123))
    linkedlist.add_head(Node('x', 'b', 123))
    linkedlist.add_head(Node('y', 'b', 123))
    linkedlist.add_head(Node('z', 'b', 123))
    linkedlist.display_all_data()
    print(linkedlist.calculate_length())
    linkedlist.remove_head()
    linkedlist.display_all_data()
    print(linkedlist.calculate_length())
