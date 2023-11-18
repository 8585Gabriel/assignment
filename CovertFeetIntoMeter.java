import java.util.Scanner;

public class CovertFeetIntoMeter {
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);    
  
System.out.println("Enter the value of feet: ");
double name = input.nextDouble();

double meter = name * 0.305;

System.out.printf("%n%.1f feet is %.4f meters", name,meter);



	}


}
