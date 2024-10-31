using System;

namespace LAB1_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num1 = int.Parse(Console.ReadLine());
            int num2 = int.Parse(Console.ReadLine());

            CalculateSumAndDifference(num1, num2, out int sum, out int diff);

            Console.WriteLine($"Sum: {sum}");
            Console.WriteLine($"Difference: {diff}");
            Console.ReadKey();
        }

        static void CalculateSumAndDifference(int a, int b, out int sum, out int diff)
        {
            sum = a + b;
            diff = a - b;
        }
    }
}
