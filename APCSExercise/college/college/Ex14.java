package com;

import java.util.Scanner;
import java.util.Arrays;

public class Ex14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 讀入三個邊長
        System.out.print("請輸入三個正整數（用空格分開）：");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        // 放入陣列並排序，確保 c 是最長邊
        int[] sides = {a, b, c};
        Arrays.sort(sides); // sides[2] 是最大值

        int x = sides[0]; // 較短邊
        int y = sides[1]; // 較短邊
        int z = sides[2]; // 最長邊（視為斜邊）

        // 三角形不等式檢查
        if (x + y <= z) {
            System.out.println("無法構成三角形");
        } else {
            // 判斷是否為直角三角形（x^2 + y^2 == z^2）
            if (x * x + y * y == z * z) {
                double area = 0.5 * x * y;
                System.out.printf("%.0f\n", area); // 輸出整數形式面積
            } else {
                System.out.println("其他類型三角形");
            }
        }
    }
}
