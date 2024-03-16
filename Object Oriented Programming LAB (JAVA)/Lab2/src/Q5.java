import java.util.Scanner;

public class Q5 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter N numbers: ");
		int N = sc.nextInt();
		int arr[] = new int[N];

		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		System.out.println("Enter n numbers: ");
		int n = sc.nextInt();
		int arr_search[] = new int[n];

		for (int i = 0; i < n; i++)
			arr_search[i] = sc.nextInt();

		for (int i = 0; i < N; i++)
			System.out.print(arr[i] + " ");
		System.out.println();

		for (int i = 0; i < n; i++)
			System.out.print(arr_search[i] + " ");
		System.out.println();

		for (int i = 0; i < N; i++)
			for (int j = 0; j < n; j++)
				if (arr[i] == arr_search[j])
					System.out.println("Element: " + arr_search[j] + "\nIndex: " + i);

		// Close the Scanner
		sc.close();
	}
}
