package chapter03;

public class Fact {
    public static void main(String[] args) {
        System.out.println("5! = " + fact(5));
    }

    private static int fact(int num) {
        if (num == 1) {
            return num;
        }
        return num * fact(num-1);
    }
}
