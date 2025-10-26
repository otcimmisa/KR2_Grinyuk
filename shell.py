def diminishing_increment_sort(sequence):
    size = len(sequence)
    step = size // 2
    
    while step > 0:
        for current in range(step, size):
            temporary = sequence[current]
            position = current
            while position >= step and sequence[position - step] > temporary:
                sequence[position] = sequence[position - step]
                position -= step
            sequence[position] = temporary
        step //= 2
    return sequence

# Пример использования
data = [64, 23, 89, 12, 45]
print("Исходные данные:", data)
diminishing_increment_sort(data)
print("Упорядоченный массив:", data)
