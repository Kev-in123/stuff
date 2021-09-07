public class fibonacci {
	public static void main (String[] args) {
	  System.out.println(calculate(15));
	}
  
	public static long calculate(int n) {
	  if (n == 2 || n == 1) {
		return 1;
	  }
	  long r1 = 1;
	  long r2 = 1;
	  long r = 0;
	  for (int i = 0; i < n - 2; ++i) {
		r = r1 + r2;
		r2 = r1;
		r1 = r;
	  }
	  return r;
	}
}
