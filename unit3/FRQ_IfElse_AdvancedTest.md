# Free Response Questions

## **Question 1 (Programming Problem)**
Write a complete Java program that does the following:

1. Prompts the user to enter three integer values
2. Reads the three integers using Scanner
3. Determines and prints which value is the largest and which is the smallest
4. If all three values are equal, print "All values are equal"
5. Calculate and print the average of the three numbers as a double value

**Example Output 1:**
```
Enter three integers: 45 23 67
Largest: 67
Smallest: 23
Average: 45.0
```

**Example Output 2:**
```
Enter three integers: 10 10 10
All values are equal
Average: 10.0
```

---

## **Question 2 (Code Analysis)**
Consider the following code segment:

```java
Scanner input = new Scanner(System.in);
System.out.print("Enter a number: ");
int num = input.nextInt();

int result = 0;
if (num > 0) {
    result = num % 10;
} else if (num < 0) {
    result = -(num % 10);
} else {
    result = 0;
}
System.out.println("Result: " + result);
```

**Part A:** What does this code segment do? Explain in 1-2 sentences.

**Part B:** What will be printed if the user enters `-37`?

**Part C:** Identify and explain one potential issue with this code if the user enters non-integer input.
