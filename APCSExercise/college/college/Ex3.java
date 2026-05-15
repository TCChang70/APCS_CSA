package com;

import java.util.Scanner;

public class Ex3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入一個介於 0 到 100 的分數：");
        int score = scanner.nextInt();

        // 簡單的輸入範圍檢查
        if (score < 0 || score > 100) {
            System.out.println("錯誤：分數必須介於 0 到 100 之間！");
        } else {
            char grade;

            if (score >= 90) {
                grade = 'A';
            } else if (score >= 80) {
                grade = 'B';
            } else if (score >= 70) {
                grade = 'C';
            } else if (score >= 60) {
                grade = 'D';
            } else {
                grade = 'F';
            }

            System.out.println("該分數的等級為：" + grade);
        }
    }
}

