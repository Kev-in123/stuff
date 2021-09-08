import java.util.Scanner;

public class typewriter {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    String n = s.nextLine();
    typewriter(n);
    s.close();
  }

  public static void typewriter(String n) {
    for (int i = 0; i < n.length(); ++i) {
      char c = n.charAt(i);    
      System.out.print(c);
    }
  }
}
