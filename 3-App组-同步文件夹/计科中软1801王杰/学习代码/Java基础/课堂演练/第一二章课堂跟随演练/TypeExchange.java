package com.imooc;

public class TypeExchange {
   public static void main(String[]args) {
	 //char���ͺ�int����֮���ת��
	 char c=(char)65536;
	 int n;
	 n=c;//��ʽ����ת��
	 c=(char)n;
	 
	 //���ͺ͸����͵�����ת������
	 int x=100;
	 long y=x;
	 x=(int)y;
	 float f=10000000000L;
	 System.out.println("f="+f);
	 //�������ݶ�ʧ�����
	 float f1=10986578655L;
	 System.out.println("f1="+f1);
	 
	 
   }
}
