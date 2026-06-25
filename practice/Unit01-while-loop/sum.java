public class sum {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;
        while (i <= 10) {
           if(i%3==0){
                sum += i;   // sum=sum+i
           }            
           i+=1;
        }
        System.out.println("The sum of numbers divisible by 3 from 1 to 10 is: " + sum);
    }
}
