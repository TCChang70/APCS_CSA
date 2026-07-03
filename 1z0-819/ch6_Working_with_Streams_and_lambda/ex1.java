package ch6_Working_with_Streams_and_lambda;

import java.util.*;

import java.util.stream.*;

class Thermometer {
	private String feelsLike;
	private double temp;

	@Override
	public String toString() {
		return feelsLike;
	}

	// Constructor/Getters/Setters Omitted
	public Thermometer() {
	}

	public Thermometer(String feelsLike, double temp) {
		this.feelsLike = feelsLike;
		this.temp = temp;
	}

	public double getTemp() {
		return temp;
	}

	public void setTemp(double temp) {
		this.temp = temp;
	}

	public static void main(String... season) {
		var readings = List.of(new Thermometer("HOT!", 72),
				new Thermometer("Too Cold", 0),
				new Thermometer("Just right!", 72));
		readings
				.parallelStream() // k1
				.collect(Collectors.groupingByConcurrent(
						Thermometer::getTemp)) // k2
				.forEach((temp, ther) -> System.out.printf("feellike:%s , temp:%.2f\n ",ther,temp)); // k3

	}

	public String getFeelsLike() {
		return feelsLike;
	}

	public void setFeelsLike(String feelsLike) {
		this.feelsLike = feelsLike;
	}
}

/*
 * What is a possible output of the following application?
 * import java.url.*;
 * import java.util.stream.*;
 * public class Thermometer {
 * private String feelsLike;
 * private double temp;
 * 
 * @Override public String toString(){ return feelsLike;}
 * // Constructor/Getters/Setters Omitted
 * 
 * 
 * public static void main(String... season) {
 * var readings=List.of(new Thermometer("HOT!",72),
 * new Thermometer("Too Cold",0),
 * new Thermometer("Just right!"72));
 * readings
 * .parallelStream() // k1
 * .collect(Collectors.groupingByConcurrent(
 * Thermometer::getTemp)) // k2
 * .forEach(System.out::println); // k3
 * 
 * }}
 * 
 * 
 * A) {0.0=[Cold!], 72.0=[Hot!, Just right!]}
 * B) {0.0=[Cold!], 72.0=[Just right!] , 72.0=[HOT!]}
 * C) The code does not compile because of line k1
 * D) The code does not compile because of line k2
 * E) The code does not compile because of line k3
 * F) None of the above
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * ans:E
 * 
 * 
 */