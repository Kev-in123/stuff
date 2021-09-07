import java.util.Scanner;

public class is_prime {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    System.out.println(isPrime(n));
    s.close();
  }

  public static boolean isPrime(int n) {
    if (n < 2) {
      return false;
    } else if (n == 2) {
      return true;
    } else {
      return 2 == (Math.pow(2, n) % n);
    }
  }
}
