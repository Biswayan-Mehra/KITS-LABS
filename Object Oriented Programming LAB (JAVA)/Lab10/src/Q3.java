import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;

public class Q3 implements ActionListener {
	JFrame frame;
	JRadioButton r1, r2, r3;
	JLabel text;
	ButtonGroup G;

	Q3() {
		frame = new JFrame();
		frame.setTitle("GUI 2");

		text = new JLabel();
		text.setText("Please choose your favorite language: ");
		text.setBounds(0, 0, 190, 25);

		r1 = new JRadioButton();
		r2 = new JRadioButton();
		r3 = new JRadioButton();

		G = new ButtonGroup();
		G.add(r1);
		G.add(r2);
		G.add(r3);

		r1.setText("JAVA");
		r1.setBounds(0, 20, 190, 25);
		r1.addActionListener(this);
		frame.add(r1);

		r2.setText("CPP");
		r2.setBounds(0, 40, 190, 25);
		r2.addActionListener(this);
		frame.add(r2);

		r3.setText("Python");
		r3.setBounds(0, 60, 190, 25);
		r3.addActionListener(this);
		frame.add(r3);

		frame.add(text);
		frame.setLayout(null);
		frame.setSize(500, 500);
		frame.setVisible(true);
	}

	public static void main(String[] args) {
		new Q3(); // Create an instance of Q3 directly
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == r1) {
			JOptionPane.showMessageDialog(frame, "Hello JAVA");
			G.clearSelection();
		}
		if (e.getSource() == r2) {
			JOptionPane.showMessageDialog(frame, "Hello CPP");
			G.clearSelection();
		}
		if (e.getSource() == r3) {
			JOptionPane.showMessageDialog(frame, "Hello Python");
			G.clearSelection();
		}
	}
}
