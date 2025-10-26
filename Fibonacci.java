import java.util.Arrays;

public class GoldenRatioSearch {

    // Генерация последовательности до достижения нужного размера
    public static int generateSequence(int size) {
        int fibPrev = 0;
        int fibCurr = 1;
        int fibNext = fibPrev + fibCurr;

        while (fibNext < size) {
            fibPrev = fibCurr;
            fibCurr = fibNext;
            fibNext = fibPrev + fibCurr;
        }
        return fibNext;
    }

    // Поиск с использованием золотого сечения
    public static int goldenRatioSearch(int[] data, int target) {
        int length = data.length;

        int fibPrev = 0;
        int fibCurr = 1;
        int fibNext = fibPrev + fibCurr;

        while (fibNext < length) {
            fibPrev = fibCurr;
            fibCurr = fibNext;
            fibNext = fibPrev + fibCurr;
        }

        int position = -1;

        while (fibNext > 1) {
            int checkIndex = Math.min(position + fibPrev, length - 1);

            if (data[checkIndex] < target) {
                fibNext = fibCurr;
                fibCurr = fibPrev;
                fibPrev = fibNext - fibCurr;
                position = checkIndex;
            }
            else if (data[checkIndex] > target) {
                fibNext = fibPrev;
                fibCurr = fibCurr - fibPrev;
                fibPrev = fibNext - fibCurr;
            }
            else {
                return checkIndex;
            }
        }

        if (fibCurr == 1 && position + 1 < length && data[position + 1] == target) {
            return position + 1;
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] numbers = {15, 25, 38, 42, 55, 63, 77, 81, 89, 95, 105};
        int searchValue = 89;

        System.out.println("Набор чисел: " + Arrays.toString(numbers));
        System.out.println("Цель поиска: " + searchValue);

        int index = goldenRatioSearch(numbers, searchValue);

        if (index != -1) {
            System.out.println("Объект расположен на индексе: " + index);
        } else {
            System.out.println("Объект отсутствует в наборе");
        }
    }
}
