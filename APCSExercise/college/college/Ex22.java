package com;

public class Ex22 {
    public static void main(String[] args) {
        // 外層控制列數（從 5 到 1）
        for (int i = 5; i >= 1; i--) {
            // 每列印出 i 個星星
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            // 換行
            System.out.println();
        }
    }
}
