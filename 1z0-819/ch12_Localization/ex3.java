package ch12_Localization;




public class ex3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		

	}

}
/*
Given the code fragment:

Locale locale=Locale.US;
// Line 1
double currency=1_00.00;
System.out.println(formatter.format(currency));

You want to display the value of currency as $100.00.

Which code inserted on line 1 will accomplish this?

A) NumberFormat formatter=NumberFormat.getInstance(locale).getCurrency();
B) NumberFormat formatter=NumberFormat.getInstance(locale);
C) NumberFormat formatter=NumberFormat.getCurrency(locale);
D) NumberFormat formatter=NumberFormat.getCurrencyInstance(locale);



ans:D




*/