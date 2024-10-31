using System;
using System.Linq;

namespace LAB4
{
    public class Matrix
    {
        private int rows;
        private int columns;
        private int[,] matrixArray;

        public Matrix(int rows, int columns)
        {
            this.rows = rows;
            this.columns = columns;
            matrixArray = new int[rows, columns];
        }

        public Matrix(int[,] array)
        {
            rows = array.GetLength(0);
            columns = array.GetLength(1);
            matrixArray = array;
        }

        // Override ToString() to display matrix
        public override string ToString()
        {
            string result = "";
            for (int i = 0; i < rows; i++)
            {
                for (int j = 0; j < columns; j++)
                    result += matrixArray[i, j] + "\t";
                result += "\n";
            }
            return result;
        }

        public Matrix Add(Matrix other)
        {
            int[,] resultArray = new int[rows, columns];
            for (int i = 0; i < rows; i++)
                for (int j = 0; j < columns; j++)
                    resultArray[i, j] = this.matrixArray[i, j] + other.matrixArray[i, j];
            return new Matrix(resultArray);
        }

        public Matrix Subtract(Matrix other)
        {
            int[,] resultArray = new int[rows, columns];
            for (int i = 0; i < rows; i++)
                for (int j = 0; j < columns; j++)
                    resultArray[i, j] = this.matrixArray[i, j] - other.matrixArray[i, j];
            return new Matrix(resultArray);
        }

        // Event for display function
        public event Action DisplayEvent;

        // Display method to trigger the event
        public void Display()
        {
            Console.WriteLine("Matrix1: " + this.ToString());
        }

        public void InvokeEvent()
        {
            this.DisplayEvent.Invoke();
        }

        // Lambda function to add 5 to all elements
        public void AddFive()
        {
            matrixArray = matrixArray.Cast<int>().Select(x => x + 5).ToArray().Reshape(rows, columns);
        }
    }

    public static class ArrayExtensions
    {
        // Extension method to reshape a 1D array into a 2D array
        public static T[,] Reshape<T>(this T[] array, int rows, int cols)
        {
            T[,] result = new T[rows, cols];
            for (int i = 0; i < rows; i++)
                for (int j = 0; j < cols; j++)
                    result[i, j] = array[i * cols + j];
            return result;
        }
    }

    // MatrixTest class to test the Matrix operations
    public class MatrixTest
    {
        // Delegates declaration
        public delegate Matrix MatrixOperation(Matrix a, Matrix b);

        static void Main(string[] args)
        {
            Matrix matrix1 = new Matrix(new int[,] { { 1, 2 }, { 3, 4 } });
            Matrix matrix2 = new Matrix(new int[,] { { 5, 6 }, { 7, 8 } });

            MatrixOperation addOperation = (a, b) => a.Add(b);
            MatrixOperation subtractOperation = (a, b) => a.Subtract(b);

            Console.WriteLine("\nMenu:");
            Console.WriteLine("1. Add two Matrices");
            Console.WriteLine("2. Subtract two Matrices");
            Console.WriteLine("3. Array of Delegates (Add & Subtract)");
            Console.WriteLine("4. Multicast Delegates (Add then Subtract)");
            Console.WriteLine("5. Display Matrix");
            Console.WriteLine("6. Add 5 to each element in Matrix1 using Lambda Expression");
            Console.WriteLine("7. Exit");

            while (true)
            {
                Console.Write("Choose an option: ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        Matrix resultAdd = addOperation(matrix1, matrix2);
                        Console.WriteLine("Addition:\n" + resultAdd);
                        break;
                    case "2":
                        Matrix resultSubtract = subtractOperation(matrix1, matrix2);
                        Console.WriteLine("Subtraction:\n" + resultSubtract);
                        break;
                    case "3":
                        MatrixOperation[] operations = { addOperation, subtractOperation };
                        foreach (var operation in operations)
                        {
                            Matrix result = operation(matrix1, matrix2);
                            Console.WriteLine("Operation Result:\n" + result);
                        }
                        break;
                    case "4":
                        MatrixOperation multicastOperation = addOperation + subtractOperation;
                        Matrix resultMulticast = multicastOperation(matrix1, matrix2);
                        Console.WriteLine("Multicast Delegate Result:\n" + resultMulticast);
                        break;
                    case "5":
                        matrix1.DisplayEvent += matrix1.Display;
                        matrix1.InvokeEvent();
                        break;
                    case "6":
                        matrix1.AddFive();
                        Console.WriteLine("Matrix1 after adding 5:\n" + matrix1);
                        break;
                    case "7":
                        return;
                    default:
                        Console.WriteLine("Invalid choice.");
                        break;
                }
            }
        }
    }
}