public class Kata
    {
        public static int FindShort(string s)
        {
            string[] WordArr = s.Split(' ');
            int Shortest = int.MaxValue;
            for (int i = 0; i < WordArr.Length; i++)
            {
                if (WordArr[i].Length < Shortest)
                {
                    Shortest = WordArr[i].Length;
                }
            }
            return Shortest;
        }
    }