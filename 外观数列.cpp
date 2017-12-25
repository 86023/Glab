#include <iostream>  
#include <string.h>  
#include <stdio.h>  
  
using namespace std;  
char list[32][10005];  
  
void Init()  
{  
    for(int i = 0; i < 32; i++)  
        memset(list, 0, sizeof(list));  
    list[1][0] = '1';  
    for(int i = 2; i < 32; i++)  
    {  
        int k = 0;  
        int cnt = 1;  
        int len = strlen(list[i - 1]);  
        for(int j = 0; j < len; j++)  
        {  
            if(list[i - 1][j] == list[i - 1][j + 1]) cnt++;  
            else  
            {  
                list[i][k++] = cnt + '0';  
                list[i][k++] = list[i - 1][j];  
                cnt = 1;  
            }  
        }  
    }  
}  
  
int main()  
{  
    int n;  
    Init();  
    while(cin>>n && n)  
        cout<<strlen(list[n])<<endl;  
    return 0;  