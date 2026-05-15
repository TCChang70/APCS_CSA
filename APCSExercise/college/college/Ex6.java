package com;

import java.util.Scanner;
import java.util.Random;

public class Ex6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int answer = random.nextInt(21); // 產生 0~20 的隨機整數
        System.out.print("請猜一個 0~20 的整數：");
        int guess = scanner.nextInt();

        if (guess < 0 || guess > 20) {
            System.out.println("超出範圍");
        } else if (guess == answer) {
            System.out.println("恭喜答對！");
        } else {
            System.out.println("請再接再厲。");
            System.out.println("正確答案是：" + answer); // 可加可不加，看是否想提示答案
        }
    }
}

