package com.imooc;

public class CharDemo {
	public static void main(String[]args) {
		//定义一个变量存放字符'a'
		char a='a';
		System.out.println("a="+a);
		char ch=65535;
		System.out.println("ch="+ch);
		//如果字面值超过char类型的数据范围(65535)，需要进行强制类型转换。
		
		char c=(char)65536;
		System.out.println("c"+c);
		//定义变量存放Unicode编码表示的字符
		char ch1='\u005d';
		System.out.println("ch1="+ch1);
		
	}
	

}
