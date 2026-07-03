package ch8_Concurrency;
import java.util.*;
public class ex5 {
    public static void main(String[] args) {
        Thread t = new Thread(new MyWork());
        t.start();
    }
}

class MyWork implements Runnable {
    List<String> mydata;
    public boolean exists(String data) {
        return mydata.contains(data);
    }
    @Override
    public void run() {
        boolean b = exists("java");
        System.out.println(b);
    }
    
}