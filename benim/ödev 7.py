#include <stdio.h>
int main()
{
	
	//1.SORU  
int n1, n2;

printf ("birinci sayiyi girin :");
scanf("%d",&n1);

printf ("\nikinci sayiyi girin :");
scanf("%d",&n2);
{
if ( n1 > n2 )
printf ("\n%d > %d",n1 , n2 );
}
{
if ( n1 < n2 )
printf ("\n%d < %d",n1 , n2 ); 


   //2.SORU

int n1;
printf("bir sayi giriniz:");
scanf("%d",&n1);
{

if (n1%2 == 0 )
printf("girdiginiz sayi cifttir. \n");
else
printf("girdiginiz sayi tektir");
}


   //3.SORU
   
float n1, n2;
printf("birinci sayiyi giriniz:");
scanf("%f",&n1);

printf("ikinci sayiyi giriniz:");
scanf("%f",&n2);

{
	if(n1>100)
	printf("sonuc=%f",(n1/100)+n2);

}
{
	if(n1<100)
	printf("sonuc=%f",n2-n1-100);
	
}


   //4.SORU
int n1;

printf("18 yasindan kucuk degilseniz dogum yilinizi giriniz:");
scanf("%d",&n1);
{

if (n1<=2004)
printf("18 yasindan buyuksunuz");

else
printf("18 yasindan kucuksunuz");
}
}

