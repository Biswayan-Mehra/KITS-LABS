import java.util.Scanner;

public class Q3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter paragraph:");
		String string = sc.nextLine();
		System.out.println("Enter search word:");
		String sword = sc.nextLine();
		String[] words = string.split(" ");
		int count = 0;
		for (int i = 0; i < words.length; i++) {
			if (sword.equals(words[i])) {
				count++;
				System.out.println("Position: " + (i + 1));
			}
		}
		System.out.println("Search Word appeared: " + count);

		// Close the Scanner
		sc.close();
	}
}
