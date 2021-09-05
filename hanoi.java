public class hanoi {
  public static void main(String[] args) {
    TowerOfHanoi(5, "left", "right", "middle");
  }
  public static void TowerOfHanoi(int n, String fromRod, String toRod, String spareRod) {
    if (n == 1) {
      System.out.println("Move disk 1 fromRod " + fromRod + " toRod " + toRod);
    } else {
      TowerOfHanoi(n - 1, fromRod, spareRod, toRod);
      System.out.println("Move disk " + n + " fromRod " + fromRod + " toRod " + toRod);
      TowerOfHanoi(n - 1, spareRod, toRod, fromRod);
    }
  }
}