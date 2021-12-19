import java.util.Scanner; // import Scanner class for input

public class typewriter {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in); // set up scanner to take input 
    String n = s.nextLine(); // take input
    typewriter(n); // print out the text
    s.close(); // close the scanner
  }

  public static void typewriter(String n) {
    for (int i = 0; i < n.length(); ++i) { // iterate through the length of the string 
      char c = n.charAt(i); // set c to the character of the index int the string
      System.out.print(c); // print the character
    }
  }
}
