import java.util.Scanner;

public class exponent {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int m = s.nextInt();
    System.out.println(recursiveExp(n, m));
    s.close();
  }

  public static int recursiveExp(int n, int r) {
    if (r == 0) {
      return 1;
    } else {
      return n * recursiveExp(n, r - 1);
    }
  }
  
}