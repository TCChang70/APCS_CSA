public class Number {
    public static void main(String[] args){
        int number=50;
        while(number%7!= 0){
            number++;
        }
        System.out.println("The 1st number >= 50 that is divisible by 7 is: " + number);
    }
}
