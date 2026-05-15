package com;

import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入一個年份：");
        int year = scanner.nextInt();

        String[] zodiacs = {
            "鼠", "牛", "虎", "兔", "龍", "蛇", 
            "馬", "羊", "猴", "雞", "狗", "豬"
        };

        // 計算與1900年的差距，然後取餘數
        int index = (year - 1900) % 12;
        if (index < 0) {
            index += 12; // 處理負值年份
        }

        System.out.println(year + " 年的生肖是：" + zodiacs[index]);
    }
}

