import java.net.*;
import java.io.*;
import java.util.*;

public class Server {
	public static void main(String[] args) {
		ServerSocket ss = null;
		Socket server = null;
		Scanner sc = null;
		PrintWriter pw = null;

		try {
			ss = new ServerSocket(5000);
			System.out.println("Waiting for Connection...");
			server = ss.accept();
			System.out.println("Server Connected...");

			sc = new Scanner(System.in);
			pw = new PrintWriter(server.getOutputStream(), true); // Auto flush set to true

			while (true) {
				System.out.print("Enter Data: ");
				String data = sc.nextLine();
				pw.println(data);
			}
		} catch (IOException e) {
			System.out.println(e);
		} finally {
			try {
				if (ss != null) {
					ss.close();
					System.out.println("ServerSocket Closed.");
				}
				if (sc != null) {
					sc.close();
					System.out.println("Scanner Closed.");
				}
				if (server != null) {
					server.close();
					System.out.println("Server Disconnected.");
				}
			} catch (IOException e) {
				System.out.println(e);
			}
		}
	}
}
