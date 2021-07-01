# Tugas 1 Rafid Aslam
from queue import Queue


BLOCKED_NODES_SET = {
    'A2', 'A3', 'A4', 'A5',
    'B2', 'B4',
    'C4', 'C6',
    'D4',
    'E2', 'E4', 'E5',
    'F2'
}

FINISH_A_NODE = 'A6'
FINISH_B_NODE = 'F1'
START_NODE = 'C1'

graph_dict = {}


def is_valid_node(node_str):
    char, num = node_str
    num = int(num)
    if (not (ord('A') <= ord(char) <= ord('F')) or
            not (1 <= num <= 6)):
        return False
    return True


def get_node_around_str(node_str, location_num):
    '''
    :param node_str:      The node_str
    :param location_num:  0 for top, 1 right, 2 bottom, 3 left
    :return:              Node str after the operation is done or None
    '''
    char, num = node_str
    num = int(num)

    if location_num == 0:
        char = chr(ord(char) - 1)
    elif location_num == 1:
        num += 1
    elif location_num == 2:
        char = chr(ord(char) + 1)
    elif location_num == 3:
        num -= 1

    num = str(num)
    result_node = char + num

    if not is_valid_node(result_node):
        return None
    return result_node


# Build the graph
for char_ord in range(ord('A'), ord('F') + 1):
    for num in range(1, 6 + 1):
        char = chr(char_ord)
        node_str = char + str(num)

        if node_str in BLOCKED_NODES_SET:
            continue

        for location_num in range(0, 3 + 1):
            neighbour_node = get_node_around_str(node_str, location_num)

            if (neighbour_node is None or
                    neighbour_node in BLOCKED_NODES_SET):
                continue

            try:
                graph_dict[node_str].append(neighbour_node)
            except KeyError:
                graph_dict[node_str] = [neighbour_node]


def generate_backtrack_path(end_node, parent_nodes_dict):
    path_list = []

    current_node = end_node
    while current_node is not None:
        path_list.append(current_node)
        # Hanya memilih satu jalan yang mungkin
        current_node = parent_nodes_dict[current_node][0]

    path_list.reverse()
    return path_list


def generate_bfs_maze_path_solution(start_node, finish_node):
    bfs_queue = Queue()
    bfs_queue.put(start_node)

    traversed_nodes_list = []
    parent_nodes_dict = {start_node: [None]}  # Initialize with one start node

    while not bfs_queue.empty():
        current_node_traversed = bfs_queue.get()
        if current_node_traversed in traversed_nodes_list:
            continue

        traversed_nodes_list.append(current_node_traversed)
        if current_node_traversed == finish_node:
            break

        for neighbour_node in graph_dict[current_node_traversed]:
            if neighbour_node in traversed_nodes_list:
                # Tidak boleh balik
                continue

            bfs_queue.put(neighbour_node)

            try:
                parent_nodes_dict[neighbour_node].append(
                    current_node_traversed)
            except KeyError:
                parent_nodes_dict[neighbour_node] = [current_node_traversed]

    solution_path = generate_backtrack_path(finish_node, parent_nodes_dict)

    return solution_path


def generate_dfs_maze_path_solution(start_node, finish_node):
    dfs_stack_list = []
    dfs_stack_list.append(start_node)

    traversed_nodes_list = []
    parent_nodes_dict = {start_node: [None]}  # Initialize with one start node

    while len(dfs_stack_list) != 0:
        current_node_traversed = dfs_stack_list.pop()
        if current_node_traversed in traversed_nodes_list:
            continue

        traversed_nodes_list.append(current_node_traversed)
        if current_node_traversed == finish_node:
            break

        for neighbour_node in graph_dict[current_node_traversed]:
            if neighbour_node in traversed_nodes_list:
                # Tidak boleh balik
                continue

            dfs_stack_list.append(neighbour_node)

            try:
                parent_nodes_dict[neighbour_node].append(
                    current_node_traversed)
            except KeyError:
                parent_nodes_dict[neighbour_node] = [current_node_traversed]

    solution_path = generate_backtrack_path(finish_node, parent_nodes_dict)

    return solution_path


print('Dengan BFS')
print('----------')
print('FINISH A:')
solution_bfs_path = generate_bfs_maze_path_solution(START_NODE, FINISH_A_NODE)
print(solution_bfs_path)
print('Panjang langkah (termasuk start dan finish)', len(solution_bfs_path))
print()
print('FINISH B:')
solution_bfs_path = generate_bfs_maze_path_solution(START_NODE, FINISH_B_NODE)
print(solution_bfs_path)
print('Panjang langkah (termasuk start dan finish)', len(solution_bfs_path))
print()
print()
print('Dengan DFS')
print('----------')
print('FINISH A:')
solution_bfs_path = generate_dfs_maze_path_solution(START_NODE, FINISH_A_NODE)
print(solution_bfs_path)
print('Panjang langkah (termasuk start dan finish)', len(solution_bfs_path))
print()
print('FINISH B:')
solution_bfs_path = generate_dfs_maze_path_solution(START_NODE, FINISH_B_NODE)
print(solution_bfs_path)
print('Panjang langkah (termasuk start dan finish)', len(solution_bfs_path))
