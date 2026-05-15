package com;

import java.util.Scanner;

public class Ex17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入一個整數：");
        int n = scanner.nextInt();

        // 階乘定義：0! = 1
        if (n < 0) {
            System.out.println("錯誤：階乘僅定義於非負整數！");
            return;
        }

        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }

        System.out.println(n + "! = " + factorial);
    }
}
