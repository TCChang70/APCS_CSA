package com;

import java.util.Scanner;

public class Ex12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入一個整數
        System.out.print("請輸入一個整數：");
        int number = scanner.nextInt();

        // 判斷正負或零
        if (number > 0) {
            System.out.println("這是一個正數。");
        } else if (number < 0) {
            System.out.println("這是一個負數。");
        } else {
            System.out.println("這是零。");
        }
    }
}

