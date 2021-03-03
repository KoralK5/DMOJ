#include<stdio.h>
#include<iostream>
using namespace std;

int main () { 
	while (1) {
		int num;
		cout << "ENTER NUMBER: " << endl;
		cin >> num;
		
		if (num == 0) {
			break;
		}

		unsigned long long f[num+1];
		unsigned long long i;
		
		f[0] = 0; 
		f[1] = 1; 
		
		for (i = 2; i <= num; i++) { 
			f[i] = f[i-1] + f[i-2]; 
		} 

		cout << f[num]; 
	}
	return 0;
} 

