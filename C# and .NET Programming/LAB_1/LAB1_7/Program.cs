using System;
using System.Collections.Generic;
using System.Linq;

namespace LAB1_7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> regnos = new List<string>();

            foreach (var regno in Console.ReadLine().Split())
                regnos.Add("URK21CS" + regno);
 
            Console.Write("\nReg no: ");
            Console.WriteLine(string.Join(" ", regnos));
   
            Console.Write("\nEnter search Reg No: ");
            string searchRegno = "URK21CS" + Console.ReadLine();

            bool found = regnos.Contains(searchRegno, StringComparer.OrdinalIgnoreCase);
            Console.WriteLine(found
                ? $"\n{searchRegno} was found in the list."
                : $"\n{searchRegno} was not found in the list.");

            Console.ReadKey();
        }
    }
}