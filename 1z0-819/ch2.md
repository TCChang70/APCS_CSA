# Chapter 2 — Controlling Program Flow

## 1z0-819 Exam Style Questions

---

### Question 1

Variables declared as which of the following are never permitted in a `switch` statement? (Choose two)

A. `var`  
B. `double`  
C. `int`  
D. `String`  
E. `char`  
F. `Object`

<details>
<summary>Answer</summary>
**B, F**

`switch` supports `int`, `char`, `byte`, `short`, `String`, `enum`, and `var` (if inferred to an allowed type).  
`double` and `Object` are never permitted.
</details>

---

### Question 2

What is the output of the following application?

```java
package planning;

public class ThePlan {
    var plan = 1;
    plan = plan++ + --plan;
    if (plan == 1) {
        System.out.print("Plan A");
    } else {
        if (plan == 2)
            System.out.print("Plan B");
    } else
        System.out.print("Plan C");
    }
}
```

A. Plan A  
B. Plan B  
C. Plan C  
D. The class does not compile  
E. None of the above

<details>
<summary>Answer</summary>
**D. The class does not compile**

Multiple compilation errors:
1. `var` cannot be used for a class field — only for local variables.
2. Two `else` clauses are attached to the same `if` statement.
3. Brace mismatch / invalid syntax.
</details>

---

### Question 3

Given:

```java
int i = 10;
do {
    for (int j = i / 2; j > 0; j--) {
        System.out.print(j + " ");
    }
    i -= 2;
} while (i > 0);
```

What is the result?

A) `5 4 3 2 1`  
B) nothing  
C) `5`  
D) `5 4 3 2 1 4 3 2 1 3 2 1 2 1 1`

<details>
<summary>Answer</summary>
**D) `5 4 3 2 1 4 3 2 1 3 2 1 2 1 1`**

Tracing:
- i=10 → j: 5 4 3 2 1, then i=8
- i=8  → j: 4 3 2 1, then i=6
- i=6  → j: 3 2 1, then i=4
- i=4  → j: 2 1, then i=2
- i=2  → j: 1, then i=0 → exits
</details>
