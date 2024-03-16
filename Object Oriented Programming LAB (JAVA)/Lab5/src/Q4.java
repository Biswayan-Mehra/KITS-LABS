import java.util.*;

class Train {
	String name, source, destination;
	int trainno, no_of_tickets, bookedTickets;
	double cost, totalCost = 0;

	Train(int trainno, String source, String destination, int no_of_tickets, double cost) {
		this.trainno = trainno;
		this.source = source;
		this.destination = destination;
		this.no_of_tickets = no_of_tickets;
		this.cost = cost;
	}

	void Check_SeatAvailability() {
		System.out.println("\nTrain No. Available:" + this.trainno + "\nSeats Available: " + no_of_tickets);
	}

	void BookTicket(String name, int no_of_tickets) {
		this.name = name;
		this.bookedTickets = no_of_tickets;
		if (this.no_of_tickets >= this.bookedTickets) {
			this.no_of_tickets -= this.bookedTickets;
			this.totalCost = this.cost * this.bookedTickets;
		}
	}

	void displayTicket() {
		if (this.totalCost > 0) {
			System.out.println("\n----------------------------\nName: " + this.name + "\nTrain No.: " + this.trainno
					+ "\nSource:" + this.source + "\nDestination: " + this.destination + "\nNo. of Tickets: "
					+ this.bookedTickets + "\nTotal Cost: " + this.totalCost + "\n----------------------------\n");
		}
	}
}

class ChennaiExpress extends Train {
	ChennaiExpress(int trainno, String source, String destination, int no_of_tickets, double cost) {
		super(trainno, source, destination, no_of_tickets, cost);
	}

	void Check_SeatAvailability() {
		super.Check_SeatAvailability();
	}

	void BookTicket(String name, int no_of_tickets) {
		super.BookTicket(name, no_of_tickets);
	}

	void displayTicket() {
		super.displayTicket();
	}
}

class CoimbatoreExpress extends Train {
	CoimbatoreExpress(int trainno, String source, String destination, int no_of_tickets, double cost) {
		super(trainno, source, destination, no_of_tickets, cost);
	}

	void Check_SeatAvailability() {
		super.Check_SeatAvailability();
	}

	void BookTicket(String name, int no_of_tickets) {
		super.BookTicket(name, no_of_tickets);
	}

	void displayTicket() {
		super.displayTicket();
	}
}

public class Q4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Train ExpList[] = {
				new ChennaiExpress(2000, "Mysore", "Chennai", 90, 1800),
				new ChennaiExpress(2001, "Bangalore", "Chennai", 45, 1500),
				new ChennaiExpress(2002, "Kuppam", "Chennai", 15, 1200),
				new CoimbatoreExpress(3001, "Bangalore", "Coimbatore", 55, 1500),
				new CoimbatoreExpress(3002, "Pune", "Coimbatore", 115, 2200)
		};
		while (true) {
			System.out.println("\n----------------------------\nEnter Train No.: ");
			int trainno = sc.nextInt();
			int count = 0;
			for (int i = 0; i < ExpList.length; i++) {
				if (ExpList[i].trainno == trainno)
					count = 1;
			}
			if (count == 0) {
				System.out.println("Train Not Available...");
				continue;
			}
			System.out.println(
					"\n----------------------------\n1. Book Ticket\n2. Check Availability\n3. Display Tickets\n4. Exit\n----------------------------\n");
			System.out.println("Enter the choice:");
			int choice = sc.nextInt();

			if (choice == 4) {
				System.out.println("System Terminated...");
				sc.close(); // Close the Scanner
				System.exit(0);
			}
			sc.nextLine();
			switch (choice) {
				case 1:
					System.out.println("Enter Name: ");
					String name = sc.nextLine();
					System.out.println("Enter no. of Tickets: ");
					int no_of_tickets = sc.nextInt();
					for (int i = 0; i < ExpList.length; i++) {
						if (ExpList[i].trainno == trainno)
							ExpList[i].BookTicket(name, no_of_tickets);
					}
					break;
				case 2:
					System.out.println("\n----------------------------\nEnter Source: ");
					String source = sc.nextLine();
					System.out.println("Enter Destination: ");
					String destination = sc.nextLine();
					for (int i = 0; i < ExpList.length; i++) {
						if (ExpList[i].source.compareToIgnoreCase(source) == 0
								&& ExpList[i].destination.compareToIgnoreCase(destination) == 0)
							ExpList[i].Check_SeatAvailability();
					}
					System.out.println("\n----------------------------\n");
					break;
				case 3:
					for (int i = 0; i < ExpList.length; i++) {
						if (ExpList[i].trainno == trainno)
							ExpList[i].displayTicket();
					}
					break;
				default:
					System.out.println("Invalid Choice...");
			}
		}
	}
}
