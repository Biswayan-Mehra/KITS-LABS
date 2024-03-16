import java.util.Scanner;

public class Q5 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.print("Enter the no. of orders: ");
		int n = input.nextInt();

		int order[] = new int[3], orderNo;
		FlowerOrderThread processes[] = new FlowerOrderThread[n];

		for (orderNo = 1; orderNo <= n; orderNo++) {
			System.out.print("Enter no. of roses: ");
			order[0] = input.nextInt();

			System.out.print("Enter no. of daisies: ");
			order[1] = input.nextInt();

			System.out.print("Enter no. of lilies: ");
			order[2] = input.nextInt();

			processes[orderNo - 1] = new FlowerOrderThread(orderNo, order, input);
			System.out.println("Your order no. is " + orderNo + ".\n");
		}

		for (orderNo = 1; orderNo <= n; orderNo++) {
			processes[orderNo - 1].start();
		}
	}
}

class Task {
	synchronized static void deliverOrder(int orderNo, int[] order, Scanner input) {
		try {
			System.out.println("\nOrder no. " + orderNo + " received");
			Thread.sleep(500);

			System.out.println("\nCollecting " + order[0] + " roses");
			Thread.sleep(2000);

			System.out.println("\nCollecting " + order[1] + " daisies");
			Thread.sleep(2000);

			System.out.println("\nCollecting " + order[2] + " lilies");
			Thread.sleep(2000);

			System.out.println("\nOrder no. " + orderNo + " delivered!");
		} catch (InterruptedException e) {
		} finally {
			input.close(); // Close the Scanner here
		}
	}
}

class FlowerOrderThread extends Thread {
	int orderNo, order[];
	Scanner input;

	public FlowerOrderThread(int orderNo, int[] order, Scanner input) {
		this.orderNo = orderNo;
		this.order = order.clone();
		this.input = input;
	}

	public void run() {
		Task.deliverOrder(orderNo, order, input);
	}
}
