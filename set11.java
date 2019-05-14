import java.util.Scanner
Public class Pos
{
public static void main(String[] args)
{
int a;
Scanner s=new Scanner(System.in);
a=s.nextInt();
if(a>0)
{
System.out.println("Positive");
}
else if(a<0)
{
System.out.println("Negative");
}
else
{
System.out.println("Zero");
}
}
}
