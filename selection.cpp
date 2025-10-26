#include <iostream>
#include <vector>

// Функция упорядочивания методом последовательного выбора
void sequentialSelectSort(std::vector<int>& data) {
    int size = data.size();

    // Обрабатываем каждый элемент как начальный неупорядоченной части
    for (int current = 0; current < size - 1; current++) {
        // Считаем текущий элемент минимальным
        int minPosition = current;

        // Ищем наименьший элемент в оставшейся части
        for (int next = current + 1; next < size; next++) {
            if (data[next] < data[minPosition]) {
                minPosition = next; // Запоминаем новую минимальную позицию
            }
        }

        // Перемещаем минимальный элемент на текущую позицию
        if (minPosition != current) {
            std::swap(data[current], data[minPosition]);
        }
    }
}

// Функция отображения элементов вектора
void displayVector(const std::vector<int>& data) {
    for (int value : data) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Тестовый набор чисел
    std::vector<int> numbers = {58, 32, 17, 45, 23};

    std::cout << "Начальный набор: ";
    displayVector(numbers);

    // Выполняем упорядочивание
    sequentialSelectSort(numbers);

    std::cout << "Обработанный набор: ";
    displayVector(numbers);

    return 0;
}
