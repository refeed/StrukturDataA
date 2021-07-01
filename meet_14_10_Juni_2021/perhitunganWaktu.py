import sorting
import timeit

data = [1, 8, 3, 5, 6, 9, 2, 4]

start_time = timeit.default_timer()
sorting.bubble(data)
end_time = timeit.default_timer()
print('Bubble Sort      : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.bucket(data)
end_time = timeit.default_timer()
print('Bucket Sort      : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.comb(data)
end_time = timeit.default_timer()
print('Comb Sort        : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.counting(data)
end_time = timeit.default_timer()
print('Counting Sort    : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.maxheap(data)
end_time = timeit.default_timer()
print('Max Heap Sort    : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.minheap(data)
end_time = timeit.default_timer()
print('Min Heap Sort    : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.merge(data)
end_time = timeit.default_timer()
print('Merge Sort       : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.quick(data)
end_time = timeit.default_timer()
print('Quick Sort       : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.radix(data)
end_time = timeit.default_timer()
print('Radix Sort       : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.selection(data)
end_time = timeit.default_timer()
print('Selection Sort   : ', '%.15f' % (end_time - start_time))

start_time = timeit.default_timer()
sorting.cycle(data)
end_time = timeit.default_timer()
print('Cycle Sort       : ', '%.15f' % (end_time - start_time))
