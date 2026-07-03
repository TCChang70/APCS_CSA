package ch10_Secure_Coding_in_java_se_Application;

public class ex2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
/*
How do you change the value of an instance variable in an immutable class?

A. Call the setter method
B. Remove the final modifier and set the instance variable directly
C. Create a new instance with an inner class
D. Use a method other than Option A,B, or C.
E. You can't



ans:E

定義immutable class的方法如下

不提供修改屬性內容的setter方法。
所有的屬性宣告為private final使其無法被修改。
類別宣告為final class使無法被繼承，方法無法被覆寫。或是把建構式設為private，並改以工廠方法提供物件的實例。
若屬性為mutable object應避免提供修改方法，讀取時提供複製物件而非原物件的參照。
*/