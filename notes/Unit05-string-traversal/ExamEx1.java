public class ExamEx1 {
    public static void main(String[] args){
        String str="Zbc";
        String str2="";
        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            ch++;
            if(ch>'z'){
                ch='a';
            }
            if(ch>'Z' && ch<'a'){
                ch='A';
            }
            str2+=ch;
        }
        System.out.println(str2);
    }
}
