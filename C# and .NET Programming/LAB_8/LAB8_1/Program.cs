using System;
using System.Threading;

namespace LAB8_1
{
    internal class Program
    {
        static void printOdd()
        {
            for (int i = 1; i <= 10; i += 2)
            {
                Console.WriteLine("{0} is odd", i);
            }
        }

        static void printEven()
        {
            for (int i = 0; i <= 10; i += 2)
            {
                Console.WriteLine("{0} is even", i);
            }
        }

        static void print5Mul()
        {
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine("{0} x 5 = {1}", i, i * 5);
            }
        }

        static void Main(string[] args)
        {
            Thread t1 = new Thread(new ThreadStart(printEven));
            Thread t2 = new Thread(new ThreadStart(printOdd));
            Thread t3 = new Thread(new ThreadStart(print5Mul));

            t1.Start();
            t2.Start();
            t3.Start();
            Console.ReadKey();
        }
    }
}
