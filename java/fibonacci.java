import java.util.Scanner; //import Scanner class for input

public class fibonacci {
  public static void main (String[] args) {
    Scanner s = new Scanner(System.in); // set up scanner to take input 
    int n = s.nextInt(); // take input
    System.out.println(calculate(n));
    s.close(); // close the scanner
  }
  
  public static long calculate(int n) {
      if (n == 2 || n == 1) { // if the number requested is the 1st or 2nd fibonacci number
        return 1;
      }
      long r1 = 1; // calculate the nth fibonacci number
      long r2 = 1;
      long r = 0;
      for (int i = 0; i < n - 2; ++i) {
        r = r1 + r2;
        r2 = r1;
        r1 = r;
      }
      return r;
  }
}
