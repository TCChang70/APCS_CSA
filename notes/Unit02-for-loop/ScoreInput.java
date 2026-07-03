import java.util.Scanner;
public class ScoreInput {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the math score: ");
        int mathScore=input.nextInt();
        System.out.print("Enter the chinese score: ");
        int chineseScore=input.nextInt();
        System.out.print("Enter the english score: ");
        int englishScore=input.nextInt();
        int totalScore = mathScore + chineseScore + englishScore;
        double averageScore = totalScore / 3.0;
        System.out.println("Total score: " + totalScore);
        System.out.println("Average score: " + averageScore);
        input.close();
        boolean isPass = averageScore >= 60;
        System.out.println("Pass: " + isPass);
    }
}
