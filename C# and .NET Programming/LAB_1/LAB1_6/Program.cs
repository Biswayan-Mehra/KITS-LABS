using System;

namespace LAB1_6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num1 = int.Parse(Console.ReadLine());
            int num2 = int.Parse(Console.ReadLine());

            Console.WriteLine($"Before swap: num1 = {num1}, num2 = {num2}");

            SwapNumbers(ref num1, ref num2);

            Console.WriteLine($"After swap: num1 = {num1}, num2 = {num2}");
            Console.ReadKey();
        }

        static void SwapNumbers(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }
    }
}
