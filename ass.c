#include<stdio.h>
#include<string.h>
int z=0,i=0,j=0,c=0;
char a[20],ac[20],stk[20],act[10],al[20],ah[20],ax[20];
void check()
   {
     strcpy(ac,"REDUCE BY S->a");
     for(z=0; z<c; z++)
       if(stk[z]=='a' && stk[z+1]=='1')
         {
           stk[z]='S';
           stk[z+1]='\0';
           printf("\t%s",ac);
           printf("\n$%s\t%s$",stk,a);
           j++;
         }
         else if(stk[z]=='a' && stk[z+1]=='2')
         {
           stk[z]='S';
           stk[z+1]='\0';
           printf("\t%s",ac);
           printf("\n$%s\t%s$",stk,a);
           j++;
         }
         else if(stk[z]=='a' && stk[z+1]=='3')
          {

           stk[z]='S';
           stk[z+1]='\0';
           printf("\t%s",ac);
           printf("\n$%s\t%s$",stk,a);
           j++;
         }
    /*strcpy(al,"REDUCE BY S->S+S");
     for(z=0; z<c; z++)
     {


       if(stk[z]=='S' && stk[z+1]=='+' && stk[z+2]=='S' && stk[z+3]==')')
         {
           stk[z]='S';
           stk[z+1]='\0';
           stk[z+2]='\0';
           printf("\t%s",al);
           printf("\n$%s\t%s$",stk,a);
           i=i-2;
         }
     }*/
     strcpy(al,"REDUCE BY S->S+S");
     for(z=0; z<c; z++)
     {


       if(stk[z]=='S' && stk[z+1]=='+' && stk[z+2]=='S')
         {
           stk[z]='S';
           stk[z+1]='\0';
           stk[z+2]='\0';
           printf("\t%s",al);
           printf("\n$%s\t%s$",stk,a);
           i=i-2;
         }
     }
     strcpy(ah,"REDUCE BY S->S-S");
     for(z=0; z<c; z++){
       if(stk[z]=='S' && stk[z+1]=='-' && stk[z+2]=='S')
         {
           stk[z]='S';
           stk[z+1]='\0';
           stk[z+2]='\0';
           printf("\t%s",ah);
           printf("\n$%s\t%s$",stk,a);
           i=i-2;
         }
         }
    strcpy(ax,"REDUCE BY S->(S)");
     for(z=0; z<c; z++){
       if(stk[z]=='(' && stk[z+1]=='S' && stk[z+2]==')')
         {
           stk[z]='S';
           stk[z+1]='\0';
           stk[z+2]='\0';
           printf("\t%s",ax);
           printf("\n$%s\t%s$",stk,a);
           i=i-2;
         }
     }
   }
int main()
   {

      printf("The grammar is\n S->S+S \n S->S-S \n S->(S) \n S->a\n");
      strcpy(a,"a1-(a2+a3)");
      c=strlen(a);
      strcpy(act,"SHIFT->");
      printf("Stack\t  Input\t\tAction\n");
      printf("\n$\t%s$\t", a);

      for(i=0; j<c; i++,j++)
       {
         if(a[j]=='a' && a[j+1]=='1')
           {
              //stk[i]='\0';
              stk[i]=a[j];
              stk[i+1]=a[j+1];
              stk[i+2]='\0';
              a[j]=' ';
              a[j+1]=' ';
              printf("%sa1",act);
              printf("\n$%s\t%s$",stk,a);
              check();
           }
          else if(a[j]=='a' && a[j+1]=='2')
           {
              stk[i]=a[j];
              stk[i+1]=a[j+1];
              stk[i+2]='\0';
              a[j]=' ';
              a[j+1]=' ';
              printf("\t%sa2",act);
              printf("\n$%s\t%s$",stk,a);
              check();
           }
           else if(a[j]=='a' && a[j+1]=='3')
           {
              stk[i]=a[j];
              stk[i+1]=a[j+1];
             // stk[i+2]=a[j+2];
              stk[i+2]='\0';
              a[j]=' ';
              a[j+1]=' ';
              //a[j+2]=' ';
              printf("\t%sa3",act);
              printf("\n$%s\t%s$",stk,a);
              check();
           }
          /*  else if(a[j]=='+' && a[j+1]=='a' && a[j+2]=='3')
           {
              stk[i]=a[j];
              stk[i+1]=a[j+1];
              stk[i+2]=a[j+2];
              stk[i+3]='\0';
              a[j]=' ';
              a[j+1]=' ';
              a[j+2]=' ';
              printf("\t%s %c",act,stk[i]);
              printf("\n$%s\t%s$",stk,a);
              //check();
           }*/
         else
      {
              stk[i]=a[j];
              stk[i+1]='\0';
              a[j]=' ';
              printf("\t%s %c",act,stk[i]);
              printf("\n$%s\t%s$",stk,a);
              check();
           }

       }
       check();
       if(stk[0] == 'S' && stk[1] == '\0'){
        printf("\tAccept\n");
            }
    else
        {
            printf("\tReject\n");

}

   }

