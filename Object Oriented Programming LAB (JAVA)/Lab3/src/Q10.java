import java.util.Scanner;

public class Q10 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Line:");
		String line = sc.nextLine();
		String vowel = "aeiouAEIOU";
		int count = 0;

		for (int i = 0; i < line.length() - 1; i++) {
			if (vowel.indexOf(line.charAt(i)) != -1 && vowel.indexOf(line.charAt(i + 1)) != -1) {
				System.out.printf("%c%c\n", line.charAt(i), line.charAt(i + 1));
				count++;
			}
		}

		System.out.println("Total pairs of consecutive vowels: " + count);

		// Close the Scanner
		sc.close();
	}
}
