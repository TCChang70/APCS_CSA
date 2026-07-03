# Chapter 1 — Working with Java Data Types

## 1z0-819 Exam Style Questions

---

### Question 1

How many of these compile?

```java
Comparator<String> c1 = (j, k) -> 0;
Comparator<String> c2 = (String j, String k) -> 0;
Comparator<String> c3 = (var j, String k) -> 0;
Comparator<String> c4 = (var j, k) -> 0;
Comparator<String> c5 = (var j, var k) -> 0;
```

A. 0  
B. 1  
C. 2  
D. 3  
E. 4  
F. 5

<details>
<summary>Answer</summary>
**D. 3**

`c1`, `c2`, `c5` compile.  
`c3` fails — cannot mix `var` with explicit type in lambda parameters.  
`c4` fails — `var` must be used for all parameters or none.
</details>

---

### Question 2

What is the output of the following application?

```java
public class Airplane {
    static int start = 2;
    final int end;

    public Airplane(int x) {
        x = 4;
        end = x;
    }

    public void fly(int distance) {
        System.out.print(end - start + " ");
        System.out.print(distance);
    }

    public static void main(String... start) {
        new Airplane(10).fly(5);
    }
}
```

A. 2 5  
B. 8 5  
C. 6 5  
D. The code does not compile.  
E. None of the above

<details>
<summary>Answer</summary>
**A. 2 5**

`start = 2` (static). Constructor reassigns `x = 4`, so `end = 4`.  
`end - start = 4 - 2 = 2`. `distance = 5`.
</details>

---

### Question 3

Given the code fragment:

```java
var i = 10;
var j = 5;
i += (j * 5 + i) / j - 2;
System.out.println(i);
```

What is the result?

A) 5  
B) 11  
C) 21  
D) 23  
E) 15

<details>
<summary>Answer</summary>
**E) 15**

`i = 10 + (5*5 + 10)/5 - 2` → `10 + 35/5 - 2` → `10 + 7 - 2` → `15`
</details>

---

### Question 4

Given:

```java
public class Tester {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder(5);
        sb.append("HOWDY");
        sb.insert(0, ' ');
        sb.replace(3, 5, "LL");
        sb.insert(6, "COW");
        sb.delete(2, 7);
        System.out.println(sb.length());
    }
}
```

What is the result?

A) 5  
B) 3  
C) An exception is thrown at runtime.  
D) 4

<details>
<summary>Answer</summary>
**D) 4**

Tracing the StringBuilder operations:
1. `sb = ""` (capacity 5)
2. `append("HOWDY")` → `"HOWDY"`
3. `insert(0, ' ')` → `" HOWDY"`
4. `replace(3, 5, "LL")` → `" HOLLY"`
5. `insert(6, "COW")` → `" HOLLYCOW"`
6. `delete(2, 7)` → remaining length = 4
</details>

---

### Question 5

Given:

```java
public class StrBldr {
    static StringBuilder sb1 = new StringBuilder("yo ");
    StringBuilder sb2 = new StringBuilder("hi ");

    public static void main(String[] args) {
        sb1 = sb1.append(new StrBldr().foo(new StringBuilder("hey")));
        System.out.println(sb1);
    }

    StringBuilder foo(StringBuilder s) {
        System.out.print(s + " oh " + sb2);
        return new StringBuilder("ey");
    }
}
```

What is the result?

A) oh hi hey  
B) hey oh hi  
C) A compile time error occurs.  
D) hey oh hi yo ey  
E) yo ey  
F) hey oh hi ey

<details>
<summary>Answer</summary>
**D) hey oh hi yo ey**

1. `foo()` called first: prints `"hey oh hi "`
2. Returns `new StringBuilder("ey")`
3. `sb1.append("ey")` → `"yo "` becomes `"yo ey"`
4. Full output: `"hey oh hi yo ey"`
</details>

---

### Question 6

Given:

```java
public class Test {
    public void process(byte v) {
        System.out.println("Byte value " + v);
    }

    public void process(short v) {
        System.out.println("Short value " + v);
    }

    public void process(Object v) {
        System.out.println("Object value " + v);
    }

    public static void main(String[] args) {
        byte x = 12;
        short y = 13;
        new Test().process(x + y);  // line 1
    }
}
```

What is the output?

A) Object value 25  
B) Byte value 25  
C) Short value 25  
D) The compilation fails due to an error in line 1

<details>
<summary>Answer</summary>
**A) Object value 25**

`byte` + `short` undergoes binary numeric promotion to `int`.  
Result is `int` 25, autoboxed to `Integer`, which matches `process(Object v)`.
</details>
