def build_max_heap(collection, size, root):
    max_index = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    
    if left_child < size and collection[root] < collection[left_child]:
        max_index = left_child
        
    if right_child < size and collection[max_index] < collection[right_child]:
        max_index = right_child
        
    if max_index != root:
        collection[root], collection[max_index] = collection[max_index], collection[root]
        build_max_heap(collection, size, max_index)

def pyramid_sort(collection):
    n = len(collection)
    
    for i in range(n // 2 - 1, -1, -1):
        build_max_heap(collection, n, i)
        
    for i in range(n - 1, 0, -1):
        collection[i], collection[0] = collection[0], collection[i]
        build_max_heap(collection, i, 0)
    return collection

# Пример использования
data = [15, 9, 17, 3, 8, 12]
print("Исходные данные:", data)
pyramid_sort(data)
print("Упорядоченные данные:", data)
