import java.util.Scanner;
  
public class Numberofyear{

public static void main(String[] args){

Scanner input = new Scanner(System.in);

System.out.println("Enter of years number");
 
int number = input.nextInt();

int numberOfAge = (number * 365);

System.out.println("numberOfage is %d%n", numberofAge);


}

}