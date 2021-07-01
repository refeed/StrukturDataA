'''
RAFID ASLAM
NIM: 20/464402/SV/18721

Tugas 27 Mei 2021

Sequence, binary, insert open address, search yg open address, sm slide
'''


def is_number_in_the_list_seq_search(num_to_search, num_list):
    is_found = False
    for num in num_list:
        if num == num_to_search:
            is_found = True
            break

    return is_found


def is_number_in_the_list_binary_search(num_to_search, num_list):
    low_idx = 0
    high_idx = len(num_list) - 1

    is_found = False
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        mid_num = num_list[mid_idx]

        if mid_num == num_to_search:
            is_found = True
            break
        elif num_to_search > mid_num:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1

    return is_found


class HashWithOpenAdressCollisionResolver:
    def __init__(self, size) -> None:
        self._list = []
        self.size = size
        for _ in range(size):
            self._list.append(None)

    def insert(self, num):
        orig_idx = self._hash_function(num)
        offset_from_orig_idx = 0

        current_idx = (orig_idx + offset_from_orig_idx) % self.size
        while (self._list[current_idx] is not None and
               offset_from_orig_idx < self.size):
            offset_from_orig_idx += 1
            current_idx = (orig_idx + offset_from_orig_idx) % self.size

        self._list[current_idx] = num

    def search_idx(self, num):
        orig_idx = self._hash_function(num)
        offset_from_orig_idx = 0

        current_idx = (orig_idx + offset_from_orig_idx) % self.size
        while (self._list[current_idx] != num and
               offset_from_orig_idx < self.size):
            offset_from_orig_idx += 1
            current_idx = (orig_idx + offset_from_orig_idx) % self.size

        if self._list[current_idx] == num:
            return current_idx
        return -1

    def _hash_function(self, num):
        return num % 7
