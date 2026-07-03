# Chapter 8 — Concurrency

## 1z0-819 Exam Style Questions

---

### Question 1

What is the output of the following application?

```java
import java.util.*;

public class SearchList<T> {
    private List<T> data;
    private boolean foundMatch = false;

    public SearchList(List<T> list) {
        this.data = list;
    }

    public void exists(T v, int start, int end) {
        if (end - start == 0) {}
        else if (end - start == 1) {
            foundMatch = foundMatch || v.equals(data.get(start));
        } else {
            final int middle = start + (end - start) / 2;
            new Thread(() -> exists(v, start, middle)).run();
            new Thread(() -> exists(v, middle, end)).run();
        }
    }

    public static void main(String[] a) throws Exception {
        List<Integer> data = List.of(1, 2, 3, 4, 5, 6);
        SearchList<Integer> t = new SearchList<Integer>(data);
        t.exists(5, 0, data.size());
        System.out.print(t.foundMatch);
    }
}
```

A. `true`  
B. `false`  
C. The code does not compile  
D. The result is unknown until runtime  
E. An exception is thrown  
F. None of the above

<details>
<summary>Answer</summary>
**A. `true`**

`.run()` executes the task synchronously on the current thread (not a new thread). The recursive binary search finds `5` in the list and sets `foundMatch = true`.
</details>

---

### Question 2

Which of the following methods is **not** available on an `ExecutorService` instance? (Choose two.)

A. `execute(Callable)`  
B. `shutdownNow()`  
C. `submit(Runnable)`  
D. `exit()`  
E. `submit(Callable)`  
F. `execute(Runnable)`

<details>
<summary>Answer</summary>
**A, D**

`ExecutorService.execute()` only accepts `Runnable`, not `Callable`. `exit()` is not a method of `ExecutorService`.
</details>

---

### Question 3

Given:

```java
var c = new CopyOnWriteArrayList<>(List.of("1", "2", "3", "4"));
Runnable r = () -> {
    try {
        Thread.sleep(150);
    } catch (InterruptedException e) {
        System.out.println(e);
    }
    c.set(3, "four");
    System.out.print(c + " ");
};
Thread t = new Thread(r);
t.start();
for (var s : c) {
    System.out.print(s + " ");
    Thread.sleep(100);
}
```

What is the output?

A) `1 2 [1, 2, 3, four] 3 4`  
B) `1 2 [1, 2, 3, 4] 3 four`  
C) `1 2 [1, 2, 3, 4] 3 4`  
D) `1 2 [1, 2, 3, four] 3 four`

<details>
<summary>Answer</summary>
**A) `1 2 [1, 2, 3, four] 3 4`**

`CopyOnWriteArrayList` uses a snapshot iterator. The main thread iterates over the original snapshot: `"1"`, `"2"`, `"3"`, `"4"`. After 150ms, the other thread modifies index 3 to `"four"` and prints `[1, 2, 3, four]`. The main thread continues with its snapshot: `"3"`, `"4"`.
</details>

---

### Question 4

Given:

```java
public interface Worker {
    public void doProcess();
}

public class HardWorker implements Worker {
    public void doProcess() {
        System.out.println("doing things");
    }
}

public class Cheater implements Worker {
    public void doProcess() {}
}

public class Main<T extends Worker> extends Thread {
    private List<T> processes = new ArrayList<>();

    public void addProcess(HardWorker w) {     // line 3
        processes.add(w);
    }

    public void run() {
        processes.forEach((p) -> p.doProcess());
    }
}
```

What needs to change to make these classes compile and still handle all types of `Worker`?

A) Replace Line 1 with `public class Main<T extends HardWorker> extends Thread`  
B) Replace Line 3 with `public void addProcess(T w)`  
C) Replace Line 3 with `public void addProcess(Worker w)`  
D) Replace Line 2 with `private List<HardWorker> processes = new ArrayList<>()`

<details>
<summary>Answer</summary>
**B) Replace Line 3 with `public void addProcess(T w)`**

`processes` is `List<T>` but `addProcess` takes `HardWorker`. Since `T` could be any `Worker` subtype (e.g., `Cheater`), `HardWorker` is not assignable to `T`. The fix is to use `T w` as the parameter type.
</details>

---

### Question 5

```java
public class MyWork implements Runnable {
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

// and
Thread t = new Thread(new MyWork());
t.start();
```

What is the result?

A) `false`  
B) `true`  
C) A `NullPointerException` is thrown at runtime  
D) The code does not compile

<details>
<summary>Answer</summary>
**C) A `NullPointerException` is thrown at runtime**

`mydata` is never initialized (defaults to `null`). Calling `mydata.contains(data)` throws a `NullPointerException`.
</details>

---

### Question 6

Given:

```java
class Student implements java.io.Serializable {
    String id, name;

    public Student() {}

    public Student(String i, String n) {
        id = i;
        name = n;
    }

    public String toString() {
        return id + "," + name;
    }
}

// and
static void save() throws IOException {
    Student s1 = new Student("S001", "Mary");
    OutputStream out = new FileOutputStream("c:/temp/stu.bin");
    ObjectOutputStream sm = new ObjectOutputStream(out);
    sm.writeObject(s1);
    sm.close();
    System.out.println(sm);
}
```

What is the output?

A) `S001,Mary`  
B) The code does not compile  
C) An `IOException` or `NotSerializableException` is thrown  
D) The result is a serialized object and a reference to the `ObjectOutputStream` is printed

<details>
<summary>Answer</summary>
**D) The result is a serialized object and a reference to the `ObjectOutputStream` is printed**

`Student` implements `Serializable`, so serialization succeeds. `System.out.println(sm)` prints the `ObjectOutputStream` object reference (e.g., `java.io.ObjectOutputStream@...`).
</details>
