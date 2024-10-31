using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace LAB6
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = "The mobile numbers on campus are given here 121 999 911 1234567890, 9991234567, 2468643876, 1357909870, 9991234567, 1234543789 and there are so many numbers but everything cannot be included here 1289, 5656, 423432, 9999, these may not be mobile numbers  but you have to filter all the mobile numbers.";
            List<string> mobileNumbers = ExtractMobileNumbers(input);

            Console.WriteLine("\nMenu:");
            Console.WriteLine("1. Mobile Number Operations");
            Console.WriteLine("2. String Combination (short + long + short)");
            Console.WriteLine("3. Count 'code' Variants in a String");
            Console.WriteLine("4. Exit");

            while (true)
            {

                Console.Write("Choose an option: ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        MobileNumberOperations(mobileNumbers);
                        break;
                    case "2":
                        StringCombination();
                        break;
                    case "3":
                        CountCodeVariants();
                        break;
                    case "4":
                        return;
                    default:
                        Console.WriteLine("Invalid option. Please try again.");
                        break;
                }
            }
        }

        static List<string> ExtractMobileNumbers(string input)
        {
            // Regex to extract mobile numbers
            MatchCollection matches = Regex.Matches(input, @"\b\d{10}\b|\b999\d{7}\b");
            return matches.Cast<Match>().Select(m => m.Value).ToList();
        }

        static void MobileNumberOperations(List<string> mobileNumbers)
        {
            Console.WriteLine("\nMobile Number Operations:");
            Console.WriteLine("1. Extract all 10-digit numbers");
            Console.WriteLine("2. Display numbers with prefix 999");
            Console.WriteLine("3. Display numbers ending with 0");
            Console.WriteLine("4. Replace all even digits with 1");
            Console.WriteLine("5. Display duplicate numbers");
            Console.WriteLine("6. Concatenate any two numbers");
            Console.WriteLine("7. Return last occurrence of a repeating digit in a number");
            Console.WriteLine("8. Insert 0 at the beginning of 10-digit numbers");
            Console.WriteLine("9. Find first occurrence of a given digit in a number");
            Console.WriteLine("10. List all numbers that have substring 78");
            Console.WriteLine("11. Back to main menu");

            while (true)
            {
                Console.Write("Choose an option: ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        ExtractTenDigitNumbers(mobileNumbers);
                        break;
                    case "2":
                        DisplayNumbersWithPrefix999(mobileNumbers);
                        break;
                    case "3":
                        DisplayNumbersEndingWith0(mobileNumbers);
                        break;
                    case "4":
                        ReplaceEvenNumbers(mobileNumbers);
                        break;
                    case "5":
                        DisplayDuplicateNumbers(mobileNumbers);
                        break;
                    case "6":
                        ConcatenateTwoNumbers(mobileNumbers);
                        break;
                    case "7":
                        LastOccurrenceOfRepeatingDigit();
                        break;
                    case "8":
                        InsertZeroAtBeginning(mobileNumbers);
                        break;
                    case "9":
                        FindFirstOccurrenceOfDigit();
                        break;
                    case "10":
                        ListNumbersWithSubstring78(mobileNumbers);
                        break;
                    case "11":
                        return;
                    default:
                        Console.WriteLine("Invalid option. Please try again.");
                        break;
                }
            }
        }

        static void ExtractTenDigitNumbers(List<string> mobileNumbers)
        {
            Console.WriteLine("10-digit numbers:");
            foreach (var number in mobileNumbers.Where(num => num.Length == 10))
            {
                Console.WriteLine(number);
            }
        }

        static void DisplayNumbersWithPrefix999(List<string> mobileNumbers)
        {
            Console.WriteLine("Numbers with prefix 999:");
            foreach (var number in mobileNumbers.Where(num => num.StartsWith("999")))
            {
                Console.WriteLine(number);
            }
        }

        static void DisplayNumbersEndingWith0(List<string> mobileNumbers)
        {
            Console.WriteLine("Numbers ending with 0:");
            foreach (var number in mobileNumbers.Where(num => num.EndsWith("0")))
            {
                Console.WriteLine(number);
            }
        }

        static void ReplaceEvenNumbers(List<string> mobileNumbers)
        {
            Console.WriteLine("Replacing even digits with 1:");
            foreach (var number in mobileNumbers)
            {
                string replaced = Regex.Replace(number, "[02468]", "1");
                Console.WriteLine(replaced);
            }
        }

        static void DisplayDuplicateNumbers(List<string> mobileNumbers)
        {
            var duplicates = mobileNumbers.GroupBy(x => x)
                                           .Where(g => g.Count() > 1)
                                           .Select(g => g.Key)
                                           .ToList();

            Console.WriteLine("Duplicate numbers:");
            foreach (var number in duplicates)
            {
                Console.WriteLine(number);
            }
        }

        static void ConcatenateTwoNumbers(List<string> mobileNumbers)
        {
            Console.WriteLine("Enter two numbers to concatenate (separated by space):");
            var input = Console.ReadLine().Split(' ');
            if (input.Length == 2 && mobileNumbers.Contains(input[0]) && mobileNumbers.Contains(input[1]))
            {
                string concatenated = input[0] + input[1];
                Console.WriteLine("Concatenated result: " + concatenated);
            }
            else
            {
                Console.WriteLine("Invalid input. Please ensure both numbers are in the list.");
            }
        }

        static void LastOccurrenceOfRepeatingDigit()
        {
            Console.WriteLine("Enter a number:");
            string number = Console.ReadLine();
            var repeatingDigits = number.GroupBy(c => c).Where(g => g.Count() > 1).Select(g => g.Key);

            foreach (var digit in repeatingDigits)
            {
                int lastIndex = number.LastIndexOf(digit);
                Console.WriteLine($"Last occurrence of digit '{digit}': Index {lastIndex}");
            }
        }

        static void InsertZeroAtBeginning(List<string> mobileNumbers)
        {
            Console.WriteLine("10-digit numbers with 0 at the beginning:");
            foreach (var number in mobileNumbers.Where(num => num.Length == 10))
            {
                Console.WriteLine("0" + number);
            }
        }

        static void FindFirstOccurrenceOfDigit()
        {
            Console.WriteLine("Enter a number:");
            string number = Console.ReadLine();
            Console.WriteLine("Enter a digit to find:");
            char digit = Console.ReadLine()[0];

            int index = number.IndexOf(digit);
            if (index != -1)
            {
                Console.WriteLine($"First occurrence of digit '{digit}': Index {index}");
            }
            else
            {
                Console.WriteLine($"Digit '{digit}' not found in the number.");
            }
        }

        static void ListNumbersWithSubstring78(List<string> mobileNumbers)
        {
            Console.WriteLine("Numbers containing substring '78':");
            foreach (var number in mobileNumbers.Where(num => num.Contains("78")))
            {
                Console.WriteLine(number);
            }
        }

        static void StringCombination()
        {
            Console.WriteLine("Enter first string:");
            string a = Console.ReadLine();
            Console.WriteLine("Enter second string:");
            string b = Console.ReadLine();

            string result = (a.Length < b.Length) ? a + b + a : b + a + b;
            Console.WriteLine($"Result: {result}");
        }

        static void CountCodeVariants()
        {
            Console.WriteLine("Enter a string to count 'code' variants:");
            string input = Console.ReadLine();
            int count = Regex.Matches(input, @"co.e").Count;
            Console.WriteLine($"Count of 'code' variants: {count}");
        }
    }
}