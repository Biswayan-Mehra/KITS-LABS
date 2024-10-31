using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB7_1
{
    internal class Record : IComparable<Record>
    {
        public string itemname;
        public int qty;

        public Record(string i, int q)
        {
            itemname = i;
            qty = q;
        }

        public override string ToString()
        {
            return "Item Name: " + itemname + ", Quantity: " + qty.ToString();
        }

        public int CompareTo(Record that)
        {
            if (string.Compare(this.itemname, that.itemname) == 0)
            {
                return this.qty.CompareTo(that.qty);
            }
            return string.Compare(this.itemname, that.itemname);
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            LinkedList<Record> inventory = new LinkedList<Record>();
            int choice = -1;

            while (choice != 0)
            {
                Console.WriteLine("\nInventory Management System:");
                Console.WriteLine("1. Add Record");
                Console.WriteLine("2. Remove Record");
                Console.WriteLine("3. Insert Record Before Another");
                Console.WriteLine("4. Update Record");
                Console.WriteLine("5. Display Records");
                Console.WriteLine("6. Display Records Sorted");
                Console.WriteLine("7. Find Record");
                Console.WriteLine("0. Exit");
                Console.Write("Enter your choice: ");
                choice = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        // Add Record
                        Console.Write("Enter item name: ");
                        string addName = Console.ReadLine();
                        Console.Write("Enter quantity: ");
                        int addQty = int.Parse(Console.ReadLine());
                        inventory.AddLast(new Record(addName, addQty));
                        Console.WriteLine("Record added.");
                        break;

                    case 2:
                        // Remove Record
                        Console.Write("Enter item name to remove: ");
                        string removeName = Console.ReadLine();
                        Console.Write("Enter quantity: ");
                        int removeQty = int.Parse(Console.ReadLine());
                        var nodeToRemove = inventory.FirstOrDefault(r => r.itemname == removeName && r.qty == removeQty);
                        if (nodeToRemove != null)
                        {
                            inventory.Remove(nodeToRemove);
                            Console.WriteLine("Record removed (if existed).");
                        }
                        else
                        {
                            Console.WriteLine("Record not found.");
                        }
                        break;

                    case 3:
                        // Insert Record Before Another
                        Console.Write("Enter existing item name (to insert before): ");
                        string beforeName = Console.ReadLine();
                        Console.Write("Enter quantity of the existing item: ");
                        int beforeQty = int.Parse(Console.ReadLine());
                        Record beforeRec = new Record(beforeName, beforeQty);
                        Console.Write("Enter new item name to insert: ");
                        string newName = Console.ReadLine();
                        Console.Write("Enter quantity for new item: ");
                        int newQty = int.Parse(Console.ReadLine());
                        Record newRec = new Record(newName, newQty);
                        var nodeBefore = inventory.FirstOrDefault(r => r.itemname == beforeName && r.qty == beforeQty);
                        if (nodeBefore != null)
                        {
                            var node = inventory.Find(nodeBefore);
                            inventory.AddBefore(node, newRec);
                            Console.WriteLine("New record inserted.");
                        }
                        else
                        {
                            Console.WriteLine("Record to insert before not found.");
                        }
                        break;

                    case 4:
                        // Update Record
                        Console.Write("Enter current item name to update: ");
                        string oldName = Console.ReadLine();
                        Console.Write("Enter current quantity: ");
                        int oldQty = int.Parse(Console.ReadLine());
                        Record oldRec = new Record(oldName, oldQty);
                        Console.Write("Enter new item name: ");
                        string updatedName = Console.ReadLine();
                        Console.Write("Enter new quantity: ");
                        int updatedQty = int.Parse(Console.ReadLine());
                        Record updatedRec = new Record(updatedName, updatedQty);
                        var nodeToUpdate = inventory.FirstOrDefault(r => r.itemname == oldName && r.qty == oldQty);
                        if (nodeToUpdate != null)
                        {
                            var node = inventory.Find(nodeToUpdate);
                            node.Value = updatedRec;
                            Console.WriteLine("Record updated.");
                        }
                        else
                        {
                            Console.WriteLine("Record to update not found.");
                        }
                        break;

                    case 5:
                        // Display Records
                        Console.WriteLine("\nDisplaying all records:");
                        foreach (Record rec in inventory)
                        {
                            Console.WriteLine("{0}", rec.ToString());
                        }
                        break;

                    case 6:
                        // Display Records Sorted
                        Console.WriteLine("\nDisplaying all records (sorted):");
                        foreach (Record rec in inventory.OrderBy(rec => rec))
                        {
                            Console.WriteLine("{0}", rec.ToString());
                        }
                        break;

                    case 7:
                        // Find Record
                        Console.Write("Enter item name to find: ");
                        string searchName = Console.ReadLine();
                        bool found = false;
                        foreach (Record rec in inventory)
                        {
                            if (rec.itemname == searchName)
                            {
                                Console.WriteLine("Record found: {0}", rec.ToString());
                                found = true;
                                break;
                            }
                        }
                        if (!found)
                        {
                            Console.WriteLine("Record not found");
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
