package chapter02;

public class SelectionSort {
    public static void main(String[] args) {
        int[] testArr = new int[]{1, 4, 7, 4, 9, 10};
        selectionSort(testArr);
        for (int sub : testArr) {
            System.out.print(sub + "->");
        }
    }

    /**
     * selection sort, no so fast. the default sort type in java util like Arrays is quick sort
     * @param arr
     */
    private static void selectionSort(int[] arr) {
        int length = arr.length;
        for (int i = 0; i < length; i++) {
            int smallest = arr[i];
            int position = i;
            // find the smallest element in array
            for (int j = i + 1; j < length; j++) {
                if (smallest > arr[j]) {
                    smallest = arr[j];
                    position = j;
                }
            }
            // after find smallest element, switch position
            int tmp = arr[i];
            arr[i] = smallest;
            arr[position] = tmp;
        }
    }
}
