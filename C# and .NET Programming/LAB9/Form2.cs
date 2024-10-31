using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LAB9
{
    public partial class Form2 : Form
    {
        SqlConnection con;
        public Form2()
        {
            InitializeComponent();
            string str = @"Data Source=DRACNIAL\SQLEXPRESS;Initial Catalog=URK21CS1004;Integrated Security=True";
            con = new SqlConnection(str);
            con.Open();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.employeeTableAdapter.Fill(this.uRK21CS1004DataSet.Employee);
        }

        // Button 1 - Insert
        private void button1_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("INSERT INTO [employee] (employee_id, name, job_title) VALUES (@i, @n, @j)", con);

            cmd.Parameters.Add("@i", SqlDbType.Int).Value = int.Parse(textBox1.Text);  // employee_id from textBox1
            cmd.Parameters.Add("@n", SqlDbType.VarChar, 50).Value = textBox2.Text;     // name from textBox2
            cmd.Parameters.Add("@j", SqlDbType.VarChar, 50).Value = textBox3.Text;     // job_title from textBox3

            int i = cmd.ExecuteNonQuery();

            MessageBox.Show("Insert successful");

            SqlDataAdapter adp = new SqlDataAdapter("SELECT * FROM employee", con);
            DataSet ds = new DataSet();
            adp.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];

            // Clear textboxes 1, 2, 3
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
        }

        // Button 3 - Delete
        private void button3_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("DELETE FROM employee WHERE employee_id = @i", con);

            cmd.Parameters.Add("@i", SqlDbType.Int).Value = int.Parse(textBox7.Text);  // employee_id from textBox7

            int i = cmd.ExecuteNonQuery();

            MessageBox.Show("Delete successful");

            SqlDataAdapter adp = new SqlDataAdapter("SELECT * FROM employee", con);
            DataSet ds = new DataSet();
            adp.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];

            // Clear textbox 7
            textBox7.Text = "";
        }

        // Button 2 - Update
        private void button2_Click(object sender, EventArgs e)
        {
            SqlCommand cmd = new SqlCommand("UPDATE employee SET name=@n, job_title=@j WHERE employee_id=@i", con);

            cmd.Parameters.Add("@i", SqlDbType.Int).Value = int.Parse(textBox4.Text);  // employee_id from textBox4
            cmd.Parameters.Add("@n", SqlDbType.VarChar, 50).Value = textBox5.Text;     // name from textBox5
            cmd.Parameters.Add("@j", SqlDbType.VarChar, 50).Value = textBox6.Text;     // job_title from textBox6

            int i = cmd.ExecuteNonQuery();

            MessageBox.Show("Record updated successfully");

            SqlDataAdapter adp = new SqlDataAdapter("SELECT * FROM employee", con);
            DataSet ds = new DataSet();
            adp.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];

            // Clear textboxes 4, 5, 6
            textBox4.Text = "";
            textBox5.Text = "";
            textBox6.Text = "";
        }
    }
}
