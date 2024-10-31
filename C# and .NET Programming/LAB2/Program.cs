using System;
using System.Collections.Generic;

namespace LAB2
{
    // Interface for Account Holder functionalities
    interface IAccountHolder
    {
        void Deposit(decimal amount);
        void Withdraw(decimal amount);
        void ApplyForLoan(decimal amount, int tenure);
    }

    // Loan Detail Class
    public class Loan
    {
        public decimal LoanAmount { get; set; }
        public int TenureInMonths { get; set; }

        public Loan(decimal loanAmount, int tenureInMonths)
        {
            LoanAmount = loanAmount;
            TenureInMonths = tenureInMonths;
        }

        public override string ToString()
        {
            return $"Loan Amount: {LoanAmount}, Tenure: {TenureInMonths} months";
        }
    }

    // Base Account Class
    public abstract class Account : IAccountHolder
    {
        // Properties
        public int AccountNumber { get; set; }
        public string AccountHolderName { get; set; }
        public decimal Balance { get; set; }
        public List<Loan> Loans { get; set; }

        // Constructor
        public Account(int accountNumber, string accountHolderName, decimal initialBalance)
        {
            AccountNumber = accountNumber;
            AccountHolderName = accountHolderName;
            Balance = initialBalance;
            Loans = new List<Loan>();
        }

        // Virtual Methods for Overriding
        public virtual void Deposit(decimal amount)
        {
            Balance += amount;
            Console.WriteLine($"Deposited {amount} successfully. Current Balance: {Balance}");
        }

        public virtual void Withdraw(decimal amount)
        {
            if (amount <= Balance)
            {
                Balance -= amount;
                Console.WriteLine($"Withdrawn {amount} successfully. Current Balance: {Balance}");
            }
            else
            {
                Console.WriteLine("Insufficient balance.");
            }
        }

        public abstract void ApplyForLoan(decimal amount, int tenure);
    }

    // Savings Account Class
    public class SavingsAccount : Account
    {
        public SavingsAccount(int accountNumber, string accountHolderName, decimal initialBalance)
            : base(accountNumber, accountHolderName, initialBalance)
        {
        }

        public override void Withdraw(decimal amount)
        {
            decimal maximumLimit = 10000; // Example maximum withdrawal limit
            if (amount > maximumLimit)
            {
                Console.WriteLine($"Withdrawal amount exceeds the maximum limit of {maximumLimit}.");
            }
            else
            {
                base.Withdraw(amount);
            }
        }

        public override void ApplyForLoan(decimal amount, int tenure)
        {
            Loan loan = new Loan(amount, tenure);
            Loans.Add(loan);
            Console.WriteLine("Loan applied successfully.");
        }
    }

    // Current Account Class
    public class CurrentAccount : Account
    {
        public CurrentAccount(int accountNumber, string accountHolderName, decimal initialBalance)
            : base(accountNumber, accountHolderName, initialBalance)
        {
        }

        public override void Withdraw(decimal amount)
        {
            decimal maximumLimit = 20000; // Example maximum withdrawal limit
            if (amount > maximumLimit)
            {
                Console.WriteLine($"Withdrawal amount exceeds the maximum limit of {maximumLimit}.");
            }
            else
            {
                base.Withdraw(amount);
            }
        }

        public override void ApplyForLoan(decimal amount, int tenure)
        {
            Console.WriteLine("Current account holders are not eligible for loans.");
        }
    }

    // Admin Class
    public class Admin
    {
        private Dictionary<int, Account> accounts;

        public Admin()
        {
            accounts = new Dictionary<int, Account>();
        }

        public void CreateAccount(string accountType, int accountNumber, string accountHolderName, decimal initialBalance)
        {
            Account account = null;
            if (accountType.ToLower() == "savings")
            {
                account = new SavingsAccount(accountNumber, accountHolderName, initialBalance);
            }
            else if (accountType.ToLower() == "current")
            {
                account = new CurrentAccount(accountNumber, accountHolderName, initialBalance);
            }

            if (account != null)
            {
                accounts.Add(accountNumber, account);
                Console.WriteLine($"{accountType} account created successfully for {accountHolderName} with Account Number: {accountNumber}");
            }
            else
            {
                Console.WriteLine("Invalid account type specified.");
            }
        }

        public void ManageAccountDetails(int accountNumber)
        {
            if (accounts.ContainsKey(accountNumber))
            {
                Account account = accounts[accountNumber];
                Console.WriteLine("Account Details:");
                Console.WriteLine($"Account Number: {account.AccountNumber}");
                Console.WriteLine($"Account Holder Name: {account.AccountHolderName}");
                Console.WriteLine($"Balance: {account.Balance}");
                Console.WriteLine("Loans:");
                if (account.Loans.Count > 0)
                {
                    foreach (var loan in account.Loans)
                    {
                        Console.WriteLine(loan.ToString());
                    }
                }
                else
                {
                    Console.WriteLine("No loans found.");
                }
            }
            else
            {
                Console.WriteLine("Account not found.");
            }
        }

        public Account GetAccount(int accountNumber)
        {
            if (accounts.ContainsKey(accountNumber))
            {
                return accounts[accountNumber];
            }
            else
            {
                Console.WriteLine("Account not found.");
                return null;
            }
        }
    }

    // Program Class
    internal class Program
    {
        static void Main(string[] args)
        {
            Admin admin = new Admin();

            // Admin creating accounts
            admin.CreateAccount("Savings", 1001, "John Doe", 5000);
            admin.CreateAccount("Current", 1002, "Jane Smith", 10000);

            Console.WriteLine();

            // Admin managing account details
            admin.ManageAccountDetails(1001);
            Console.WriteLine();
            admin.ManageAccountDetails(1002);

            Console.WriteLine();

            // Account Holder operations
            Account johnAccount = admin.GetAccount(1001);
            if (johnAccount != null)
            {
                johnAccount.Deposit(2000);
                johnAccount.Withdraw(12000); // Exceeds limit
                johnAccount.Withdraw(8000);
                johnAccount.ApplyForLoan(50000, 24);
                Console.WriteLine();
                admin.ManageAccountDetails(1001);
            }

            Console.WriteLine();

            Account janeAccount = admin.GetAccount(1002);
            if (janeAccount != null)
            {
                janeAccount.Deposit(5000);
                janeAccount.Withdraw(25000); // Exceeds limit
                janeAccount.Withdraw(15000);
                janeAccount.ApplyForLoan(100000, 36); // Not eligible
                Console.WriteLine();
                admin.ManageAccountDetails(1002);
            }

            Console.ReadLine();
        }
    }
}
