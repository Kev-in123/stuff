public class pi {
  public static void main(String[] args) {
    // initialize variables for the number of points in and outside of a circle
    int in = 0;
    int total = 0;
    double distance;
    // loop 1,000,000 times, increase the value for more a more accurate result
    for (int i = 1; i < 1000000; i++) {
      // generate 1 point and calculates its distance from the origin
      distance = Math.pow((Math.pow(Math.random(), 2) + Math.pow(Math.random(), 2)), 0.5);
      // check the distance and determine if it's in the circle
      if (distance <= 1) {
        in++;
      }
      total++;
    }
    // since the value of in/total is π/4, we multiply it by 4
    System.out.println((double) in/total*4);
  }
}
