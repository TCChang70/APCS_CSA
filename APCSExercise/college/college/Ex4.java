package com;

import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入一個年份：");
        int year = scanner.nextInt();

        boolean isLeapYear;

        if (year % 400 == 0) {
            isLeapYear = true;
        } else if (year % 4 == 0 && year % 100 != 0) {
            isLeapYear = true;
        } else {
            isLeapYear = false;
        }

        if (isLeapYear) {
            System.out.println(year + " 是閏年。");
        } else {
            System.out.println(year + " 不是閏年。");
        }
    }
}

