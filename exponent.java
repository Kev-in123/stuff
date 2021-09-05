public class exponent {
  public static void main(String[] args) {
    System.out.println(recursiveExp(3, 5));
  }
  public static int recursiveExp(int n, int r) {
    if (r == 0) {
      return 1;
    } else {
      return n * recursiveExp(n, r - 1);
    }
  }
}