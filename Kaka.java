import  java.util.Scanner;
public class Kaka{
public static void main(String [] args){

Scanner input = new Scanner(System.in);

System.out.println("Enter a number between 1 and 10: ");
int number = input.nextInt();



if (number < 1 || number >10){
System.out.printf( "Try  one more time");
} 
else{
int counter = 1;
while (counter <= 12){
int multiplication = counter * number;

System.out.printf("%d,x,%d = %d%n",number,counter,multiplication);
counter = counter +1;
}
 
}

}
}