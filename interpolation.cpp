#include <iostream>
#include <vector>

// Функция поиска с оценкой позиции
int estimatedPositionSearch(const std::vector<int>& data, int target) {
    int size = data.size();
    int left_bound = 0;
    int right_bound = size - 1;

    while (left_bound <= right_bound && target >= data[left_bound] && target <= data[right_bound]) {
        if (left_bound == right_bound) {
            if (data[left_bound] == target) return left_bound;
            return -1;
        }

        // Вычисление примерного местоположения
        int estimated_index = left_bound + (((double)(target - data[left_bound]) / 
                              (data[right_bound] - data[left_bound])) * (right_bound - left_bound));

        if (data[estimated_index] == target) {
            return estimated_index;
        }
        else if (data[estimated_index] < target) {
            left_bound = estimated_index + 1;
        }
        else {
            right_bound = estimated_index - 1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> numbers = {5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41};
    int search_value = 20;

    std::cout << "Набор чисел: ";
    for (int num : numbers) std::cout << num << " ";
    std::cout << "\nЦель поиска: " << search_value << std::endl;

    int position = estimatedPositionSearch(numbers, search_value);

    if (position != -1) {
        std::cout << "Найден на индексе: " << position << std::endl;
    } else {
        std::cout << "Не обнаружен в наборе" << std::endl;
    }

    return 0;
}
