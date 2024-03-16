import java.util.Scanner;

public class Q6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter two Numbers: ");
		int num1 = sc.nextInt(), num2 = sc.nextInt();
		while (true) {
			System.out.println("Select Operation:\n1. +\n2. -\n3. /\n4. *\n5. %\n6. Exit");
			char operation = sc.next().charAt(0);
			if (operation == '+')
				System.out.println(num1 + num2);
			else if (operation == '-')
				System.out.println(num1 - num2);
			else if (operation == '/')
				System.out.println(num1 / num2);
			else if (operation == '*')
				System.out.println(num1 * num2);
			else if (operation == '%')
				System.out.println(num1 % num2);
			else if (operation == '6') {
				// Close the Scanner and exit the loop
				sc.close();
				break;
			}
		}
	}
}
