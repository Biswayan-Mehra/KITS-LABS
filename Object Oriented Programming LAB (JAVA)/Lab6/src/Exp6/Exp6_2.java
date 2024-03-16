package Exp6;

import java.util.Scanner;
import pkg1.Hostel;
import pkg2.SRA;

public class Exp6_2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Hostel hostels[] = new Hostel[5];
		int nh = 0;
		int ch;
		String d1, d2, d3;
		char ans;
		boolean f;
		do {
			System.out.println("Enter the choice:\n1. add hostel\n2. add SRA" +
					"\n3. view SRAs\n4. add students\n5. view Students");
			ch = input.nextInt();

			switch (ch) {
				case 1:
					if (nh >= 5) {
						System.out.println("Maximum limit reached");
						break;
					}
					input.nextLine();
					System.out.print("Enter hostel name: ");
					d1 = input.nextLine();
					hostels[nh++] = new Hostel(d1);
					break;
				case 2:
					System.out.print("Enter hostel name: ");
					input.nextLine();
					d1 = input.nextLine();
					for (Hostel h : hostels) {
						if (h != null && h.name.toLowerCase().equals(d1)) {
							System.out.print("Enter SRA name: ");
							d2 = input.nextLine().toLowerCase();
							h.add_sra(d2);
							break;
						}
					}
					break;
				case 3:
					for (Hostel h : hostels) {
						if (h == null)
							break;
						System.out.println(h);
					}
					input.nextLine();
					break;
				case 5:
					for (Hostel h : hostels) {
						if (h == null)
							break;
						for (SRA s : h.sras) {
							if (s != null)
								System.out.println(s.view_students());
						}
					}
					input.nextLine();
					break;
				case 4:
					System.out.print("Enter hostel name: ");
					input.nextLine();
					d1 = input.nextLine();
					for (Hostel h : hostels) {
						if (h != null && h.name.toLowerCase().equals(d1)) {
							System.out.print("Enter SRA name: ");
							d2 = input.nextLine().toLowerCase();
							f = false;
							for (SRA s : h.sras) {
								if (s != null) {
									System.out.print(s);
									if (s.name.equals(d2)) {
										System.out.print("Enter student name: ");
										d3 = input.nextLine();
										System.out.print("Enter student reg_no: ");
										d1 = input.nextLine();
										s.assign_student(d3, d1);
										f = true;
										break;
									}
								}
							}
							if (!f) {
								System.out.println("SRA not found");
							}
							break;
						}
					}
			}
			System.out.print("Enter y (to continue): ");
			input.nextLine(); // Consume the newline character
			ans = input.nextLine().toLowerCase().charAt(0);
		} while (ans == 'y');

		input.close(); // Close the Scanner
	}
}
