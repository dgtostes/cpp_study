/* dgt_lib.c */
#include <stdio.h>
#include "dgt_lib.h"

float ask4float(char sentence[])
{
        float variable2return;
        printf("%s", sentence);
        scanf("%f", &variable2return);
        return variable2return;
}



int ask4int(char sentence[])
{
        int variable2return;
        printf("%s", sentence);
        scanf("%d", &variable2return);
        return variable2return;
}


/*
char ask4char(char sentence[])
{
        char variable2return[1000];
        printf("%s", sentence);
        scanf("%s", &variable2return);
        return variable2return;
}
*/
