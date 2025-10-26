def split_and_combine(sequence):
    if len(sequence) <= 1:
        return sequence
    
    center = len(sequence) // 2
    first_part = sequence[:center]
    second_part = sequence[center:]
    
    first_part = split_and_combine(first_part)
    second_part = split_and_combine(second_part)
    
    return combine_parts(first_part, second_part)

def combine_parts(first, second):
    merged = []
    first_index = 0
    second_index = 0
    
    while first_index < len(first) and second_index < len(second):
        if first[first_index] < second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1
    
    merged.extend(first[first_index:])
    merged.extend(second[second_index:])
    
    return merged

# Пример использования
data = [56, 23, 78, 45, 12, 89, 34]
print("Исходные данные:", data)
ordered_data = split_and_combine(data)
print("Упорядоченные данные:", ordered_data)
