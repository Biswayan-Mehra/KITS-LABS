using System;
namespace LAB1_3
{
    internal class Program
    {
        static int toAdd(int num1, int num2) => num1 + num2;
        static int toSub(int num1, int num2) => num1 - num2;
        static int toMul(int num1, int num2) => num1 * num2;
        static int toDiv(int num1, int num2) => num1 / num2;

        static void Main(string[] args)
        {
            int num1 = int.Parse(Console.ReadLine());
            int num2 = int.Parse(Console.ReadLine());

            while (true)
            {
                string choice = Console.ReadLine();
                switch (choice)
                {
                    case "+":
                        Console.WriteLine(toAdd(num1, num2));
                        break;
                    case "-":
                        Console.WriteLine(toSub(num1, num2));
                        break;
                    case "*":
                        Console.WriteLine(toMul(num1, num2));
                        break;
                    case "/":
                        Console.WriteLine(toDiv(num1, num2));
                        break;
                    default:
                        Console.WriteLine("Invalid Choice...");
                        break;

                }
            }
        }
    }
}
