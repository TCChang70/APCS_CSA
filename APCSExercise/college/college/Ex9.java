package com;

import java.util.Scanner;

public class Ex9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入兩個數字
        System.out.print("請輸入第一個整數：");
        int num1 = scanner.nextInt();

        System.out.print("請輸入第二個整數：");
        int num2 = scanner.nextInt();

        // 找出起點與終點
        int start = Math.min(num1, num2);
        int end = Math.max(num1, num2);

        int sum = 0;

        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                sum += i;
            }
        }

        System.out.println("介於 " + start + " 到 " + end + " 之間所有偶數的總和為：" + sum);
    }
}

