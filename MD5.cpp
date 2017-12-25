// MD5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

void main(int argc,char* args[])
{
	char filename[256];   //文件名
	FILE *fp;
	while(1)
	{
		if(args[1]!=NULL)
		{
			strncpy(filename,args[1],sizeof(filename));
		}
		else
		{
			printf("Input file path: ");
			gets(filename);    //用get函数,避免scanf以空格分割数据
			assert(filename!=NULL);
		}
		if (filename[0]==34) 
		{
			filename[strlen(filename)-1]=0;
			strcpy(filename,filename+1);  //支持文件拖曳,但会多出双引号,这里是处理多余的双引号
		}
		if (!strcmp(filename,"exit")) 
		{
			exit(0); //输入exit退出
		}
		if (!(fp=fopen(filename,"rb"))) //以二进制打开文件
		{
			printf("Can not open this file ! Error Code: %d\n",GetLastError());
			//continue;
			break;
		}  
		fseek(fp, 0, SEEK_END);  //文件指针转到文件末尾
		if((len=ftell(fp))==-1) 
		{
			printf("Sorry! Can not calculate files which larger than 2 GB!\n");
			fclose(fp);
			//continue;
			break;
		}  //ftell函数返回long,最大为2GB,超出返回-1
		rewind(fp);  //文件指针复位到文件头
		A=0x67452301,B=0xefcdab89,C=0x98badcfe,D=0x10325476; //初始化链接变量
		flen[1]=len/0x20000000;     //flen单位是bit
		flen[0]=(len%0x20000000)*8;
		memset(x,0,64);   //初始化x数组为0
		fread(&x,4,16,fp);  //以4字节为一组,读取16组数据
		for(i=0;i<len/64;i++)
		{    //循环运算直至文件结束
			md5();
			memset(x,0,64);
			fread(&x,4,16,fp);
		}
		((char*)x)[len%64]=128;  //文件结束补1,补0操作,128二进制即10000000
		if(len%64>55) 
		{
			md5();
			memset(x,0,64);
		}
		memcpy(x+14,flen,8);    //文件末尾加入原文件的bit长度
		md5();
		fclose(fp);
		printf("MD5 32 bit Code: 【%08X%08X%08X%08X】\n",PP(A),PP(B),PP(C),PP(D));  //高低位逆反输出
		printf("MD5 16 bit Code: 【%08X%08X】\n",PP(B),PP(C));
		break;
	}
	getch();
}

