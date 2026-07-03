public class OP3 {
    public static void main(String[] args) {
        // Math score=59
        int score= 59;
        // Student John's age=20
        int age = 20;
        /*
         * Check if the student passed the math exam and is of legal age.
         */
        boolean isPassed = (score >= 60) && (age >= 18);
        System.out.println(isPassed);
    }
}
