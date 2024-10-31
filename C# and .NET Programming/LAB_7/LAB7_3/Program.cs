using System;
using System.Collections.Generic;

namespace LAB7_3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Stack<int> stack = new Stack<int>();
            bool running = true;

            while (running)
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Push to stack");
                Console.WriteLine("2. Pop from stack");
                Console.WriteLine("3. Iterate through stack elements");
                Console.WriteLine("4. See the number of stack elements");
                Console.WriteLine("5. See the top of stack");
                Console.WriteLine("6. Exit");
                Console.Write("Enter your choice: ");

                switch (int.Parse(Console.ReadLine()))
                {
                    case 1:
                        Console.Write("Enter the integer to push: ");
                        stack.Push(int.Parse(Console.ReadLine()));
                        Console.WriteLine("Pushed value to the stack.");
                        break;

                    case 2:
                        if (stack.Count > 0)
                        {
                            int poppedValue = stack.Pop();
                            Console.WriteLine("Popped {0} from the stack.", poppedValue);
                        }
                        else
                        {
                            Console.WriteLine("Stack is empty.");
                        }
                        break;

                    case 3:
                        if (stack.Count > 0)
                        {
                            Console.WriteLine("Stack elements:");
                            foreach (int item in stack)
                            {
                                Console.WriteLine(item);
                            }
                        }
                        else
                        {
                            Console.WriteLine("Stack is empty.");
                        }
                        break;

                    case 4:
                        Console.WriteLine("Number of stack elements: {0}", stack.Count);
                        break;

                    case 5:
                        if (stack.Count > 0)
                        {
                            Console.WriteLine("Top of the stack: {0}", stack.Peek());
                        }
                        else
                        {
                            Console.WriteLine("Stack is empty.");
                        }
                        break;

                    case 6:
                        running = false;
                        Console.WriteLine("Exiting...");
                        break;

                    default:
                        Console.WriteLine("Invalid choice. Please select a valid option.");
                        break;
                }
            }
        }
    }
}
