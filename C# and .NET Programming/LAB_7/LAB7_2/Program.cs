using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB7_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, string> library = new Dictionary<string, string>();
            int choice = -1;
            string book, person;

            while (choice != 0)
            {
                Console.WriteLine("\nInventory Management System:");
                Console.WriteLine("1. Add book");
                Console.WriteLine("2. Remove book");
                Console.WriteLine("3. Update record");
                Console.WriteLine("4. View all records");
                Console.WriteLine("5. Display Records Sorted");
                Console.WriteLine("6. Find Record");
                Console.WriteLine("0. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        // Add book
                        Console.Write("Enter name of book: ");
                        book = Console.ReadLine();
                        Console.Write("Enter name of person who has lent it: ");
                        person = Console.ReadLine();
                        if (library.ContainsKey(book))
                        {
                            Console.WriteLine("Book is already in the database");
                        }
                        else
                        {
                            library[book] = person;
                        }
                        break;

                    case 2:
                        // Remove book
                        Console.Write("Enter name of book: ");
                        book = Console.ReadLine();
                        if (library.ContainsKey(book))
                        {
                            Console.WriteLine("Book {0} owned by {1} is removed", book, library[book]);
                            library.Remove(book);
                        }
                        else
                        {
                            Console.WriteLine("Book not present in library");
                        }
                        break;

                    case 3:
                        // Update record
                        Console.Write("Enter name of book: ");
                        book = Console.ReadLine();
                        Console.Write("Enter name of person to lend to: ");
                        person = Console.ReadLine();
                        if (library.ContainsKey(book))
                        {
                            Console.WriteLine("Book {0} owned by {1} is now updated", book, library[book]);
                            library[book] = person;
                        }
                        else
                        {
                            Console.WriteLine("Book not present in library");
                        }
                        break;

                    case 4:
                        // View all records
                        foreach (KeyValuePair<string, string> kvp in library)
                        {
                            Console.WriteLine("{0} lent to {1}", kvp.Key, kvp.Value);
                        }
                        break;

                    case 5:
                        // Display Records Sorted
                        foreach (KeyValuePair<string, string> kvp in library.OrderBy(kvp => kvp.Key))
                        {
                            Console.WriteLine("{0} lent to {1}", kvp.Key, kvp.Value);
                        }
                        break;

                    case 6:
                        // Find Record
                        Console.Write("Enter name of book: ");
                        book = Console.ReadLine();
                        if (library.ContainsKey(book))
                        {
                            Console.WriteLine("Found book {0} owned by {1}", book, library[book]);
                        }
                        else
                        {
                            Console.WriteLine("Book not present in library");
                        }
                        break;

                    case 0:
                        // Exit
                        Console.WriteLine("Exiting...");
                        break;

                    default:
                        Console.WriteLine("Invalid choice, please try again.");
                        break;
                }
            }
        }
    }
}
