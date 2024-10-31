using System;
namespace LAB1_1
{
    internal class Program
    {
        public bool isLeapYear(int year) => ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
        
        static void Main(string[] args)
        {
            Program myProg = new Program();
            int year = int.Parse(Console.ReadLine());

            if (myProg.isLeapYear(year))
                Console.WriteLine("It's a Leap Year.");
            else
                Console.WriteLine("Not a Leap Year.");
            
            Console.ReadKey();
        }
    }
}
