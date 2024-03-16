import java.util.Scanner;

public class Q10 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter N numbers: ");
		int N = sc.nextInt();
		int arr[] = new int[N];
		System.out.println("Enter the key: ");
		int key = sc.nextInt();
		for (int i = 0; i < N; i++)
			arr[i] = sc.nextInt();

		int count = 0;
		int maxcount = 0;
		int element_max_freq = 0;

		for (int i = 0; i < N; i++) {
			if (arr[i] == key)
				++count;

			int count_num = 0;
			for (int j = 0; j < N; j++) {
				if (arr[i] == arr[j])
					count_num++;
			}

			if (count_num > maxcount) {
				maxcount = count_num;
				element_max_freq = arr[i];
			}
		}

		if (count == 0)
			System.out.println(key + " Appears: " + count);
		else
			System.out.println(key + " Appears: " + count);

		System.out.println("Element with max Frequency: " + element_max_freq);

		// Close the Scanner
		sc.close();
	}
}
