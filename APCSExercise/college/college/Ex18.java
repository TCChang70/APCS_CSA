package com;

public class Ex18 {
    public static void main(String[] args) {
        // 外層迴圈控制列（1 到 9）
        for (int i = 1; i <= 9; i++) {
            // 內層迴圈控制行（1 到 9）
            for (int j = 1; j <= 9; j++) {
                System.out.printf("%d×%d=%-2d  ", i, j, i * j);
            }
            // 換行
            System.out.println();
        }
    }
}

