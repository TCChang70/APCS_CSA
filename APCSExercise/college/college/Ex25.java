package com;

public class Ex25 {
    public static void main(String[] args) {
        System.out.println("1 到 50 之間能被 3 或 5 整除的數字：");

        for (int i = 1; i <= 50; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                System.out.print(i + " ");
            }
        }

        System.out.println(); // 換行
    }
}
