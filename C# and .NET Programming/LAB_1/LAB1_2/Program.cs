using System;
namespace LAB1_2
{
    internal class Program
    {
        public void primeGenerator(int lowerLimit, int upperLimit)
        {
            bool[] numbers = new bool[upperLimit + 1];
            for (int num = 2; num <= upperLimit; num++)
                numbers[num] = true;
            
            for (int num = 2; num <= upperLimit; num++)
                if (numbers[num])
                {
                    int limit = upperLimit / num;

                    for (int i = 2; i <= limit; i++)
                        numbers[num * i] = false;
                    
                    if (num >= lowerLimit)
                        Console.Write(num + " ");
                    
                }
        }
        static void Main(string[] args)
        {
            int lowerLimit = int.Parse(Console.ReadLine());
            int upperLimit = int.Parse(Console.ReadLine());

            Program myProg = new Program();
            myProg.primeGenerator(lowerLimit, upperLimit);
            Console.ReadKey();
        }
    }
}
