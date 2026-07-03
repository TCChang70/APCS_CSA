# Chapter 4 — Exception Handling

## 1z0-819 Exam Style Questions

---

### Question 1

Which specific type of exception will be printed in the stack trace at runtime?

```java
package carnival;

public class WhackAnException {
    public static void main(String... hammer) {
        try {
            throw new ClassCastException();
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException();
        } catch (RuntimeException e) {
            throw new NullPointerException();
        } finally {
            throw new RuntimeException();
        }
    }
}
```

A. ClassCastException  
B. IllegalArgumentException  
C. NullPointerException  
D. RuntimeException  
E. The code does not compile.  
F. None of the above

<details>
<summary>Answer</summary>
**D. RuntimeException**

The `finally` block always runs. If it throws an exception, that exception replaces any exception thrown in the `try` or `catch` blocks.
</details>

---

### Question 2

What is the name of the class printed at line e1?

```java
package canyon;

final class FallenException extends Exception {}
final class HikingGear implements AutoCloseable {
    @Override public void close() throws Exception {
        throw new FallenException();
    }
}

public class Cliff {
    public final void climb() throws Exception {
        try (HikingGear gear = new HikingGear()) {
            throw new RuntimeException();
        }
    }

    public static void main(String... rocks) {
        try {
            new Cliff().climb();
        } catch (Throwable t) {
            System.out.println(t);  // e1
        }
    }
}
```

A. `canyon.FallenException`  
B. `java.lang.RuntimeException`  
C. The code does not compile.  
D. The code compiles, but the answer cannot be determined until runtime.  
E. None of the above

<details>
<summary>Answer</summary>
**B. `java.lang.RuntimeException`**

In try-with-resources, if both the try block and `close()` throw exceptions, the try block exception is the primary exception. The `close()` exception is added as a suppressed exception.
</details>

---

### Question 3

Given:

```java
import java.io.FileNotFoundException;
import java.io.IOException;

public class Tester {
    public static void main(String[] args) {
        try {
            doA();
        }  // line 1
    }

    private static void doA() throws Exception, IndexOutOfBoundsException {
        if (false) {
            throw new FileNotFoundException();
        } else {
            throw new IndexOutOfBoundsException();
        }
    }
}
```

What must be added in line 1 to compile this class?

A) `catch(FileNotFoundException | Exception e){}`  
B) `catch(FileNotFoundException e){}` / `catch(IndexOutOfBoundsException e){}`  
C) `catch(Exception e){}`  
D) `catch(IndexOutOfBoundsException e){}` / `catch(FileNotFoundException e){}`  
E) `catch(FileNotFoundException | IndexOutOfBoundsException e){}`

<details>
<summary>Answer</summary>
**C) `catch(Exception e){}`**

`FileNotFoundException` is a checked exception. A single `catch(Exception e)` covers both checked and unchecked exceptions. Options A and E have redundancy (multi-catch cannot have subtypes of the same exception). Options B and D won't compile because `FileNotFoundException` must be caught (checked).
</details>

---

### Question 4

Given:

```java
char[] characters = new char[100];
try (FileReader reader = new FileReader("file_to_path")) {
    // line 1
    System.out.println(String.valueOf(characters));
} catch (IOException e) {
    e.printStackTrace();
}
```

You want to read data through the reader object.

Which statement inserted on line 1 will accomplish this?

A) `reader.readLine();`  
B) `characters = reader.read();`  
C) `reader.read(characters);`  
D) `characters.read();`

<details>
<summary>Answer</summary>
**C) `reader.read(characters);`**

`FileReader.read(char[])` reads characters into the specified array and returns the number of characters read. `readLine()` is a `BufferedReader` method, not available on `FileReader`.
</details>

---

### Question 5

Given:

```java
public class ExSuper extends Exception {
    private final int eCode;
    public ExSuper(int eCode, Throwable cause) {
        super(cause);
        this.eCode = eCode;
    }
    public ExSuper(int eCode, String msg, Throwable cause) {
        super(msg, cause);
        this.eCode = eCode;
    }
    public String getMessage() {
        return this.eCode + ": " + super.getMessage() + "_" + this.getCause().getMessage();
    }
}

public class ExSub extends ExSuper {
    public ExSub(int eCode, String msg, Throwable cause) {
        super(eCode, msg, cause);
    }
}
```

and the code fragment:

```java
try {
    String param1 = "oracle";
    if (param1.equalsIgnoreCase("oracle")) {
        throw new ExSub(9001, "APPLICATION ERROR-9001", new FileNotFoundException("MyFile.txt"));
    }
    throw new ExSuper(9001, new FileNotFoundException("MyFile.txt"));  // Line 1
} catch (ExSuper ex) {
    System.out.println(ex.getMessage());
}
```

What is the result?

A) Compilation fails at Line 1;  
B) `9001: java.io.FileNotFoundException:MyFile.txt-MyFile.txt`  
C) `9001: APPLICATION ERROR-9001-MyFile.txt`  
D) `9001: APPLICATION ERROR-9001-MyFile.txt` / `9001: java.io.FileNotFoundException: MyFile.txt-MyFile.txt`

<details>
<summary>Answer</summary>
**C) `9001: APPLICATION ERROR-9001-MyFile.txt`**

`param1.equalsIgnoreCase("oracle")` is `true`, so `ExSub` is thrown. `ExSub.getMessage()` calls `super.getMessage()` → `ExSuper.getMessage()`. `super.getMessage()` returns the message string `"APPLICATION ERROR-9001"`, and `getCause().getMessage()` returns `"MyFile.txt"`. Result: `"9001: APPLICATION ERROR-9001_MyFile.txt"`.
</details>

---

### Question 6

Given:

```java
public class Option {
    public static void main(String[] args) {
        System.out.println("Ans: " + convert("a").get());
    }

    private static Optional<Integer> convert(String s) {
        try {
            return Optional.of(Integer.parseInt(s));
        } catch (Exception e) {
            return Optional.empty();
        }
    }
}
```

What is the result?

A) `Ans:`  
B) `Ans: a`  
C) A `java.util.NoSuchElementException` is thrown at runtime  
D) The compilation fails

<details>
<summary>Answer</summary>
**C) A `java.util.NoSuchElementException` is thrown at runtime**

`Integer.parseInt("a")` throws `NumberFormatException`. `Optional.empty()` is returned. Calling `.get()` on an empty `Optional` throws `NoSuchElementException`.
</details>

---

### Question 7

Given:

```java
import java.io.*;

public class Tester {
    public static void main(String args[]) {
        try {
            doA();
            doB();
        } catch (IOException e) {
            System.out.print("c");
            return;
        } finally {
            System.out.print("d");
        }
        System.out.print("f");
    }

    private static void doA() {
        System.out.print("a");
        if (false) {
            throw new IndexOutOfBoundsException();
        }
    }

    private static void doB() throws FileNotFoundException {
        System.out.print("b");
        if (true) {
            throw new FileNotFoundException();
        }
    }
}
```

What is the result?

A) The compilation fails.  
B) `adf`  
C) `abd`  
D) `abcd`  
E) `abdf`

<details>
<summary>Answer</summary>
**D) `abcd`**

`doA()` prints `"a"`. `doB()` prints `"b"` then throws `FileNotFoundException`. The `catch` prints `"c"` and executes `return`, but `finally` still runs and prints `"d"`. The `return` in `catch` prevents `"f"` from being printed.
</details>

---

### Question 8

Given:

```java
public class Test {
    private int num = 1;
    private int div = 0;

    public void divide() {
        try {
            num = num / div;
            System.out.print("Exception");
        } catch (ArithmeticException ae) {
            num = 100;
        } catch (Exception e) {
            num = 200;
        } finally {
            num = 300;
        }
        System.out.print(num);
    }

    public static void main(String args[]) {
        Test test = new Test();
        test.divide();
    }
}
```

What is the output?

A) 200  
B) 100  
C) 300  
D) Exception

<details>
<summary>Answer</summary>
**C) 300**

Division by zero throws `ArithmeticException`. The `catch` block sets `num = 100`. The `finally` block always executes, setting `num = 300`. After `finally`, `num` is printed as `300`.
</details>

---

### Question 9

Given:

```java
public class Test {
    private int sum;

    public int compute() {
        int x = 0;
        while (x < 3) {
            sum += ++x;
        }
        return sum / 4;
    }

    public static void main(String[] args) {
        Test t = new Test();
        int sum = t.compute();
        sum = t.compute();
        System.out.print(sum);
    }
}
```

What is the output?

A) 6  
B) 3  
C) An exception is thrown at runtime  
D) 9

<details>
<summary>Answer</summary>
**B) 3**

First `compute()`: `sum` starts at 0. Loop: x=1, sum=1; x=2, sum=3; x=3, sum=6. Returns `6/4 = 1` (integer division).  
Second `compute()`: `sum` (instance field) is still 6. Loop: x=1, sum=7; x=2, sum=9; x=3, sum=12. Returns `12/4 = 3`.  
Local variable `sum` (in `main`) = `3`.
</details>
