import java.util.Scanner;
public class StudentScore{
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);

		int highestScore = 0; 			
		String highestScoreName = ""; 
		


		System.out.print("Enter the number of students:- ");
		
int numberOfStudents = input.nextInt();
		
System.out.println("Enter each student’s name and score");
		
for (int s = 0; s < numberOfStudents; s++) {
System.out.print("Student: " + (s + 1) +"\n   Name:- ");
			String name = input.next();
			
System.out.print(	"   Score: ");
		int score = input.nextInt();
if (score > highestScore)
			
{
highestScore = score;
highestScoreName = name;

			}	

		}


    System.out.println("Student with the highest score: " + highestScoreName);
	}
}