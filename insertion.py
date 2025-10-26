def element_by_element_sort(sequence):
    """
    Алгоритм последовательного упорядочивания элементов.
    Модифицирует исходную последовательность.
    """
    # Обрабатываем элементы начиная со второго
    for current_index in range(1, len(sequence)):
        current_element = sequence[current_index]  # Элемент для размещения
        previous_index = current_index - 1         # Позиция предыдущего элемента

        # Перемещаем элементы, превышающие текущий
        while previous_index >= 0 and sequence[previous_index] > current_element:
            sequence[previous_index + 1] = sequence[previous_index]  # Сдвиг вправо
            previous_index -= 1                    # Двигаемся левее

        # Размещаем элемент на найденной позиции
        sequence[previous_index + 1] = current_element

def display_sequence(sequence):
    """Отображение элементов последовательности."""
    print(*sequence)

# Демонстрация работы
if __name__ == "__main__":
    # Тестовый набор данных
    data = [18, 7, 15, 9, 4]

    print("Начальная последовательность:")
    display_sequence(data)

    # Выполняем упорядочивание
    element_by_element_sort(data)

    print("Обработанная последовательность:")
    display_sequence(data)
