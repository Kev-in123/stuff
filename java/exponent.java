import java.util.Scanner; //import Scanner class for input

public class exponent {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in); //set up scanner to take input 
        int n = s.nextInt(); //take input
        int m = s.nextInt(); //take input
        System.out.println(recursiveExp(n, m));
        s.close(); //close the scanner
    }

    public static int recursiveExp(int n, int r) {
        if (r == 0) { //if the number is 0
          return 1;
        } else { //calculate the exponent
          return n * recursiveExp(n, r - 1);
        }
    }
}
