package com;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Ex19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sum = 0;
        int count = 0;

        System.out.println("請持續輸入正整數（輸入 -1 結束）：");

        while (true) {
            int num = scanner.nextInt();

            if (num == -1) {
                break;
            }

            if (num > 0) {
                sum += num;
                count++;
            } else {
                System.out.println("請輸入正整數，或輸入 -1 結束。");
            }
        }

        if (count > 0) {
            double average = (double) sum / count;
            DecimalFormat df = new DecimalFormat("0.00");
            System.out.println("總和為：" + sum);
            System.out.println("平均為：" + df.format(average));
        } else {
            System.out.println("沒有輸入任何正整數。");
        }
    }
}
