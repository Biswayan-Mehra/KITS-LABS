import java.util.Scanner;

public class Q3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter N numbers: ");
		int N = sc.nextInt();
		int arr[] = new int[N];

		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		System.out.println("Original Array:");
		printArray(arr);

		bubbleSort(arr, true); // Ascending
		System.out.println("\nAscending Order:");
		printArray(arr);

		bubbleSort(arr, false); // Descending
		System.out.println("\nDescending Order:");
		printArray(arr);

		// Close the Scanner
		sc.close();
	}

	private static void bubbleSort(int[] arr, boolean ascending) {
		int n = arr.length;
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < n - i - 1; j++) {
				if (ascending ? arr[j] > arr[j + 1] : arr[j] < arr[j + 1]) {
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
	}

	private static void printArray(int[] arr) {
		for (int num : arr) {
			System.out.print(num + " ");
		}
	}
}
