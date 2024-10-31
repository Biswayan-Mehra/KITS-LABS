using System;
using System.Collections.Generic;
using System.Threading;

namespace LAB8_2
{
    internal class Program
    {
        // Shared queue between producer and consumer
        static Queue<int> queue = new Queue<int>();

        // Producer method
        static void producer()
        {
            for (int i = 0; i <= 10; i++)
            {
                lock (queue)
                {
                    queue.Enqueue(i);
                    Console.WriteLine("Enqueued {0}", i);
                    Thread.Sleep(3500); // Simulate some delay
                }
            }
        }

        // Consumer method
        static void consumer()
        {
            while (true)
            {
                if (queue.Count > 0)
                {
                    lock (queue)
                    {
                        int num = queue.Dequeue();
                        Console.WriteLine("Dequeued: {0}", num);
                        Thread.Sleep(3000); // Simulate some processing time
                    }
                }
            }
        }

        static void Main(string[] args)
        {
            // Creating producer and consumer threads
            Thread produce = new Thread(new ThreadStart(producer));
            Thread consume = new Thread(new ThreadStart(consumer));

            // Start the threads
            produce.Start();
            consume.Start();

            // Optional: Prevent the main thread from exiting immediately
            produce.Join();
            consume.Join();
        }
    }
}
