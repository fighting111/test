public class demo{
	public static void main(String[] args) {
		
		int j=5;
		for(int i=1;i<=j;i++) 
		{
			
			if(i<=(j+1)/2) 
			{
			  for(int x=1;x<=j;x++)
			  {
				  if(x<=(2*i)-1) 
				  {
					 System.out.print("*") ;
				  }
				  else 
				  {
					 break; 
				  }
			  }System.out.println( );
			}
			else 
			{
				for(int x=1;x<=j;x++)
				  {
					  if(x<=2*(((j+1)/2)*2-i)-1) 
					  {
						 System.out.print("*") ;
					  }
					  else 
					  {
						 break; 
					  }
				  }System.out.println( );
			}
		}
	}
}