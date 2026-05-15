package com;

import java.util.Scanner;

public class Ex23 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入一個正整數 n（n > 0）：");
        int n = scanner.nextInt();

        if (n <= 0) {
            System.out.println("輸入錯誤，n 必須大於 0。");
            return;
        }

        // 列印 n 列星號
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println(); // 換行
        }
    }
}

