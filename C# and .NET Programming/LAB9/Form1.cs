using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LAB9
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.button1.Click += new System.EventHandler(this.button1_Click);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string name = textBox1.Text;
            string pass = textBox2.Text;

            // Check if fields are not empty
            if (string.IsNullOrWhiteSpace(name) || string.IsNullOrWhiteSpace(pass))
            {
                MessageBox.Show("Please enter both username and password.");
                return;
            }

            // Validate user credentials for "admin"
            if (name == "admin" && pass == "admin")
            {
                Form2 adminForm = new Form2();
                adminForm.Show();
            }
            // Validate user credentials for "mehra"
            else if (name == "user" && pass == "user")
            {
                Form3 mehraForm = new Form3();
                mehraForm.Show();
            }
            // If none of the credentials match
            else
            {
                MessageBox.Show("ERROR: Invalid credentials.");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {
            // This method is currently unused
        }
    }
}
