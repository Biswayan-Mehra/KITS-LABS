import java.util.Scanner;

public class Q4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter max element: ");
		int n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			for (int j = n; j > i; j--)
				System.out.print(" ");
			for (int j = 1; j <= i; j++)
				System.out.print(j);
			for (int j = i - 1; j >= 1; j--)
				System.out.print(j);
			System.out.println();
		}

		// Close the Scanner
		sc.close();
	}
}
