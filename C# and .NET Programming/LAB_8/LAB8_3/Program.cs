using System;
using System.Threading;

namespace LAB8_3
{
    internal class Program
    {
        public static void GoodMorning()
        {
            while (true)
            {
                Console.WriteLine("Good Morning");
                Thread.Sleep(1000);
            }
        }

        public static void Hello()
        {
            while (true)
            {
                Console.WriteLine("Hello");
                Thread.Sleep(2000);
            }
        }

        public static void Welcome()
        {
            while (true)
            {
                Console.WriteLine("Welcome");
                Thread.Sleep(3000);
            }
        }

        static void Main(string[] args)
        {
            Thread t1 = new Thread(new ThreadStart(GoodMorning));
            Thread t2 = new Thread(new ThreadStart(Hello));
            Thread t3 = new Thread(new ThreadStart(Welcome));

            t1.Start();
            t2.Start();
            t3.Start();
        }
    }
}
