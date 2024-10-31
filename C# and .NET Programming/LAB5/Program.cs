using System;
using System.Linq;

namespace LAB5
{
    class InvalidAgeException : Exception
    {
        public InvalidAgeException(string message) : base(message) { }
    }

    class InvalidPasswordException : Exception
    {
        public InvalidPasswordException(string message) : base(message) { }
    }

    class ExcessiveAmountException : Exception
    {
        public ExcessiveAmountException(string message) : base(message) { }
    }

    class InsufficientInitialBalanceException : Exception
    {
        public InsufficientInitialBalanceException(string message) : base(message) { }
    }

    class NegativeValueException : Exception
    {
        public NegativeValueException(string message) : base(message) { }
    }

    class ZeroValueException : Exception
    {
        public ZeroValueException(string message) : base(message) { }
    }

    class InvalidVowelException : Exception
    {
        public InvalidVowelException(string message) : base(message) { }
    }

    class Calculator
    {
        public long Power(int baseValue, int exponent)
        {
            if (baseValue < 0 || exponent < 0)
                throw new NegativeValueException("Base or exponent cannot be negative");
            if (baseValue == 0 || exponent == 0)
                throw new ZeroValueException("Base or exponent cannot be zero");

            return (long)Math.Pow(baseValue, exponent);
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Pick an option:");
                Console.WriteLine("1) Banking Application");
                Console.WriteLine("2) Power Function");
                Console.WriteLine("3) Vowel Detection");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        RunBankingApplication();
                        break;
                    case "2":
                        RunPowerFunction();
                        break;
                    case "3":
                        RunVowelDetection();
                        break;
                    default:
                        Console.WriteLine("Invalid option. Please try again.");
                        break;
                }
            }
        }

        static void RunBankingApplication()
        {
            Console.WriteLine("Welcome to the bank. Please register:");

            Console.Write("Enter your ID: ");
            int id = int.Parse(Console.ReadLine());

            Console.Write("Enter your password: ");
            string password = Console.ReadLine();

            if (!IsValidPassword(password))
            {
                return;
            }

            Console.Write("Initial Deposit: ");
            int initialDeposit = int.Parse(Console.ReadLine());

            try
            {
                if (initialDeposit < 500)
                {
                    throw new InsufficientInitialBalanceException("Initial balance must be at least 500");
                }

                Console.Write("Amount to transfer (max 5000): ");
                int transferAmount = int.Parse(Console.ReadLine());

                if (transferAmount > 5000)
                {
                    throw new ExcessiveAmountException("Transfer limit exceeded");
                }

                Console.WriteLine("Transfer successful.");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        static bool IsValidPassword(string password)
        {
            if (password.Length < 9)
            {
                Console.WriteLine("Password must be at least 9 characters long.");
                return false;
            }

            if (!password.Any(char.IsLower))
            {
                Console.WriteLine("Password must contain at least one lowercase letter.");
                return false;
            }

            if (!password.Any(char.IsUpper))
            {
                Console.WriteLine("Password must contain at least one uppercase letter.");
                return false;
            }

            if (!password.Any(char.IsDigit))
            {
                Console.WriteLine("Password must contain at least one digit.");
                return false;
            }

            return true;
        }

        static void RunPowerFunction()
        {
            try
            {
                Console.Write("Enter base value: ");
                int baseValue = int.Parse(Console.ReadLine());

                Console.Write("Enter exponent value: ");
                int exponent = int.Parse(Console.ReadLine());

                Calculator calculator = new Calculator();
                long result = calculator.Power(baseValue, exponent);

                Console.WriteLine($"Result: {result}");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        static void RunVowelDetection()
        {
            Console.Write("Enter comma-separated characters: ");
            string input = Console.ReadLine();
            string[] inputs = input.Split(',');

            string[] vowels = { "a", "e", "i", "o", "u" };
            bool allVowels = true;

            foreach (string item in inputs)
            {
                string trimmedInput = item.Trim().ToLower();

                if (!vowels.Contains(trimmedInput))
                {
                    allVowels = false;
                    Console.WriteLine($"Invalid vowel: '{trimmedInput}'");
                }
            }

            if (allVowels)
            {
                Console.WriteLine("All inputs are valid vowels.");
            }
        }
    }
}
