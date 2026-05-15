package com;

import java.util.Scanner;

public class Ex7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入三個邊長
        System.out.print("請輸入第一個邊長：");
        int a = scanner.nextInt();

        System.out.print("請輸入第二個邊長：");
        int b = scanner.nextInt();

        System.out.print("請輸入第三個邊長：");
        int c = scanner.nextInt();

        // 三角形存在條件：任兩邊和大於第三邊
        boolean isTriangle = (a + b > c) && (a + c > b) && (b + c > a);

        if (!isTriangle) {
            System.out.println("錯誤：這三個邊長無法構成合法的三角形！");
        } else {
            // 判斷三角形類型
            if (a == b && b == c) {
                System.out.println("這是等邊三角形。");
            } else if (a == b || a == c || b == c) {
                System.out.println("這是等腰三角形。");
            } else {
                System.out.println("這是不等邊三角形。");
            }
        }
    }
}
