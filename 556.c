#include<stdio.h>
void main()
{
	int y,x,z;
	printf("���������ڣ�");
	
	scanf("%d%d%d",&z,&y,&x); 
	int t=z%100;
	int p=z/100;
	if(y<=2){t=t-1,y=y+12;
	}
	int w=t+(t/4)+(p/4)-(2*p);
	int u=26*(y+1)/10;
	int r=x-1;
	int he=w+u+r; 
	switch(he%7)
	{
		case 1:printf("����1",he);break;
			case 2:printf("����2",he);break;
				case 3:printf("����3",he);break;
					case 4:printf("����4",he);break;
						case 5:printf("����5",he);break;
							case 6:printf("����6",he);break;
	default:printf("������",he);break; 
	}
	
	 
	 

 } 
