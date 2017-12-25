#include <iostream>  
#include <string.h>  
#include <stdio.h>  
  
using namespace std;  
typedef long long LL;  
  
const int BASE  = 10000;  
const int DIGIT = 10000;  
const int NUM   = DIGIT >> 2;  
  
int res[NUM], A[NUM], B[NUM], C[NUM];  
  
void set(int res[], int x)  
{  
    for(int i = 0; i < NUM; i++)  
        res[i] = 0;  
    res[0] = x;  
}  
  
void copy(int res[], int x[])  
{  
    for(int i = 0; i < NUM; i++)  
        res[i] = x[i];  
}  
  
bool zero(int res[])  
{  
    for(int i = 0; i < NUM; i++)  
        if(res[i]) return false;  
    return true;  
}  
  
void add(int res[], int x[])  
{  
    for(int i = NUM - 1; i >= 0; i--)  
    {  
        res[i] += x[i];  
        if(res[i] >= BASE && i > 0)  
        {  
            res[i] -= BASE;  
            res[i - 1]++;  
        }  
    }  
}  
  
void sub(int res[], int x[])  
{  
    for(int i = NUM - 1; i >= 0; i--)  
    {  
        res[i] -= x[i];  
        if(res[i] < 0 && i > 0)  
        {  
            res[i] += BASE;  
            res[i - 1]--;  
        }  
    }  
}  
  
void multi(int res[], int x)  
{  
    int t = 0;  
    for(int i = NUM - 1; i >= 0; i--)  
    {  
        res[i] *= x;  
        res[i] += t;  
        t = res[i] / BASE;  
        res[i] %= BASE;  
    }  
}  
  
void div(int res[], int x)  
{  
    int t = 0;  
    for(int i = 0; i < NUM; i++)  
    {  
        res[i] += t * BASE;  
        t = res[i] % x;  
        res[i] /= x;  
    }  
}  
  
void arctan(int res[], int A[], int B[], int x)  
{  
    int m = x * x;  
    int cnt = 1;  
    set(res, 1);  
    div(res, x);  
    copy(A, res);  
    do{  
        div(A, m);  
        copy(B, A);  
        div(B, 2 * cnt + 1);  
        if(cnt & 1)  
            sub(res, B);  
        else  
            add(res, B);  
        cnt++;  
    }while(!zero(B));  
}  
  
void print(int res[])  
{  
    printf("%d.\n", res[0]);  
    for(int i = 1; i < NUM; i++)  
    {  
        printf("%04d", res[i]);  
        if(i % 15 == 0) puts("");  
    }  
    puts("");  
}  
  
void Machin()  
{  
    arctan(res, A, B, 5);  
    multi(res, 4);  
    arctan(C, A, B, 239);  
    sub(res, C);  
    multi(res, 4);  
    print(res);  
}  
  
int main()  
{  
    Machin();  
    return 0;  
}  