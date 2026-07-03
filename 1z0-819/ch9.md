# Chapter 9 — Java I/O API

## 1z0-819 Exam Style Questions

---

### Question 1

Why does `Console.readPassword()` return a `char[]` rather than a `String`?

A. It improves performance  
B. It improves security  
C. Passwords must be stored as a `char` array  
D. `String` cannot hold the individual password characters  
E. It adds encryption  
F. None of the above

<details>
<summary>Answer</summary>
**B. It improves security**

A `char[]` can be overwritten/zeroed out immediately after use. A `String` is immutable and remains in memory until garbage collected, posing a security risk.
</details>

---

### Question 2

Fill in the blanks: `Writer` is a(n) __________ that related stream classes __________.

A. concrete class, extend  
B. abstract class, extend  
C. abstract class, implement  
D. interface, extend  
E. interface, implement  
F. None of the above

<details>
<summary>Answer</summary>
**B. abstract class, extend**

`java.io.Writer` is an abstract class. Concrete stream classes like `FileWriter`, `OutputStreamWriter`, and `BufferedWriter` extend it.
</details>

---

### Question 3

Given:

```java
class MyPersistenceData {
    String str;

    private void methodA() {
        System.out.println("methodA");
    }
}
```

You want to implement the `java.io.Serializable` interface in the `MyPersistenceData` class.

Which method should be overridden?

A) the `readExternal` method  
B) the `readExternal` and `writeExternal` methods  
C) the `writeExternal` method  
D) nothing

<details>
<summary>Answer</summary>
**D) nothing**

`Serializable` is a marker interface — it has no methods to override. The JVM handles serialization automatically.
</details>
