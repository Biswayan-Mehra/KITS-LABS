import java.util.Scanner;

public class Q3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int[][] m1, m2;
		System.out.print("Enter matrix size: ");
		int n = input.nextInt();
		m1 = new int[n][n];
		m2 = new int[n][n];

		System.out.println("Enter 1st square matrix:");
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				m1[i][j] = input.nextInt();

		System.out.println("\nEnter 2nd square matrix:");
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				m2[i][j] = input.nextInt();

		AdditionThread add = new AdditionThread(m1, m2);
		SubtractionThread sub = new SubtractionThread(m1, m2);
		MultiplicationThread mul = new MultiplicationThread(m1, m2);

		add.start();
		sub.start();
		mul.start();

		try {
			add.join();
			sub.join();
			mul.join();
		} catch (InterruptedException e) {
		}

		input.close(); // Close the Scanner
	}

	synchronized static void display(int[][] arr) {
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++)
				System.out.print(arr[i][j] + " ");
			System.out.println();
		}
	}
}

class AdditionThread extends Thread {
	int[][] m1, m2, sum;

	AdditionThread(int[][] m1, int[][] m2) {
		this.m1 = m1;
		this.m2 = m2;
		sum = new int[m1.length][m1[0].length];
	}

	public void run() {
		for (int i = 0; i < m1.length; i++)
			for (int j = 0; j < m1[0].length; j++)
				sum[i][j] = m1[i][j] + m2[i][j];
		System.out.println("\nAddition done...");
		Q3.display(sum);
	}
}

class SubtractionThread extends Thread {
	int[][] m1, m2, diff;

	SubtractionThread(int[][] m1, int[][] m2) {
		this.m1 = m1;
		this.m2 = m2;
		diff = new int[m1.length][m1[0].length];
	}

	public void run() {
		for (int i = 0; i < m1.length; i++)
			for (int j = 0; j < m1[0].length; j++)
				diff[i][j] = m1[i][j] - m2[i][j];
		System.out.println("\nSubtraction done...");
		Q3.display(diff);
	}
}

class MultiplicationThread extends Thread {
	int[][] m1, m2, prod;

	MultiplicationThread(int[][] m1, int[][] m2) {
		this.m1 = m1;
		this.m2 = m2;
		prod = new int[m1.length][m1[0].length];
	}

	public void run() {
		int sum;
		for (int i = 0; i < m1.length; i++) {
			for (int j = 0; j < m1.length; j++) {
				sum = 0;
				for (int k = 0; k < m1.length; k++)
					sum += m1[i][k] * m2[k][j];
				prod[i][j] = sum;
			}
		}
		System.out.println("\nMultiplication done...");
		Q3.display(prod);
	}
}
