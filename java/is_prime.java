import java.util.Scanner; //import Scanner class for input

public class is_prime {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in); //set up scanner to take input 
    int n = s.nextInt(); //take input
    System.out.println(isPrime(n));
    s.close(); //close the scanner
  }

  public static boolean isPrime(int n) {
    if (n < 2) { //check if the number is less than 2
      return false;
    } else if (n == 2) { //if the number is 2
      return true;
    } //if the number is prime and isn't 2 the check below must be true
    return (Math.pow(2, n) % n) == 2;
  }
}
