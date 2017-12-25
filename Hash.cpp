// Hash.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int main(int argc, char* argv[])
{
	DWORD hash;
	char hashName[256];
	scanf("%255s",hashName);
	hash=GetHash(hashName);
	printf("Result Hash Is: %.8X\n",hash);
	getch();
	return 0;
}
