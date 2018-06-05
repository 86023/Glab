// MD5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

void main(int argc,char* args[])
{
	char filename[256];   //�ļ���
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
			gets(filename);    //��get����,����scanf�Կո�ָ�����
			assert(filename!=NULL);
		}
		if (filename[0]==34) 
		{
			filename[strlen(filename)-1]=0;
			strcpy(filename,filename+1);  //֧���ļ���ҷ,������˫����,�����Ǵ�������˫����
		}
		if (!strcmp(filename,"exit")) 
		{
			exit(0); //����exit�˳�
		}
		if (!(fp=fopen(filename,"rb"))) //�Զ����ƴ��ļ�
		{
			printf("Can not open this file ! Error Code: %d\n",GetLastError());
			//continue;
			break;
		}  
		fseek(fp, 0, SEEK_END);  //�ļ�ָ��ת���ļ�ĩβ
		if((len=ftell(fp))==-1) 
		{
			printf("Sorry! Can not calculate files which larger than 2 GB!\n");
			fclose(fp);
			//continue;
			break;
		}  //ftell��������long,���Ϊ2GB,��������-1
		rewind(fp);  //�ļ�ָ�븴λ���ļ�ͷ
		A=0x67452301,B=0xefcdab89,C=0x98badcfe,D=0x10325476; //��ʼ�����ӱ���
		flen[1]=len/0x20000000;     //flen��λ��bit
		flen[0]=(len%0x20000000)*8;
		memset(x,0,64);   //��ʼ��x����Ϊ0
		fread(&x,4,16,fp);  //��4�ֽ�Ϊһ��,��ȡ16������
		for(i=0;i<len/64;i++)
		{    //ѭ������ֱ���ļ�����
			md5();
			memset(x,0,64);
			fread(&x,4,16,fp);
		}
		((char*)x)[len%64]=128;  //�ļ�������1,��0����,128�����Ƽ�10000000
		if(len%64>55) 
		{
			md5();
			memset(x,0,64);
		}
		memcpy(x+14,flen,8);    //�ļ�ĩβ����ԭ�ļ���bit����
		md5();
		fclose(fp);
		printf("MD5 32 bit Code: ��%08X%08X%08X%08X��\n",PP(A),PP(B),PP(C),PP(D));  //�ߵ�λ�淴���
		printf("MD5 16 bit Code: ��%08X%08X��\n",PP(B),PP(C));
		break;
	}
	getch();
}

