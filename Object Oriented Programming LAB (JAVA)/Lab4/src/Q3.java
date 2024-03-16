import java.util.Scanner;

class Distance {
	float feet, inches;

	Distance() {
		feet = 0;
		inches = 0;
	}

	Distance(float f, float i) {
		feet = f;
		inches = i;
	}

	Distance addDistance(Distance d1) {
		float totalFeet = feet + d1.feet + (inches + d1.inches) / 12;
		float newFeet = totalFeet % 1;
		float newInches = (totalFeet - newFeet) * 12;
		return new Distance(newFeet, newInches);
	}

	void display() {
		System.out.printf("\nFeet: %.2f\nInches: %.2f\n", feet, inches);
	}
}

public class Q3 {
	public static void main(String[] args) {
		Distance d1 = new Distance();
		d1.display();

		Scanner sc = new Scanner(System.in);
		float feet = sc.nextFloat();
		float inches = sc.nextFloat();
		Distance d2 = new Distance(feet, inches);
		d2.display();

		feet = sc.nextFloat();
		inches = sc.nextFloat();
		Distance d3 = new Distance(feet, inches);
		d3.display();

		Distance d4 = d2.addDistance(d3);
		d4.display();

		// Close the Scanner
		sc.close();
	}
}
