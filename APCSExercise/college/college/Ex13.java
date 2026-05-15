package com;

import java.util.Scanner;

public class Ex13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 輸入三個邊長
        System.out.print("請輸入第一個邊長：");
        int a = scanner.nextInt();

        System.out.print("請輸入第二個邊長：");
        int b = scanner.nextInt();

        System.out.print("請輸入第三個邊長：");
        int c = scanner.nextInt();

        // 檢查是否能構成三角形
        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            // 判斷是否為直角三角形
            int a2 = a * a;
            int b2 = b * b;
            int c2 = c * c;

            boolean isRightTriangle = (a2 + b2 == c2) || (a2 + c2 == b2) || (b2 + c2 == a2);

            if (isRightTriangle) {
                // 計算直角三角形面積：1/2 × 直角邊1 × 直角邊2
                double area = 0;
                if (a2 + b2 == c2) {
                    area = 0.5 * a * b;
                } else if (a2 + c2 == b2) {
                    area = 0.5 * a * c;
                } else if (b2 + c2 == a2) {
                    area = 0.5 * b * c;
                }

                System.out.printf("這是直角三角形，面積為：%.2f\n", area);
            } else {
                System.out.println("這是其他類型三角形。");
            }
        } else {
            System.out.println("資料錯誤：無法構成三角形。");
        }
    }
}
