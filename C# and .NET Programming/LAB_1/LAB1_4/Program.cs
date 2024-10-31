using System;
using System.Linq;
namespace LAB1_4
{
    internal class Program
    {
        static int Add(params int[] numbers) => numbers.Sum();
        static int Sub(params int[] numbers) => numbers.Aggregate((a, b) => a - b);

        static void Main(string[] args)
        {

            Console.WriteLine("Sum : " + Add(Console.ReadLine().Split().Select(int.Parse).ToArray()));
            Console.WriteLine("Diff: " + Sub(Console.ReadLine().Split().Select(int.Parse).ToArray()));
            Console.ReadKey();
        }
    }
}
