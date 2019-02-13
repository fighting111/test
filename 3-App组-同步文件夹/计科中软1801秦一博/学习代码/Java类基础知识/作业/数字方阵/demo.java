public class demo {
	
	public static void main(String[] args) {
		int i=1;
		for(int x=1;x<=5;x++)
		{
			for(int j=0;j<=5;j++) 
			{
				if(j<5)
				{
					System.out.print(i+j);
					System.out.print(" ");
				}
				else 
				{				    
					i=i+j;
					break;
				}
			}System.out.println();
		}
		
	}
}