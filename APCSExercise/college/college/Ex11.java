package com;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Ex11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入三個成績
        System.out.print("請輸入第一個成績：");
        int score1 = scanner.nextInt();

        System.out.print("請輸入第二個成績：");
        int score2 = scanner.nextInt();

        System.out.print("請輸入第三個成績：");
        int score3 = scanner.nextInt();

        // 計算總和與平均
        int total = score1 + score2 + score3;
        double average = total / 3.0;

        // 計算最高分
        int highest = Math.max(score1, Math.max(score2, score3));

        // 平均保留小數點兩位
        DecimalFormat df = new DecimalFormat("0.00");

        // 輸出結果
        System.out.println("總分：" + total);
        System.out.println("平均：" + df.format(average));
        System.out.println("最高分：" + highest);
    }
}
