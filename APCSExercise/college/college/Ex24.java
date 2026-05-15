package com;

import java.util.Scanner;

public class Ex24 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入兩條直角邊長
        System.out.print("請輸入第一條直角邊長（a）：");
        double a = scanner.nextDouble();

        System.out.print("請輸入第二條直角邊長（b）：");
        double b = scanner.nextDouble();

        // 計算斜邊長度
        double c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));

        // 輸出結果（保留小數點第二位）
        System.out.printf("斜邊長度為：%.2f\n", c);
    }
}

