import java.util.Scanner;

public class Q10 {
	public static void main(String args[]) {
		Scanner input = new Scanner(System.in);
		Worker worker;
		while (true) {
			System.out.println("Calculate Wage for: \n1. Daily Worker\n2. Salaried worker\n3. Exit");
			int choice = input.nextInt();
			if (choice == 3) {
				System.out.println("System Terminated...");
				input.close(); // Close the Scanner
				System.exit(0);
			}
			switch (choice) {
				case 1:
					worker = new DailyWorker();
					System.out.println("\nEnter no. of days worked: ");
					System.out.println("Wages to be paid: " + worker.ComPay(input.nextInt()));
					break;
				case 2:
					worker = new SalariedWorker();
					System.out.println("\nEnter no. of weeks worked: ");
					System.out.println("Wages to be paid: " + worker.ComPay(input.nextInt()));
					break;
				default:
					System.out.println("Invalid Choice...");
			}
		}
	}
}

class Worker {
	String name;
	float salaryRate = 180f;

	float ComPay(int hours) {
		return salaryRate * hours;
	}
}

class DailyWorker extends Worker {
	float ComPay(int days) {
		return salaryRate * days * 24;
	}
}

class SalariedWorker extends Worker {
	float ComPay(int weeks) {
		return salaryRate * weeks * 40;
	}
}
