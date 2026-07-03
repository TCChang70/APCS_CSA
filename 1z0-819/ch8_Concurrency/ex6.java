package ch8_Concurrency;

import java.io.*;

public class ex6 {
    static void save() throws IOException {
        Student s1 = new Student("S001", "Mary");
        OutputStream out = new FileOutputStream("c:/temp/stu.bin");
        ObjectOutputStream sm = new ObjectOutputStream(out);
        sm.writeObject(s1);
        sm.close();
        System.out.println(sm);
    }

    public static void main(String[] args) throws IOException {
        save();
    }
}

class Student implements java.io.Serializable {
    String id, name;

    public Student() {
    }

    public Student(String i, String n) {
        id = i;
        name = n;
    }

    public String toString() {
        return id + "," + name;
    }
}