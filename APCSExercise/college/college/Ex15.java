package com;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Ex15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] scores = new int[5];
        int sum = 0;

        // 輸入 5 個成績
        System.out.println("請輸入5個整數");
        for (int i = 0; i < 5; i++) {
            scores[i] = scanner.nextInt();
            sum += scores[i];
        }

        // 計算平均
        double average = sum / 5.0;

        // 計算低於平均的個數
        int belowAverageCount = 0;
        for (int score : scores) {
            if (score < average) {
                belowAverageCount++;
            }
        }

        // 輸出結果（平均保留兩位小數）
        DecimalFormat df = new DecimalFormat("0.00");
        System.out.println(df.format(average) + "," + belowAverageCount);
    }
}
