package com.imooc;

public class CharDemo {
	public static void main(String[]args) {
		//����һ����������ַ�'a'
		char a='a';
		System.out.println("a="+a);
		char ch=65535;
		System.out.println("ch="+ch);
		//�������ֵ����char���͵����ݷ�Χ(65535)����Ҫ����ǿ������ת����
		
		char c=(char)65536;
		System.out.println("c"+c);
		//����������Unicode�����ʾ���ַ�
		char ch1='\u005d';
		System.out.println("ch1="+ch1);
		
	}
	

}
