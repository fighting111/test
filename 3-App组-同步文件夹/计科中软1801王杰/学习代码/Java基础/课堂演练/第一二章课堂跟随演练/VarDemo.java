package com.imooc;

public class VarDemo {
   public static void main(String[]args) {
	  //定一两个整型变量 x,y
	   //int x=3,y=5;
	   int x=3,y=5;
	   System.out.println("x="+x);
	   System.out.println("y="+y);
	   //关于换行的问题
	   System.out.print(x+"\t"+y+'\n');
	   System.out.print(""+x+'\t'+y+'\n');
	  //System.out.println();//换行
	   //不换行输出
	   System.out.print(x+" "+y);
	   System.out.println("\n\'"+x+"\'");
	   //定义一个汉字的字符
	   char ch='幕';
	   System.out.println(ch);
	   //char 中文='中';
	   //不建议用中文作为变量名
	   //System.out.println(中文);
	   //用科学计数法表示浮点型数据
	   double d=1.23e5;
	   //e表示乘以10的几次方，e的后面数字代表次方
	   float f=1.23E5f;
	   //.2等于0.2
	   double d1=.2;
	   System.out.println("d="+d);
	   System.out.println("f="+f);
	   System.out.println("d1="+d1);
	   
	   
   }
}
