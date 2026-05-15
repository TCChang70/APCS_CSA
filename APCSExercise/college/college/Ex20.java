package com;

import java.util.ArrayList;
import java.util.Scanner;
import java.text.DecimalFormat;

public class E20 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> evenNumbers = new ArrayList<>();
        int sum = 0;
        int count = 0;

        System.out.println("請輸入正整數（輸入 -1 結束）：");

        while (true) {
            int number = scanner.nextInt();

            if (number == -1) {
                break;
            }

            if (number > 0) {
                sum += number;
                count++;

                if (number % 2 == 0) {
                    evenNumbers.add(number);
                }
            } else {
                System.out.println("請輸入正整數，或輸入 -1 結束。");
            }
        }

        if (count == 0) {
            System.out.println("沒有輸入任何有效正整數。");
        } else {
            double average = (double) sum / count;
            DecimalFormat df = new DecimalFormat("0.00");

            System.out.print(sum + "," + df.format(average) + ",");

            // 輸出偶數列表
            for (int i = 0; i < evenNumbers.size(); i++) {
                System.out.print(evenNumbers.get(i));
                if (i < evenNumbers.size() - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println(); // 換行
        }
    }
}
