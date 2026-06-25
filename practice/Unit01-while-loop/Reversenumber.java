public class Reversenumber {
    public static void main(String[] args){
        int n=6789;
        int v1=n%10;
        int v2=n/10;
        System.out.print("v1="+v1);        
        //System.out.println("v2="+v2);
        System.out.print(v2%10);
        v2=v2/10;
        System.out.print(v2%10);
        v2=v2/10;
        System.out.print(v2%10);
    }
}
