using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        using (StreamReader fin = new StreamReader("input.txt"))
        using (StreamWriter fout = new StreamWriter("output.txt"))
        {
            SortedSet<(int, int)> heap = new SortedSet<(int, int)>();

            int N = int.Parse(fin.ReadLine());
            string[] line;
            int type;
            int num;

            for (int i = 0; i < N; i++)
            {
                line = fin.ReadLine().Split();
                type = int.Parse(line[0]);

                if (type == 0)
                {
                    num = int.Parse(line[1]);
                    heap.Add((num, i));
                }
                else
                {
                    num = heap.Max.Item1;
                    heap.Remove(heap.Max);
                    fout.WriteLine(num);                    
                }
            }
        }
    }
}