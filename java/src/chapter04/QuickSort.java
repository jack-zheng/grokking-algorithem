package chapter04;

public class QuickSort {
    public static void main(String[] args) {
        int[] test = new int[]{4,6,2,8,0,1,3};
        quickSort(test, 0, test.length-1);
        for (int sub : test) {
            System.out.print(sub + " ");
        }
    }
    private static void quickSort(int[] arr, int left, int right) {
        if (left > right)
            return;
        int pivot = partition(arr, left, right);
        quickSort(arr, left, pivot-1);
        quickSort(arr, pivot+1, right);
    }

    /**
     * About the partition, you can refer to this blog, the picture is nice for you to understand this algorithm.
     *  https://www.cnblogs.com/MOBIN/p/4681369.html
     * @param arr
     * @param left
     * @param right
     * @return
     */
    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[left];
        while (left != right) {
            while (arr[right] > pivot && left < right)
                right--;
            arr[left] = arr[right];
            while (arr[left] < pivot && left < right)
                left++;
            arr[right] = arr[left];
        }
        arr[left] = pivot;
        return left;
    }
}
