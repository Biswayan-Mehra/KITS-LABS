import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Scanner;

public class Q5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Your name: ");
        String a = sc.nextLine();
        String b = Character.toString(a.charAt(0));
        System.out.println(b);
        File obj1 = new File("newname.txt");
        try {
            BufferedReader br = new BufferedReader(new FileReader(obj1));
            String st;
            int main_count = 0; // Initialize main_count here
            while ((st = br.readLine()) != null) {
                System.out.println(st);
                String words[] = st.split(" ");
                int line_count = 0; // Initialize line_count for each line
                for (int x = 0; x < words.length; x++) {
                    if (words[x].startsWith(b.toLowerCase())) {
                        line_count += 1; // Increment line_count
                    } else if (words[x].startsWith(b.toUpperCase())) {
                        line_count += 1; // Increment line_count
                    }
                }
                System.out.println(line_count); // Print line_count for debugging
                main_count += line_count; // Add line_count to main_count
            }
            System.out.println("There are a total of " + main_count + " '" + b + "'s in the text file");
            br.close(); // Close the BufferedReader
            sc.close(); // Close the Scanner
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
