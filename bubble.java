import java.util.Arrays;

public class ExchangeSort {

    // Метод упорядочивания массива через последовательное сравнение
    public static void sequentialSwapSort(int[] data) {
        int size = data.length;
        boolean wasSwapped; // Индикатор перемещений

        // Обработка элементов массива
        for (int pass = 0; pass < size - 1; pass++) {
            wasSwapped = false;
            // Сравнение пар элементов
            for (int position = 0; position < size - pass - 1; position++) {
                // Проверка порядка соседних элементов
                if (data[position] > data[position + 1]) {
                    // Перестановка элементов местами
                    int temporary = data[position];
                    data[position] = data[position + 1];
                    data[position + 1] = temporary;
                    wasSwapped = true; // Фиксация факта перестановки
                }
            }
            // Прерывание при отсутствии перемещений
            if (!wasSwapped) {
                break;
            }
        }
    }

    public static void main(String[] args) {
        int[] numbers = {58, 42, 19, 73, 26, 84, 15};

        System.out.println("Начальный массив: " + Arrays.toString(numbers));

        sequentialSwapSort(numbers);

        System.out.println("Упорядоченный массив: " + Arrays.toString(numbers));
    }
}
