import java.util.Scanner;

public class Q1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter N numbers: ");
		int N = sc.nextInt();

		int arr[] = new int[N];

		System.out.println("Enter the key: ");
		int key = sc.nextInt();

		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		int flag = countOccurrences(arr, key);

		if (flag == 0)
			System.out.println("Key doesn't exist.");
		else
			System.out.println("Key exists...\nAppears: " + flag);

		// Close the Scanner
		sc.close();
	}

	private static int countOccurrences(int[] arr, int key) {
		int count = 0;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == key) {
				count++;
			}
		}
		return count;
	}
}
