public class Overload {

	public static void main(String[] args) {
		int a=1,b=2;
		System.out.println(add(a,b));
		System.out.println(add(1.5,2.5));
	}

	public static int add(int m, int n) 
	{
		return m + n;
	}
	public static double add(double m, double n)
	{
		return m + n;
	}