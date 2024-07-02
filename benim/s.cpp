
#include <stdio.h>

int main()
{
	float tutar,kdv,indirim,kdvlitutar,x;
    printf("sirasi ile tutar kdv 100 sini indirim yaz ");
    scanf("%f",&tutar);
    scanf("%f",&kdv);
    scanf("%f",&indirim);
    kdvlitutar = tutar+tutar*kdv/100.;
    printf("kdvli tutar %f ",kdvlitutar);
    x = kdvlitutar-kdvlitutar*indirim/100.;
    printf("insie %f",x);
    if(x<tutar)
    printf("Zarar");
    
    
    
    return 0;
}
