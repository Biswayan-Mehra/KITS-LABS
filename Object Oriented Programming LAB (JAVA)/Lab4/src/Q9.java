import java.util.ArrayList;
import java.util.Scanner;

class smartphone {
    String productName;
    String operatingSystem;
    double displaySize;
    int memory;

    smartphone() {
        this.productName = "Unknown";
        this.operatingSystem = "Unknown";
        this.displaySize = -1;
        this.memory = -1;
    }

    smartphone(String productName, String operatingSystem, double displaySize, int memory) {
        this.productName = productName;
        this.operatingSystem = operatingSystem;
        this.displaySize = displaySize;
        this.memory = memory;
    }

    String getProductName() {
        return productName;
    }

    void setproductName(String productName) {
        this.productName = productName;
    }

    String getOperatingSystem() {
        return operatingSystem;
    }

    void setOperatingSystem(String operatingSystem) {
        this.operatingSystem = operatingSystem;
    }

    double getDisplaySize() {
        return displaySize;
    }

    void setDisplaySize(double displaySize) {
        this.displaySize = displaySize;
    }

    int getMemory() {
        return memory;
    }

    void setMemory(int memory) {
        this.memory = memory;
    }

    public String toString() {
        return "{productName=" + productName + ", operatingSystem='" + operatingSystem + '\'' + ", displaySize="
                + displaySize + ", memory=" + memory + '}';
    }
}

public class Q9 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input;
        int index;
        ArrayList<smartphone> smartphones = new ArrayList<>();
        while (true) {
            System.out.println("\n1. Add\n" + "2. Edit\n" + "3. Delete\n" + "4. Display\n" + "0. Exit");
            input = in.nextLine();
            switch (input) {
                case "1":
                    smartphone smartphone = new smartphone();
                    System.out.println("Product name:");
                    smartphone.setproductName(in.nextLine());
                    System.out.println("Operating system:");
                    smartphone.setOperatingSystem(in.nextLine());
                    System.out.println("Display size:");
                    smartphone.setDisplaySize(Double.parseDouble(in.nextLine()));
                    System.out.println("Product memory:");
                    smartphone.setMemory(Integer.parseInt(in.nextLine()));
                    smartphones.add(smartphone);
                    break;
                case "2":
                    System.out.println("Enter index:");
                    index = Integer.parseInt(in.nextLine());
                    if (index >= 0 && index < smartphones.size()) {
                        System.out.println("Product name:");
                        smartphones.get(index).setproductName(in.nextLine());
                        System.out.println("Operating system:");
                        smartphones.get(index).setOperatingSystem(in.nextLine());
                        System.out.println("Display size:");
                        smartphones.get(index).setDisplaySize(Double.parseDouble(in.nextLine()));
                        System.out.println("Product memory:");
                        smartphones.get(index).setMemory(Integer.parseInt(in.nextLine()));
                    }
                    break;
                case "3":
                    System.out.println("Enter index:");
                    index = Integer.parseInt(in.nextLine());
                    if (index >= 0 && index < smartphones.size()) {
                        smartphones.remove(index);
                    }
                    break;
                case "4":
                    for (int i = 0; i < smartphones.size(); i++) {
                        System.out.println(smartphones.get(i));
                    }
                    break;
                case "0":
                    in.close(); // Close the Scanner
                    System.exit(0);
            }
        }
    }
}