import java.util.Scanner;

class CashTree {
	String name, location;
	int codeno;

	CashTree(String name, int codeno, String location) {
		this.name = name;
		this.codeno = codeno;
		this.location = location;
	}

	void ViewBalance() {
	}

	void WithDraw() {
	}

	void Deposit() {
	}
}

class SBI_BANK extends CashTree {
	double balance;
	String customer_name;

	SBI_BANK(String name, int codeno, String location, double balance) {
		super(name, codeno, location);
		this.balance = balance;
		this.customer_name = name;
	}

	void ViewBalance() {
		System.out.println("Bank Name: SBI BANK");
		System.out.println("Customer Name: " + customer_name);
		System.out.println("Balance: " + balance);
	}

	void WithDraw(float amount) {
		final float limits = 10000;
		if (amount <= limits && amount <= balance) {
			balance -= amount;
			System.out.println("Withdrawal Successful.");
		} else {
			System.out.println("Withdrawal failed. Limit reached or insufficient balance.");
		}
	}

	void Deposit(float amount) {
		final float interest = 5.40f;
		final float service_charges = 2.50f;
		balance += (amount - service_charges) * interest;
		System.out.println("Deposit Successful.");
	}
}

class HDFC_BANK extends CashTree {
	double balance;
	String customer_name;

	HDFC_BANK(String name, int codeno, String location, double balance) {
		super(name, codeno, location);
		this.balance = balance;
		this.customer_name = name;
	}

	void ViewBalance() {
		System.out.println("Bank Name: HDFC BANK");
		System.out.println("Customer Name: " + customer_name);
		System.out.println("Balance: " + balance);
	}

	void WithDraw(float amount) {
		final float limits = 20000;
		if (amount <= limits && amount <= balance) {
			balance -= amount;
			System.out.println("Withdrawal Successful.");
		} else {
			System.out.println("Withdrawal failed. Limit reached or insufficient balance.");
		}
	}

	void Deposit(float amount) {
		final float interest = 3.25f;
		final float service_charges = 5.50f;
		balance += (amount - service_charges) * interest;
		System.out.println("Deposit Successful.");
	}
}

public class Q3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		SBI_BANK sbi_user = null;
		HDFC_BANK hdfc_user = null;

		while (true) {
			float amount = 0.0f;
			System.out.println("\n--------------------");
			System.out.println("\n1. Add User\n2. Check balance\n3. WithDraw\n4. Deposit\n5. Exit\n");
			System.out.println("--------------------\n");
			System.out.println("Enter Choice: ");
			int choice = sc.nextInt();
			if (choice == 5) {
				System.out.println("System Terminated...");
				sc.close(); // Close the Scanner
				System.exit(0);
			}
			System.out.println("\nEnter codeno: ");
			int codeno = sc.nextInt();
			System.out.println("--------------------\n");

			switch (choice) {
				case 1:
					sc.nextLine();
					System.out.println("Enter Name: ");
					String nname = sc.nextLine();
					System.out.println("Enter Location: ");
					String location = sc.nextLine();
					System.out.println("Enter Balance: ");
					double balance = sc.nextDouble();
					System.out.println("\nChoose the Bank\n1. SBI BANK\n2. HDFC BANK");
					int choose = sc.nextInt();
					if (choose == 1)
						sbi_user = new SBI_BANK(nname, codeno, location, balance);
					else if (choose == 2)
						hdfc_user = new HDFC_BANK(nname, codeno, location, balance);
					break;
				case 2:
					if (sbi_user != null && sbi_user.codeno == codeno)
						sbi_user.ViewBalance();
					else if (hdfc_user != null && hdfc_user.codeno == codeno)
						hdfc_user.ViewBalance();
					else
						System.out.println("User not found.");
					break;
				case 3:
					System.out.println("Enter Withdrawal Amount:");
					amount = sc.nextFloat();
					if (sbi_user != null && sbi_user.codeno == codeno)
						sbi_user.WithDraw(amount);
					else if (hdfc_user != null && hdfc_user.codeno == codeno)
						hdfc_user.WithDraw(amount);
					else
						System.out.println("User not found.");
					break;
				case 4:
					System.out.println("Enter Deposit Amount:");
					amount = sc.nextFloat();
					if (sbi_user != null && sbi_user.codeno == codeno)
						sbi_user.Deposit(amount);
					else if (hdfc_user != null && hdfc_user.codeno == codeno)
						hdfc_user.Deposit(amount);
					else
						System.out.println("User not found.");
					break;
				default:
					System.out.println("Invalid Choice...");
			}
		}
	}
}
