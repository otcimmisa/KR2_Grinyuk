import java.util.Arrays;

public class SequentialSearch {

    // Метод последовательного просмотра элементов
    public static int sequentialLookup(int[] data, int objective) {
        // Последовательно проверяем каждый элемент
        for (int index = 0; index < data.length; index++) {
            // Сравниваем с искомым значением
            if (data[index] == objective) {
                return index; // Возвращаем позицию найденного элемента
            }
        }
        return -1; // Элемент отсутствует в массиве
    }

    public static void main(String[] args) {
        int[] numbers = {8, 3, 6, 1, 9, 4, 2};
        int searchValue = 9; // Целевое значение

        System.out.println("Набор данных: " + Arrays.toString(numbers));
        System.out.println("Поиск значения: " + searchValue);

        // Выполняем поиск
        int foundIndex = sequentialLookup(numbers, searchValue);

        // Отображаем результат
        if (foundIndex != -1) {
            System.out.println("Значение обнаружено на позиции: " + foundIndex);
        } else {
            System.out.println("Значение не найдено в наборе");
        }
    }
}
