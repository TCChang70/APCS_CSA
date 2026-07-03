# Chapter 5 — Working with Arrays and Collections

## 1z0-819 Exam Style Questions

---

### Question 1

Which of the following fills in the blank so this code compiles?

```java
public static void getExceptions(Collection<______> coll) {
    coll.add(new RuntimeException());
    coll.add(new Exception());
}
```

A. `?`  
B. `? extends Exception`  
C. `? super Exception`  
D. None of the above

<details>
<summary>Answer</summary>
**C. `? super Exception`**

`? super Exception` allows adding `Exception` or any subclass. `?` only allows `null`. `? extends Exception` does not allow adding (producer-extends, consumer-super).
</details>

---

### Question 2

What does the following output?

```java
List<String> list = List.of("Mary", "had", "a", "little", "lamb");
Set<String> set = new HashSet<>(list);
set.addAll(list);
for (String sheep : set)
    if (sheep.length() > 1)
        set.remove(sheep);
System.out.println(set);
```

A. `[a, lamb, had, Mary, little]`  
B. `[a]`  
C. `[a, a]`  
D. The code does not compile.  
E. The code throws an exception at runtime

<details>
<summary>Answer</summary>
**E. The code throws an exception at runtime**

Modifying a `Set` directly while iterating over it with an enhanced for-each loop throws `ConcurrentModificationException`.
</details>

---

### Question 3

Given:

```java
ArrayList<Integer> a1 = new ArrayList<>();
a1.add(1);
a1.add(2);
a1.add(3);
Iterator<Integer> itr = a1.iterator();
while (itr.hasNext()) {
    if (itr.next() == 2) {
        a1.remove(2);
        System.out.print(itr.next());
    }
}
```

What is the result?

A) `1 2` followed by an exception  
B) `1 2 3` followed by an exception  
C) A `ConcurrentModificationException` is thrown at runtime  
D) `1 2 4 5`

<details>
<summary>Answer</summary>
**C) A `ConcurrentModificationException` is thrown at runtime**

Modifying the `ArrayList` (`a1.remove(2)`) while iterating with an `Iterator` (without using the iterator's own `remove()` method) throws `ConcurrentModificationException`.
</details>

---

### Question 4

Given:

```java
String[] catNames = {"abyssinian", "oxicat", "korat", "laperm", "bengal", "sphynx"};
var cats = new ArrayList<>(Arrays.asList(catNames));
cats.sort((var a, var b) -> -a.compareTo(b));
cats.forEach(System.out::println);
```

What is the result?

A) nothing  
B) `sphynx` / `oxicat` / `laperm` / `korat` / `bengal` / `abyssinian`  
C) `abyssinian` / `oxicat` / `korat` / `laperm` / `bengal` / `sphynx`  
D) `abyssinian` / `bengal` / `korat` / `laperm` / `oxicat` / `sphynx`

<details>
<summary>Answer</summary>
**B) `sphynx` / `oxicat` / `laperm` / `korat` / `bengal` / `abyssinian`**

`-a.compareTo(b)` reverses the natural (ascending) order, producing descending alphabetical order.
</details>
