#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define ymin 0
#define ymax 10
double Func(double x)
{
	return(2*exp(-2*x));	
}

int main()
{
	
	FILE *func_analy,*func_rand;
	func_analy=fopen("ex.txt","w");   
    	func_rand=fopen("ex_hist.txt","w");
	int N=10000;
	int n=40;
	int M=100;

	double x[N];
	double Exp[N];
	double y[M];
	double delta,Rand;

	delta=(ymax-ymin)/(double)(M-1.0);

	int i;
	for (i=0;i<N;i++)
	{	
		Rand = (double)rand() / (double)RAND_MAX ;  
		
		x[i]=-0.5*log(Rand);  

		fprintf(func_rand,"%e\n",x[i]); 	
	}
		
	for (i=0;i<M;i++)
	{

		y[i]=ymin+delta*i;    
		Exp[i]=Func(y[i]); 		
		fprintf(func_analy,"%e\t%e\n",y[i],Exp[i]); 
	}

	

	
  return(0);
}












