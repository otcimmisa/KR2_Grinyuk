def recursive_divide_sort(collection, start=0, end=None):
    if end is None:
        end = len(collection) - 1
    
    if start < end:
        divider_index = rearrange_elements(collection, start, end)
        recursive_divide_sort(collection, start, divider_index - 1)
        recursive_divide_sort(collection, divider_index + 1, end)
    return collection

def rearrange_elements(collection, start, end):
    separator = collection[end]
    divider_position = start - 1
    
    for current_position in range(start, end):
        if collection[current_position] <= separator:
            divider_position += 1
            collection[divider_position], collection[current_position] = collection[current_position], collection[divider_position]
    
    collection[divider_position + 1], collection[end] = collection[end], collection[divider_position + 1]
    return divider_position + 1

# Пример использования
numbers = [29, 13, 47, 32, 8, 15]
print("Начальный набор:", numbers)
recursive_divide_sort(numbers)
print("Упорядоченный набор:", numbers)
