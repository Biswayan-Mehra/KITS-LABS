import javax.swing.*;
import java.awt.event.*;

public class Q1 implements ActionListener {
	JFrame window;
	JLabel user_label, pwd_label;
	JTextField user_field;
	JPasswordField pwd_field;
	JButton submit;

	Q1() {
		window = new JFrame();
		window.setSize(600, 400);
		window.setTitle("Login");
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Set default close operation
		window.setLayout(null); // Use null layout to manually position components
		window.setVisible(true);

		user_label = new JLabel("username: ");
		pwd_label = new JLabel("password: ");
		user_field = new JTextField(15);
		pwd_field = new JPasswordField(15);

		submit = new JButton("Submit");
		submit.addActionListener(this);

		window.add(user_label);
		window.add(user_field);
		window.add(pwd_label);
		window.add(pwd_field);
		window.add(submit);

		user_label.setBounds(20, 20, 100, 20);
		user_field.setBounds(120, 20, 100, 20);
		pwd_label.setBounds(20, 40, 100, 20);
		pwd_field.setBounds(120, 40, 100, 20);
		submit.setBounds(120, 70, 100, 20);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == submit) {
			String username = user_field.getText();
			char[] passwordChars = pwd_field.getPassword();
			String password = new String(passwordChars);

			if (username.equals("Karunya") && password.equals("Karunya")) {
				JOptionPane.showMessageDialog(window, "Login Successful");
			} else {
				JOptionPane.showMessageDialog(window, "Incorrect Credentials");
			}

			// Clear the password field for security
			pwd_field.setText("");
		}
	}

	public static void main(String[] args) {
		SwingUtilities.invokeLater(() -> {
			new Q1(); // Create an instance of Q1 directly without assigning it to a variable
		});
	}

}
