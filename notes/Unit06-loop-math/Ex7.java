public class Ex7 {
    public static void main(String[] args) {
        outer: for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == j)
                    continue outer;
                System.out.print(i + "" + j + " ");
            }
        }
    }
}
