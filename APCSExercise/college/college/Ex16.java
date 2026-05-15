package com;

import java.util.Scanner;

public class Ex16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入三個整數
        System.out.println("請輸入三個整數");
        int n1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        int n3 = scanner.nextInt();

        // 條件檢查
        if (n1 >= n2 || n1 < 0 || n2 < 0 || (n3 != 1 && n3 != 2)) {
            System.out.println("Error");
        } else {
            for (int i = n1; i <= n2; i++) {
                if (n3 == 1 && i % 2 != 0) { // 奇數
                    System.out.print(i + " ");
                } else if (n3 == 2 && i % 2 == 0) { // 偶數
                    System.out.print(i + " ");
                }
            }
        }
    }
}
