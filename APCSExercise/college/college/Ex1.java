package com;
import java.util.Scanner;
import java.text.DecimalFormat;

public class Ex1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入三個整數
        System.out.print("請輸入成績 A：");
        int scoreA = scanner.nextInt();

        System.out.print("請輸入成績 B：");
        int scoreB = scanner.nextInt();

        System.out.print("請輸入學期加分：");
        int bonus = scanner.nextInt();

        // 計算初始平均
        double average = (scoreA + scoreB) / 2.0;
        double finalScore = average;

        // 若平均 > 60，加入學期加分
        if (average > 60) {
            finalScore += bonus;
        }

        // 若 A 或 B > 60，額外加 1 分
        if (scoreA > 60 || scoreB > 60) {
            finalScore += 1;
        }

        // 格式化輸出到小數點第二位
        DecimalFormat df = new DecimalFormat("0.00");
        System.out.println("最終總成績為：" + df.format(finalScore));
    }
}
