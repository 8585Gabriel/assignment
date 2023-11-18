import java.util.Scanner;

public class Interest{

public static void main(String[] args ) {

Scanner input = new Scanner(System.in);

System.out.println("Enter My balance");
int Mybalance = input.nextInt();


System.out.println("Enter your Annual Interest Rate");
float annualInterestRate = input.nextFloat();


 double interest = Mybalance*(annualInterestRate/1200);

System.out.printf("Your Annual Interest is %.6f",interest);


}
}