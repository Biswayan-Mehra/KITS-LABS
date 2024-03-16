import java.util.Scanner;
import java.util.Arrays;

public class Q4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no. of People:");
        int n = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        System.out.println("Enter names:");
        String names[] = new String[n];

        for (int i = 0; i < n; i++)
            names[i] = sc.nextLine();

        Arrays.sort(names);

        System.out.println("Sorted names:");
        for (String name : names)
            System.out.println(name);

        // Close the Scanner
        sc.close();
    }
}
