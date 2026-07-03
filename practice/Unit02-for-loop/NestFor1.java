public class NestFor1 {
    public static void main(String[] args){
        int j=1;
        for(j=1; j<=9; j++){
           for(int i=1; i<=9; i++){
              System.out.print(j+"x"+i+" = "+(j*i)+" ");
           }
           System.out.println();
        }

    }
}
