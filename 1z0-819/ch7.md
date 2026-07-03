# Chapter 7 — Java Platform Module System

## 1z0-819 Exam Style Questions

---

### Question 1

What statements are true about `requires mandated java.base`? (Choose two)

A. This output is expected when running the `java --list-modules` command.  
B. This output is expected when running the `java --show-module-resolution` command.  
C. This output is expected when running the `jdeps` command.  
D. This output is expected when running the `jmod` command.  
E. All modules will include this in the output.  
F. Some modules will include this in the output.

<details>
<summary>Answer</summary>
**C, E**

`jdeps` shows module dependencies including the implicit `requires mandated java.base`. All modules depend on `java.base`, so all will include this line.
</details>

---

### Question 2

What is the name of a file that declares a module?

A. `mod.java`  
B. `mod-data.java`  
C. `mod-info.java`  
D. `module.java`  
E. `module-data.java`  
F. `module-info.java`

<details>
<summary>Answer</summary>
**F. `module-info.java`**

The module descriptor file must be named `module-info.java` and is placed in the root directory of the module.
</details>

---

### Question 3

Suppose you have a module that contains a class with a call to `exports(ChocolateLab.class)`. Which part of the module service contains this class?

A. Consumer  
B. Service locator  
C. Service provider  
D. Service provider interface  
E. None of the above

<details>
<summary>Answer</summary>
**E. None of the above**

`exports()` in `module-info.java` is used to export packages, not related to the service provider/consumer/service locator API.
</details>

---

### Question 4

How many of these keywords can be used in a `module-info.java` file: `close`, `export`, `import`, `require`, and `uses`?

A. None  
B. One  
C. Two  
D. Three  
E. Four  
F. Five

<details>
<summary>Answer</summary>
**B. One**

Valid `module-info.java` keywords are: `exports`, `requires`, `transitive`, `provides`, `opens`, `uses`. From the list, only `uses` is valid. `export` (not `exports`) and `require` (not `requires`) are not valid keywords.
</details>

---

### Question 5

Which module defaults the foundational APIs of the Java SE Platform?

A) `java.lang`  
B) `java.base`  
C) `java.object`  
D) `java.se`

<details>
<summary>Answer</summary>
**B) `java.base`**

`java.base` is the fundamental module containing core APIs like `java.lang`, `java.util`, `java.io`, etc. It is automatically required by all other modules.
</details>
