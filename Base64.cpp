// Base64.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main(int argc, char* argv[]=NULL)
{
	if(argv[1]==NULL || argv[2]==NULL)
	{
		cout<<"base64 [-e | -d] code"<<endl;
		return 0;
	}
	ZBase64* base64=new ZBase64();
	if(!strcmp(argv[1],"-e"))
	{
		cout<<base64->Encode(argv[2],strlen(argv[2]))<<endl;
	}
	else if(!strcmp(argv[1],"-d"))
	{		
		cout<<base64->Decode(argv[2],strlen(argv[2]),NULL)<<endl;
	}
	else
	{
		cout<<"Error"<<endl;
	}
	// 	const char* testString="abcdABCD123";
	// 	const char* testCode="YWJjZEFCQ0QxMjM=";
	// 	ZBase64* base64=new ZBase64();
	// 	cout<<base64->Encode(testString,strlen(testString))<<endl;
	// 	cout<<base64->Decode(testCode,strlen(testCode),NULL)<<endl;
	
	return 0;
}
