public class hanoi {
  public static void main(String[] args) {
    TowerOfHanoi(5, "left", "right", "middle"); // call the function
  }
  public static void TowerOfHanoi(int n, String fromRod, String toRod, String spareRod) {
    if (n == 1) {
      System.out.println("Move disk 1 from rod " + fromRod + " to rod " + toRod); // move the last disk
    } else {
      TowerOfHanoi(n - 1, fromRod, spareRod, toRod); // call the function with a disk moved
      System.out.println("Move disk " + n + " from rod " + fromRod + " to rod " + toRod); //move the disk
      TowerOfHanoi(n - 1, spareRod, toRod, fromRod); // call the function with a disk moved
    }
  }
}
