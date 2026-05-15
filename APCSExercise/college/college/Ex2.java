package com;

import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int oddCount = 0;
        int evenCount = 0;

        System.out.println("請輸入 5 個整數：");
        for (int i = 1; i <= 5; i++) {
            System.out.print("輸入第 " + i + " 個整數：");
            int number = scanner.nextInt();

            if (number % 2 == 0) {
                evenCount++;  // 偶數
            } else {
                oddCount++;   // 奇數
            }
        }

        System.out.println("奇數的個數為：" + oddCount);
        System.out.println("偶數的個數為：" + evenCount);
    }
}
