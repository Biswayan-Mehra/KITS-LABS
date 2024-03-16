import java.util.*;

class InvalidAgeException extends Exception {
	InvalidAgeException(String message) {
		super(message);
	}
}

class InvalidNameException extends Exception {
	InvalidNameException(String message) {
		super(message);
	}
}

class Employee {
	String name;
	int age;

	Employee(String name, int age) {
		this.name = name;
		this.age = age;
		System.out.println("Object created successfully");
	}
}

public class Q2 {
	public static boolean isAlpha(String s) {
		return s != null && s.matches("^[a-zA-Z]*$");
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your name");
		try {
			String emp_name = sc.nextLine();
			if (!isAlpha(emp_name))
				throw new InvalidNameException("Invalid Name");

			System.out.println("Enter your age: ");
			int emp_age = sc.nextInt();
			if (emp_age > 50)
				throw new InvalidAgeException("Invalid Age");

		} catch (InvalidNameException e) {
			System.out.println("INVALID NAME: " + e.getMessage());
			System.out.println("Please use a proper name without numbers");
		} catch (InvalidAgeException d) {
			System.out.println("INVALID AGE: " + d.getMessage());
			System.out.println("Please check your age");
		} finally {
			sc.close(); // Close the Scanner
		}
	}
}
