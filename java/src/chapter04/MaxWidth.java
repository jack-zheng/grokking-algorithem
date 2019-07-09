package chapter04;

public class MaxWidth {
    public static void main(String[] args) {
        System.out.println("168*64, max width = " + maxWidth(168, 64));
    }

    private static int maxWidth(int length, int width) {
        if (length % width == 0) {
            return width;
        }
        return maxWidth(width, length%width);
    }
}
