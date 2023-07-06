#include <stdio.h>
main()
{
 int a,b,i,sum1,sum2;
 /*{input}*/
 scanf("%d%d",&a,&b);
 sum1=sum2=0;
 for(i=a;i<=b;i++)
 {
  if(i%2==0)
  {
   sum1+=i;
  }
  else
  {
   sum2+=i;
  }
 }
 /*{output}*/
 printf("Sum1=%d, Sum2=%d",sum1,sum2);
}