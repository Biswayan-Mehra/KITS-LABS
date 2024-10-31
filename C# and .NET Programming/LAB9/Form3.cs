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
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void Form3_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'uRK21CS1004DataSet.Employee' table. You can move, or remove it, as needed.
            this.employeeTableAdapter.Fill(this.uRK21CS1004DataSet.Employee);

        }
    }
}
