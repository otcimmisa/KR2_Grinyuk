def half_division_method(collection, item):
    start = 0
    end = len(collection) - 1
    
    while start <= end:
        middle = (start + end) // 2
        
        if collection[middle] == item:
            return middle
        elif collection[middle] > item:
            end = middle - 1
        else:
            start = middle + 1
    
    return None

# Демонстрация работы
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
desired = 8
position = half_division_method(numbers, desired)
if position is not None:
    print(f"Найден в ячейке: {position}")
else:
    print("Не обнаружено")