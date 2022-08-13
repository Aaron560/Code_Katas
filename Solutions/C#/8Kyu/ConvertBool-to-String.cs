using System;
using System.Linq;

public static class Kata
{
  public static string boolToWord(bool word)
  {
    if (word.ToString() == "True") 
    {
      return "Yes";
    }
    else 
    {
      return "No";
    }
  }
}