package chapter01;

public class BinarySearch {
    public static void main(String[] args) {
        int[] src = new int[100];
        for(int i=0;i<100;i++) {
            src[i] = i;
        }
        System.out.println("Guess position: " + binarySearch(src, 32));
    }

    private static int binarySearch(int[] src, int guess) {
        int low = 0;
        int high = src.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (src[mid] < guess)
                low = mid + 1;
            if (src[mid] > guess)
                high = mid - 1;
            if (src[mid] == guess)
                return mid;
        }
        return -1;
    }

    /**
     * This is the official impl of binarySearch, almost the same with my implementation exception the
     * way to get mid position, it use bit operation to get it.
     * @param a
     * @param fromIndex
     * @param toIndex
     * @param key
     * @return
     */
    private static int binarySearch0(int[] a, int fromIndex, int toIndex,
                                     int key) {
        int low = fromIndex;
        int high = toIndex - 1;

        while (low <= high) {
            int mid = (low + high) >>> 1;
            int midVal = a[mid];

            if (midVal < key)
                low = mid + 1;
            else if (midVal > key)
                high = mid - 1;
            else
                return mid; // key found
        }
        return -(low + 1);  // key not found.
    }
}
