using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace LAB7_4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string top;
            Stack<string> stack = new Stack<string>();

            Console.Write("Enter the Infix expression: ");
            string[] infix_expression = ("( " + Console.ReadLine() + " )").Split();

            Console.Write("Postfix expression is: ");
            foreach (string element in infix_expression)
            {
                // If the element is an addition or subtraction operator
                if (Regex.IsMatch(element, @"[+-]"))
                {
                    while (stack.Count > 0 && Regex.IsMatch(stack.Peek(), @"[*/%]"))
                    {
                        Console.Write("{0} ", stack.Pop());
                    }
                    stack.Push(element);
                }
                // If the element is a multiplication, division, or modulus operator
                else if (Regex.IsMatch(element, @"[*/%]"))
                {
                    stack.Push(element);
                }
                // If the element is an opening parenthesis
                else if (element == "(")
                {
                    stack.Push(element);
                }
                // If the element is a closing parenthesis
                else if (element == ")")
                {
                    top = stack.Pop();
                    while (top != "(")
                    {
                        Console.Write("{0} ", top);
                        top = stack.Pop();
                    }
                }
                // If the element is an operand
                else
                {
                    Console.Write("{0} ", element);
                }
            }
            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
