# Chapter 3 — Java Object-Oriented Approach

## 1z0-819 Exam Style Questions

---

### Question 1

Which statement about the Elephant program is correct?

```java
package stampede;

interface Long {
    Number length();
}

public class Elephant {
    public class Trunk implements Long {
        public Number length() { return 6; }          // k1
    }

    public class MyTrunk extends Trunk {
        public Integer length() { return 9; }         // k3
    }

    public static void charge() {
        System.out.print(new MyTrunk().length());
    }

    public static void main(String[] cute) {
        new Elephant().charge();                      // k4
    }
}
```

A. It compiles and prints 6.  
B. The code does not compile because of line k1.  
C. The code does not compile because of line k2.  
D. The code does not compile because of line k3.  
E. The code does not compile because of line k4.  
F. None of the above

<details>
<summary>Answer</summary>
**F. None of the above**

The code compiles and prints `9`. `Integer` is a covariant return type of `Number`. Calling a static method via instance reference is permitted.
</details>

---

### Question 2

What is the output of the following application?

```java
package sports;

abstract class Ball {
    protected final int size;
    public Ball(int size) {
        this.size = size;
    }
}

interface Equipment {}

public class SoccerBall extends Ball implements Equipment {
    public SoccerBall() {
        super(5);
    }
    public Ball get() { return this; }

    public static void main(String[] passes) {
        var equipment = (Equipment) (Ball) new SoccerBall().get();
        System.out.print(((SoccerBall) equipment).size);
    }
}
```

A. 5  
B. The code does not compile due to an invalid cast  
C. The code does not compile for a different reason  
D. The code compiles but throws a ClassCastException at runtime

<details>
<summary>Answer</summary>
**A. 5**

`get()` returns `this` (a `SoccerBall`). All casts succeed. `size` is `5`.
</details>

---

### Question 3

Given:

```java
public class GameObject {
    public Object[] move(int x, int y) {
        System.out.println("Move GameObject");
        return new Integer[]{x + 10, y + 10};
    }
}
```

and

```java
public class Avatar extends GameObject {
    public Object[] move(Number x, Number y) {
        System.out.println("Move Character");
        return super.move(x.intValue(), y.intValue());
    }

    public static void main(String... args) {
        var character = new Avatar();
        character.move(10.0, 10.0);
        character.move(10, 10);
    }
}
```

What is the result?

A) `Move Character` / `Move GameObject` / `Move GameObject`  
B) `Move GameObject` / `Move GameObject`  
C) `Move GameObject` / `Move Character` / `Move GameObject`  
D) `Move GameObject`

<details>
<summary>Answer</summary>
**A) `Move Character` / `Move GameObject` / `Move GameObject`**

`move(10.0, 10.0)` matches `move(Number, Number)` (overload) → prints "Move Character", then calls `super.move(...)` → prints "Move GameObject".  
`move(10, 10)` matches `move(int, int)` (inherited method, not overridden) → prints "Move GameObject".
</details>

---

### Question 4

Given:

```java
public class Menu {
    enum Machine {
        AUTO("Truck"), MEDICAL("Scanner");
        private String type;

        private Machine(String type) {
            this.type = type;
        }

        private void setType(String type) {
            this.type = type;              // line 1
        }

        private String getType() {
            return type;
        }
    }

    public static void main(String[] args) {
        Machine.AUTO.setType("Sedan");     // line 2
        for (Machine p : Machine.values()) {
            System.out.println(p + ": " + p.getType());  // line 3
        }
    }
}
```

What is the result?

A) The compilation fails due to an error on line 3.  
B) The compilation fails due to an error on line 2.  
C) `AUTO: Truck` / `MEDICAL: Scanner`  
D) An exception is thrown at runtime  
E) The compilation fails due to an error on line 1  
F) `AUTO: Sedan` / `MEDICAL: Scanner`

<details>
<summary>Answer</summary>
**F) `AUTO: Sedan` / `MEDICAL: Scanner`**

Enum fields can be modified if not declared `final`. `setType("Sedan")` changes `AUTO.type` from `"Truck"` to `"Sedan"`. `MEDICAL` remains `"Scanner"`.
</details>

---

### Question 5

Given:

```java
class Scope {
    static int myint = 666;
    public static void main(String[] args) {
        int myint = myint;
        System.out.println(myint);
    }
}
```

Which is true?

A) Code compiles but throws a runtime exception when run.  
B) It prints 666  
C) The code compiles and runs successfully but with a wrong answer.  
D) The code does not compile successfully

<details>
<summary>Answer</summary>
**D) The code does not compile successfully**

`int myint = myint;` — the RHS refers to the local variable (not yet initialized), not the static field. Compilation fails.
</details>

---

### Question 6

Given:

```java
// package test.t1;
public class A {
    public int x = 42;
    protected A() {}
}

// package test.t2;
import test.t1.*;
public class B extends A {
    int x = 17;
    public B() { super(); }
}

// package test;
import test.t1.*;
import test.t2.*;
public class Tester {
    public static void main(String[] args) {
        A obj = new B();
        System.out.println(obj.x);
    }
}
```

What is the result?

A) The compilation fails due to an error in line 4  
B) 17  
C) The compilation fails due to an error in line 2  
D) The compilation fails due to an error in line 3  
E) The compilation fails due to an error in line 1  
F) The compilation fails due to an error in line 5  
G) 42

<details>
<summary>Answer</summary>
**G) 42**

Fields are accessed based on reference type (`A`), not object type (`B`). `A.x = 42`.
</details>

---

### Question 7

Given:

```java
public class DNASynth {
    int aCount, tCount, cCount, gCount;

    DNASynth(int aCount, int tCount, int c, int g) {
        // line 1
    }

    int setCCount(int c) { return c; }
    void setGCount(int gCount) { this.gCount = gCount; }
}
```

Which two lines of code when inserted in line 1 correctly modify instance variables?

A) `tCount = tCount;`  
B) `cCount = setCCount(c);`  
C) `setCCount(c) = cCount;`  
D) `aCount = aCount;`  
E) `setGCount(g);`

<details>
<summary>Answer</summary>
**B, E**

B assigns the return value of `setCCount(c)` to `cCount`.  
E calls `setGCount(g)` which sets `this.gCount`.  
A and D assign the parameter to itself. C is invalid syntax.
</details>

---

### Question 8

Given:

```java
public class Price {
    private final double value;

    public Price(String value) {
        this(Double.parseDouble(value));
    }

    public Price(double value) {
        this.value = value;
    }

    public Price() {}

    public double getValue() { return value; }

    public static void main(String[] args) {
        Price p1 = new Price("1.99");
        Price p2 = new Price(2.99);
        Price p3 = new Price();
        System.out.println(p1.getValue() + "," + p2.getValue() + "," + p3.getValue());
    }
}
```

What is the result?

A) `1.99,2.99,0.0`  
B) `1.99,2.99`  
C) The compilation fails  
D) `1.99,2.99,0`

<details>
<summary>Answer</summary>
**C) The compilation fails**

The no-arg constructor `Price() {}` does not initialize the `final` field `value`. Every constructor must assign `final` instance fields.
</details>

---

### Question 9

Given:

```java
public interface Builder {
    public A build(String str);
}
```

and

```java
public class BuilderImpl implements Builder {
    @Override
    public B build(String str) {
        return new B(str);
    }
}
```

Assuming this code compiles correctly, which three statements are true?

A) A cannot be abstract.  
B) A is a subtype of B.  
C) B cannot be final.  
D) B is a subtype of A.  
E) B cannot be abstract.  
F) A cannot be final.

<details>
<summary>Answer</summary>
**D, E, F**

D) `B` must be a subtype of `A` (covariant return).  
E) `B` is instantiated (`new B(str)`), so it cannot be abstract.  
F) `A` cannot be `final` (or `B` could not extend it).
</details>

---

### Question 10

Given:

```java
public class Foo {
    public void foo(Collection arg) {
        System.out.println("Bonjour le monde");
    }
}

public class Bar extends Foo {
    public void foo(Collection arg) {
        System.out.println("Hello world");
    }
    public void foo(List arg) {
        System.out.println("Hola Mundo!");
    }
}
```

and:

```java
Foo f1 = new Foo();
Foo f2 = new Bar();
Bar b1 = new Bar();
List<String> li = new ArrayList<>();
```

Which three are correct?

A) `f2.foo(li)` prints `Bonjour le monde`  
B) `f1.foo(li)` prints `Hola Mundo!`  
C) `f2.foo(li)` prints `Hola Mundo!`  
D) `b1.foo(li)` prints `Hola Mundo!`  
E) `f2.foo(li)` prints `Hello world!`  
F) `b1.foo(li)` prints `Hello world!`  
G) `f1.foo(li)` prints `Bonjour le monde!`  
H) `f1.foo(li)` prints `Hello world!`  
I) `b1.foo(li)` prints `Bonjour le monde!`

<details>
<summary>Answer</summary>
**D, E, G**

`f1.foo(li)` → `Foo` ref, only `foo(Collection)` visible → "Bonjour le monde" (G).  
`f2.foo(li)` → `Foo` ref, only `foo(Collection)` visible, overridden → "Hello world" (E).  
`b1.foo(li)` → `Bar` ref, `foo(List)` is more specific → "Hola Mundo!" (D).
</details>

---

### Question 11

Given:

```java
class SomeClass {
    public void methodA() {
        System.out.println("SomeClass#methodA()");
    }
}

class AnotherClass extends SomeClass {
    public void methodA() {
        System.out.println("AnotherClass#methodA");
    }
}

public class Test {
    public static void main(String[] args) {
        AnotherClass ac = new AnotherClass();
        SomeClass sc = new AnotherClass();
        ac = sc;
        sc.methodA();
        ac.methodA();
    }
}
```

What is the result?

A) A ClassCastException is thrown at runtime.  
B) `SomeClass#methodA()` / `AnotherClass#methodA()`  
C) `AnotherClass#methodA()` / `AnotherClass#methodA()`  
D) The compilation fails  
E) `AnotherClass#methodA()` / `SomeClass#methodA()`  
F) `SomeClass#methodA()` / `SomeClass#methodA()`

<details>
<summary>Answer</summary>
**D) The compilation fails**

`ac = sc;` assigns a supertype reference (`SomeClass`) to a subtype variable (`AnotherClass`) without a cast — compilation error.
</details>

---

### Question 12

Given:

```java
interface AbilityA {
    default void action() {
        System.out.println("a action");
    }
}

interface AbilityB {
    void action();
}

public class Test implements AbilityA, AbilityB {  // line 1
    public void action() {
        System.out.println("ab action");
    }

    public static void main(String[] args) {
        AbilityB x = new Test();                   // line 2
        x.action();
    }
}
```

What is the result?

A) The compilation fails on line 1  
B) An exception is thrown at runtime  
C) The compilation fails on line 2  
D) `a action`  
E) `ab action`

<details>
<summary>Answer</summary>
**E) `ab action`**

`Test` provides an `action()` override, resolving the default/abstract conflict. Runtime dispatch calls `Test`'s method.
</details>

---

### Question 13

Given the enum declaration:

```java
enum Alphabet {
    A, B, C
    // line 3
}
```

Example: `System.out.println(Alphabet.getFirstLetter());`

What code should be written at line 3 to print `A`?

A) `static String getFirstLetter() { return A.toString(); }`  
B) `static String getFirstLetter() { return Alphabet.values().toString(); }`  
C) `String getFirstLetter() { return A.toString(); }`  
D) `final String getFirstLetter() { return A.toString(); }`

<details>
<summary>Answer</summary>
**A) `static String getFirstLetter() { return A.toString(); }`**

The method is called on the enum type, so it must be `static`.
</details>

---

### Question 14

Given:

```java
public interface ExampleInterface {}
```

Which two statements are valid to be written in this interface?

A) `public String method();`  
B) `public void methodF() { System.out.println("F"); }`  
C) `public int x;`  
D) `final void methodE()`  
E) `final void methodG() { System.out.println("G"); }`  
F) `private abstract void methodC();`  
G) `public abstract void methodB();`

<details>
<summary>Answer</summary>
**A, G**

A) Valid abstract method. G) Explicitly abstract method.  
B) needs `default` or `static` for body. C) fields must be initialized.  
D/E) `final` methods not allowed in interfaces.  
F) `private abstract` is contradictory.
</details>

---

### Question 15

Given:

```java
public class Person {
    private String name;
    private Person child;

    public Person(String name, Person child) {
        this(name);
        this.child = child;
    }
    public Person(String name) { this.name = name; }
    public String toString() { return name + " " + child; }
}

public class Tester {
    public static Person createPeople() {
        Person jane = new Person("Jane");
        Person john = new Person("John", jane);
        return jane;
    }

    public static Person createPerson(Person person) {
        person = new Person("Jack", person);
        return person;
    }

    public static void main(String[] args) {
        Person person = createPeople();
        // line 1
        person = createPerson(person);
        // line 2
        String name = person.toString();
        System.out.println(name);
    }
}
```

Which statement is true?

A) The memory allocated for John object can be reused in line 1.  
B) The memory allocated for Jack object can be reused in line 2.  
C) The memory allocated for Jane object can be reused in line 2.  
D) The memory allocated for Jane object can be reused in line 1.

<details>
<summary>Answer</summary>
**C) The memory allocated for Jane object can be reused in line 2.**

After `person = createPerson(person)`, `person` points to `Jack`. `Jane` is referenced only by `Jack.child`. If `Jack` becomes unreachable, `Jane` also becomes eligible. At line 2, after the reassignment, the `Jane` object is eligible for garbage collection.
</details>

---

### Question 16

Given:

```java
public interface A {
    public Iterable a();
}

public interface B extends A {
    public Collection a();
}

public interface C extends A {
    public Path a();
}

public interface D extends B, C {}
```

Why does D cause a compilation error?

A) D does not define any method.  
B) D inherits `a()` only from C.  
C) D inherits `a()` from B and C but the return types are incompatible.  
D) D extends more than one interface

<details>
<summary>Answer</summary>
**C) D inherits `a()` from B and C but the return types are incompatible.**

`Iterable`, `Collection`, and `Path` are not mutually assignable — `Collection` is a subtype of `Iterable`, but `Path` is not, creating an incompatible override conflict.
</details>

---

### Question 17

Given:

```java
public class Test {
    private final int x = 1;
    static final int y;
    public Test() {
        System.out.print(x);
        System.out.print(y);
    }
    public static void main(String args[]) {
        new Test();
    }
}
```

What is the result?

A) The compilation fails at line 13  
B) The compilation fails at line 9  
C) The compilation fails at line 16  
D) 1  
E) 10

<details>
<summary>Answer</summary>
**A) The compilation fails at line 13**

`static final int y;` is declared but never initialized. `static final` fields must be assigned exactly once, either inline or in a `static` initializer block. Accessing `y` at line 13 causes a compilation error.
</details>

---

### Question 18

Given:

```java
interface Pastry {
    void getIngredients();
}

abstract class Cookie implements Pastry {}

class ChocolateCookie implements Cookie {
    public void getIngredients() {}
}

class CoconutChocolateCookie extends ChocolateCookie {
    void getIngredients(int x) {}
}
```

Which is true?

A) The compilation fails due to an error in line 10.  
B) The compilation fails due to an error in line 9.  
C) The compilation fails due to an error in line 4.  
D) The compilation fails due to an error in line 6.  
E) The compilation succeeds  
F) The compilation fails due to an error in line 7.  
G) The compilation fails due to an error in line 2

<details>
<summary>Answer</summary>
**D) The compilation fails due to an error in line 6.**

`class ChocolateCookie implements Cookie` — `Cookie` is `abstract`, so `ChocolateCookie` cannot use `implements` with it. A class `implements` an interface, but `Cookie` is a class (abstract). It should use `extends Cookie` instead.
</details>
