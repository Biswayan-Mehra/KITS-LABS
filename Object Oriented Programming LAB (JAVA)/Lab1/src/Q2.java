import java.util.Scanner;

public class Q2 {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter N: ");
		int N = s.nextInt();
		if (N % 2 != 0)
			System.out.println("Weird");
		else {
			if (N >= 3 && N <= 7)
				System.out.println("Not Weird");
			else if (N >= 8 && N <= 22)
				System.out.println("Weird");
			else if (N > 22)
				System.out.println("Not Weird");
		}

		// Close the Scanner
		s.close();
	}
}
