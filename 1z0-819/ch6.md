# Chapter 6 — Working with Streams and Lambda

## 1z0-819 Exam Style Questions

---

### Question 1

What is a possible output of the following application?

```java
var readings = List.of(
    new Thermometer("HOT!", 72),
    new Thermometer("Too Cold", 0),
    new Thermometer("Just right!", 72));
readings
    .parallelStream()                      // k1
    .collect(Collectors.groupingByConcurrent(
        Thermometer::getTemp))             // k2
    .forEach(System.out::println);         // k3
```

A) `{0.0=[Cold!], 72.0=[Hot!, Just right!]}`  
B) `{0.0=[Cold!], 72.0=[Just right!], 72.0=[HOT!]}`  
C) The code does not compile because of line k1  
D) The code does not compile because of line k2  
E) The code does not compile because of line k3  
F) None of the above

<details>
<summary>Answer</summary>
**E. The code does not compile because of line k3**

`Map.forEach()` expects a `BiConsumer<? super K, ? super V>`. `System.out::println` is a `Consumer` (single argument), not a `BiConsumer`.
</details>

---

### Question 2

What is the output of the following application?

```java
package lot;

import java.util.function.*;

public class Warehouse {
    private int quantity = 40;
    private final BooleanSupplier stock;

    {
        stock = () -> quantity > 0;
    }

    public void checkInventory() {
        if (stock.get())
            System.out.print("Plenty!");
        else {
            System.out.print("On Backorder!");
        }
    }

    public static void main(String... widget) {
        final Warehouse w13 = new Warehouse();
        w13.checkInventory();
    }
}
```

A. Plenty  
B. On Backorder!  
C. The code does not compile because of the `checkInventory()` method.  
D. The code does not compile for a different reason

<details>
<summary>Answer</summary>
**C. The code does not compile because of the `checkInventory()` method.**

`BooleanSupplier.get()` returns a `boolean`. If the condition inside `checkInventory()` or the lambda causes a compilation issue, it fails. In this case, the code does not compile due to the `checkInventory()` method — `stock.get()` cannot be resolved in this context.
</details>

---

### Question 3

Which code fragment represents a valid `Comparator` implementation?

A)
```java
new Comparator<String>() {
    public int compareTo(String str1, String str2) {
        return str1.compareTo(str2);
    }
};
```

B)
```java
public class Comps implements Comparator {
    public boolean compare(Object obj1, Object obj2) {
        return obj1.equals(obj2);
    }
}
```

C)
```java
public class Comps implements Comparator {
    public int compare(String str1, String str2) {
        return str1.length() - str2.length();
    }
}
```

D)
```java
new Comparator<String>() {
    public int compare(String str1, String str2) {
        return str1.compareTo(str2);
    }
};
```

<details>
<summary>Answer</summary>
**D**

A uses `compareTo` instead of `compare`. B returns `boolean` instead of `int`. C uses raw `Comparator` but `compare(String, String)` does not override `compare(Object, Object)`.
</details>

---

### Question 4

Given:

```java
var fruits = List.of("apple", "orange", "banana", "lemon");
Optional<String> result = fruits.stream()
    .filter(f -> f.contains("n"))
    .findAny();    // line 1

System.out.println(result.get());
```

You replace the code on line 1 to use `parallelStream`.

Which one is correct?

A) The compilation fails.  
B) The code will produce the same result  
C) A `NoSuchElementException` is thrown at runtime  
D) The code may produce a different result

<details>
<summary>Answer</summary>
**D) The code may produce a different result**

With a serial stream, `findAny()` often returns the first match. With a parallel stream, `findAny()` may return a different element for better performance.
</details>

---

### Question 5

Given the code fragment:

```java
var list = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
UnaryOperator<Integer> u = i -> i * 2;   // line 2
list.replaceAll(u);
```

Which can replace line 2?

A) `UnaryOperator<Integer> u = var i -> { return i * 2; }`  
B) `UnaryOperator<Integer> u = i -> { return i * 2; }`  
C) `UnaryOperator<Integer> u = (var i) -> (i * 2);`  
D) `UnaryOperator<Integer> u = (int i) -> i * 2;`

<details>
<summary>Answer</summary>
**C) `UnaryOperator<Integer> u = (var i) -> (i * 2);`**

A: `var` without parentheses is invalid. B: missing semicolons inside block. D: explicit primitive type is not allowed in lambda parameters for a generic functional interface.
</details>

---

### Question 6

Which two are valid statements?

A) `BiPredicate<Integer,Integer> test = (final var x, y) -> (x.equals(y));`  
B) `BiPredicate<Integer,Integer> test = (Integer x, final Integer y) -> (x.equals(y));`  
C) `BiPredicate<Integer,Integer> test = (final Integer var x, var y) -> (x.equals(y));`  
D) `BiPredicate<Integer,Integer> test = (var x, final var y) -> (x.equals(y));`  
E) `BiPredicate<Integer,Integer> test = (Integer var x, final var y) -> (x.equals(y));`

<details>
<summary>Answer</summary>
**B, D**

B uses explicit types with `final` — valid. D uses `var` consistently with `final` — valid.  
A mixes `var` with omitted type. C and E use `var` as an identifier, not a type.
</details>

---

### Question 7

Why would you choose to use a `peek` operation instead of a `forEach` operation on a `Stream`?

A) to process the current item and return a stream  
B) to process the current item and return void  
C) to remove an item from the beginning of the stream  
D) to remove an item from the end of the stream

<details>
<summary>Answer</summary>
**A) to process the current item and return a stream**

`peek()` is an intermediate operation that returns the modified stream for further processing. `forEach()` is a terminal operation that returns `void`.
</details>

---

### Question 8

Given the contents of `lines.txt`:

```
C
C++
Java
Go
Kotlin
```

and

```java
String fileName = "lines.txt";
List<String> list = new ArrayList<>();
try (Stream<String> stream = Files.lines(Paths.get(fileName))) {
    list = stream
        .filter(line -> !line.equalsIgnoreCase("JAVA"))
        .map(String::toUpperCase)
        .collect(Collectors.toList());
} catch (IOException e) {
}
list.forEach(System.out::println);
```

What is the result?

A) `C` / `C++` / `Go` / `Kotlin`  
B) `JAVA`  
C) `C` / `C++` / `GO` / `KOTLIN`  
D) `C` / `C++` / `JAVA` / `GO` / `KOTLIN`

<details>
<summary>Answer</summary>
**C) `C` / `C++` / `GO` / `KOTLIN`**

`"Java"` is filtered out by the case-insensitive filter. The remaining lines are converted to uppercase.
</details>

---

### Question 9

Given:

```java
public class Employee {
    private String name;
    private String neighborhood;
    private int salary;
    // Constructors and setter and getter methods go here
}
```

and:

```java
List<Employee> roster = new ArrayList<>();
Predicate<Employee> p = e -> e.getSalary() > 30;
Function<Employee, Optional<String>> f =
    e -> Optional.ofNullable(e.getNeighborhood());
```

Which two objects group all employees with a salary greater than 30 by neighborhood?

A) `Map<Optional<String>, List<Employee>> r4 = roster.stream() .collect(Collectors.groupingBy(f, Collectors.filtering(p, Collectors.toList())));`  
B) `Map<Optional<String>, List<Employee>> r2 = roster.stream().filter(p) .collect(Collectors.groupingBy(f, Employee::getNeighborhood));`  
C) `Map<Optional<String>, List<Employee>> r5 = roster.stream() .collect(Collectors.groupingBy(Employee::getNeighborhood, Collectors.filtering(p, Collectors.toList())));`  
D) `Map<Optional<String>, List<Employee>> r3 = roster.stream().filter(p) .collect(Collectors.groupingBy(p));`  
E) `Map<String, List<Employee>> r1 = roster.stream() .collect(Collectors.groupingBy(Employee::getNeighborhood, Collectors.filtering(p, Collectors.toList())));`

<details>
<summary>Answer</summary>
**A, E**

A groups by the `Function<Employee, Optional<String>> f` (by neighborhood wrapped in Optional), then filters with `p`.  
E groups by `Employee::getNeighborhood` (String key), then filters with `p`. Both correctly group employees with salary > 30 by neighborhood.
</details>

---

### Question 10

Given the code fragment:

```java
List<String> fruits = List.of("banana", "orange", "apple", "lemon");
Stream<String> s1 = fruits.stream();
Stream<String> s2 = s1.peek(i -> System.out.print(i + " "));
System.out.println("--------");

Stream<String> s3 = s2.sorted();
Stream<String> s4 = s3.peek(i -> System.out.print(i + " "));
System.out.println("--------");

String strFruits = s4.collect(Collectors.joining(","));
```

What is the output?

A)
```
--------
--------
banana orange apple lemon apple banana lemon orange
```

B)
```
banana orange apple lemon
------
apple banana lemon orange
------
```

C)
```
-----
banana orange apple lemon
-----
apple banana lemon orange
```

D)
```
-----
-----
```

E)
```
banana orange apple lemon apple banana lemon orange
------
------
```

<details>
<summary>Answer</summary>
**A**

Intermediary operations like `peek()` are lazy. They execute only when the terminal operation (`collect()`) is called. Both `println("--------")` execute first, then during `collect()`: `peek1` prints the original order, then `sorted()` reorders, then `peek2` prints the sorted order.
</details>
