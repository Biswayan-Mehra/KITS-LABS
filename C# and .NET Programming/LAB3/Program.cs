using System;

namespace LAB3
{
    interface IOperations { void Display(); }

    class Time : IOperations
    {
        private int hour, min, sec;

        public Time() { hour = 0; min = 0; sec = 0; }

        public Time(int h, int m, int s) { hour = h; min = m; sec = s; NormalizeTime(); }

        public void Display() { Console.WriteLine($"{hour:D2}:{min:D2}:{sec:D2}"); }

        private void NormalizeTime()
        {
            if (sec >= 60) { min += sec / 60; sec %= 60; }
            if (min >= 60) { hour += min / 60; min %= 60; }
        }

        public static Time operator +(Time t1, Time t2)
        {
            return new Time(t1.hour + t2.hour, t1.min + t2.min, t1.sec + t2.sec);
        }

        public static Time operator -(Time t1, Time t2)
        {
            int totalSec1 = t1.hour * 3600 + t1.min * 60 + t1.sec;
            int totalSec2 = t2.hour * 3600 + t2.min * 60 + t2.sec;
            int diffSec = Math.Abs(totalSec1 - totalSec2);
            return new Time(diffSec / 3600, (diffSec % 3600) / 60, diffSec % 60);
        }

        public static bool operator ==(Time t1, Time t2)
        {
            return t1.hour == t2.hour && t1.min == t2.min && t1.sec == t2.sec;
        }

        public static bool operator !=(Time t1, Time t2)
        {
            return !(t1 == t2);
        }

        public static bool operator <=(Time t1, Time t2)
        {
            if (t1.hour < t2.hour) return true;
            if (t1.hour == t2.hour && t1.min < t2.min) return true;
            if (t1.hour == t2.hour && t1.min == t2.min && t1.sec <= t2.sec) return true;
            return false;
        }

        public static bool operator >=(Time t1, Time t2)
        {
            return !(t1 <= t2);
        }

        public static explicit operator int(Time t)
        {
            return t.hour * 3600 + t.min * 60 + t.sec;
        }

        public static implicit operator Time(int totalSeconds)
        {
            return new Time(totalSeconds / 3600, (totalSeconds % 3600) / 60, totalSeconds % 60);
        }

        public override bool Equals(object obj)
        {
            if (obj is Time) { Time t = (Time)obj; return this == t; }
            return false;
        }

        public override int GetHashCode()
        {
            return hour.GetHashCode() ^ min.GetHashCode() ^ sec.GetHashCode();
        }
    }

    class TimeTest
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Time 1 (hours minutes seconds):");
            Time t1 = InputTime();
            Console.Write("Enter Time 2 (hours minutes seconds):");
            Time t2 = InputTime();

            Console.WriteLine("\n--- Time Operations Menu ---");
            Console.WriteLine("1. Display Time");
            Console.WriteLine("2. Add Time\n3. Subtract Time");
            Console.WriteLine("4. Compare Time(==)\n5. Compare Time(<=)");
            Console.WriteLine("6. Cast Time to seconds\n7. Cast seconds to Time\n8. Exit");

            while (true)
            {
                Console.Write("Enter your choice: ");
                int choice = int.Parse(Console.ReadLine());
                switch (choice)
                {
                    case 1: 
                        Console.Write("Time 1:"); t1.Display(); 
                        Console.Write("Time 2:"); t2.Display(); 
                        break;
                    case 2: 
                        Time t3 = t1 + t2; Console.Write("Result of Addition:"); 
                        t3.Display(); 
                        break;
                    case 3: 
                        Time t4 = t1 - t2; 
                        Console.Write("Result of Subtraction:"); 
                        t4.Display(); 
                        break;
                    case 4: 
                        Console.WriteLine($"Time 1 == Time 2: {t1 == t2}"); 
                        break;
                    case 5: 
                        Console.WriteLine($"Time 1 <= Time 2: {t1 <= t2}"); 
                        break;
                    case 6: 
                        int totalSeconds1 = (int)t1; 
                        int totalSeconds2 = (int)t2; 
                        Console.WriteLine($"Time 1 in total seconds: {totalSeconds1}\nTime 2 in total seconds: {totalSeconds2}"); 
                        break;
                    case 7: 
                        Console.Write("Enter total seconds to convert to Time: "); 
                        int seconds = int.Parse(Console.ReadLine()); 
                        Time t5 = seconds; 
                        Console.WriteLine("Converted Time:"); t5.Display(); 
                        break;
                    case 8: 
                        return;
                    default: 
                        Console.Write("Invalid choice. Please try again."); 
                        break;
                }
            }
        }

        static Time InputTime()
        {
            string[] timeParts = Console.ReadLine().Split();
            int h = int.Parse(timeParts[0]);
            int m = int.Parse(timeParts[1]);
            int s = int.Parse(timeParts[2]);
            return new Time(h, m, s);
        }
    }
}
