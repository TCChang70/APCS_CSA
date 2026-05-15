package com;

import java.util.Scanner;

public class Ex8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入身高與體重
        System.out.print("請輸入身高（公分）：");
        double heightCm = scanner.nextDouble();

        System.out.print("請輸入體重（公斤）：");
        double weightKg = scanner.nextDouble();

        // 將身高轉換為公尺
        double heightM = heightCm / 100.0;

        // 計算 BMI
        double bmi = weightKg / (heightM * heightM);

        // 顯示 BMI 值（保留小數點後兩位）
        System.out.printf("您的 BMI 值為：%.2f\n", bmi);

        // 判斷體型狀態
        if (bmi < 18.5) {
            System.out.println("體型狀態：過輕");
        } else if (bmi < 24) {
            System.out.println("體型狀態：正常");
        } else if (bmi < 27) {
            System.out.println("體型狀態：過重");
        } else {
            System.out.println("體型狀態：肥胖");
        }
    }
}
