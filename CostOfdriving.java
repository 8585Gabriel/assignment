import java.util.Scanner;

public class CostOfdriving{
public static void main(String[] agrs){

Scanner input = new Scanner(System.in);

System.out.println("Enter the driving distance: ");
double distance = input.nextDouble();

System.out.println("Enter miles per gallon : ");
double miles = input.nextDouble();

System.out.println("Enter price per gallon : ");
double price = input.nextDouble();

double costOfderiveing = (distance/miles)*price;

System.out.printf("costOfderiving is %.3f", costOfderiveing );



}



}







				