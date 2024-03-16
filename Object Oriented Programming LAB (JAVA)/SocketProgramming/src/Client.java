import java.net.*;
import java.io.*;

public class Client {
	public static void main(String[] args) {
		Socket client = null;
		try {
			client = new Socket("localhost", 5000);
			System.out.println("Client Connected...");

			BufferedReader br = new BufferedReader(new InputStreamReader(client.getInputStream()));
			String data;
			while ((data = br.readLine()) != null) {
				System.out.println("Server: " + data);
			}
		} catch (IOException e) {
			System.out.println(e);
		} finally {
			try {
				if (client != null) {
					client.close();
					System.out.println("Client Disconnected.");
				}
			} catch (IOException e) {
				System.out.println(e);
			}
		}
	}
}
