package Exp6;

import java.util.Scanner;

interface Academic {
	int calAcademicCredit();

	void registerSub(String sub);

	void assignFaculty(String fac);
}

interface NonAcademic {
	int calNonAcademicCredit();

	void registerClub(String club);
}

abstract class Course {
	String name, reg_no;
	String[] subjects = new String[5], faculty = new String[5], clubs = new String[5];

	Course(String n, String reg) {
		name = n;
		reg_no = reg;
	}
}

class Student extends Course implements Academic, NonAcademic {
	Student(String n, String reg) {
		super(n, reg);
	}

	public int calNonAcademicCredit() {
		int c = 0;
		for (String el : clubs) {
			if (!(el == null)) {
				c++;
			}
		}
		return c * 2;
	}

	public void registerClub(String cl) {
		for (int i = 0; i < clubs.length; i++) {
			if (clubs[i] == null) {
				clubs[i] = cl;
				return;
			}
		}
		System.out.println("Maximum capacity reached");
		return;
	}

	public int calAcademicCredit() {
		int c = 0;
		for (String el : subjects) {
			if (!(el == null)) {
				c++;
			}
		}
		return c * 3;
	}

	public void registerSub(String sub) {
		for (int i = 0; i < subjects.length; i++) {
			if (subjects[i] == null) {
				subjects[i] = sub;
				return;
			}
		}
		System.out.println("Maximum capacity reached");
		return;
	}

	public void assignFaculty(String fac) {
		for (int i = 0; i < faculty.length; i++) {
			if (faculty[i] == null) {
				faculty[i] = fac;
				return;
			}
		}
		System.out.println("Maximum capacity reached");
		return;
	}

	public void display() {
		System.out.println("Name: " + name + "\nRegister number: " + reg_no);
		System.out.print("Subjects: ");
		for (int i = 0; i < subjects.length; i++) {
			if (subjects[i] != null)
				System.out.print(subjects[i] + " ");
		}
		System.out.print("\nFaculty: ");
		for (int i = 0; i < faculty.length; i++) {
			if (faculty[i] != null)
				System.out.print(faculty[i] + " ");
		}
		System.out.print("\nClubs: ");
		for (int i = 0; i < clubs.length; i++) {
			if (clubs[i] != null)
				System.out.print(clubs[i] + " ");
		}
		System.out.println(
				"\nAcademic credits: " + calAcademicCredit() + " Non-academic credits: " + calNonAcademicCredit());
	}
}

public class Exp6_1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String n, reg, dat;
		System.out.print("Enter student name: ");
		n = input.nextLine();
		System.out.print("Enter student reg_no: ");
		reg = input.next();
		Student stu = new Student(n, reg);
		int choice;
		char ans;
		do {
			System.out.print("Enter the choice: \n1. register subject\n2. add faculty" +
					"\n3. register club\n4. display\n");
			choice = input.nextInt();
			switch (choice) {
				case 1:
					System.out.print("Enter subject: ");
					input.nextLine();
					dat = input.nextLine();
					stu.registerSub(dat);
					break;
				case 2:
					System.out.print("Enter faculty name: ");
					input.nextLine();
					dat = input.nextLine();
					stu.assignFaculty(dat);
					break;
				case 3:
					System.out.print("Enter club: ");
					input.nextLine();
					dat = input.nextLine();
					stu.registerClub(dat);
					break;
				case 4:
					stu.display();
					input.nextLine();
			}
			System.out.print("Enter y (to continue): ");
			ans = input.next().toLowerCase().charAt(0);
		} while (ans == 'y');

		input.close(); // Close the Scanner
	}
}
