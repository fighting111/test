package com.imooc;

public class MathDemo1 {
public static void main(String[]args) {
	//x++
	int x=4;
	int y=(x++)+5;
	System.out.println("x="+x+'\n'+"y="+y);
	//++x
	x=4;
	int y1=(++x)+5;
	System.out.println("x="+x+'\n'+"y1="+y1);
	//--x
	x=4;
	int y2=(--x)+5;
	System.out.println("x="+x+'\n'+"y2="+y2);
	//x--
	x=4;
	int y3=(x--)+5;
	System.out.println("x="+x+'\n'+"y="+y);
	
   }
}
