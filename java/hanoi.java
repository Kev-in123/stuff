public class hanoi {
  public static void main(String[] args) {
    TowerOfHanoi(5, "left", "right", "middle"); // call the function
  }
  public static void TowerOfHanoi(int n, String fromRod, String toRod, String spareRod) {
    if (n == 1) {
      System.out.println("Move disk 1 from rod " + fromRod + " to rod " + toRod); /// display the step
    } else {
      TowerOfHanoi(n - 1, fromRod, spareRod, toRod); // move the disk
      System.out.println("Move disk " + n + " from rod " + fromRod + " to rod " + toRod); // display the step
      TowerOfHanoi(n - 1, spareRod, toRod, fromRod); // move the disk
    }
  }
}
