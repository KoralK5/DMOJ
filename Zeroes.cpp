#include <iostream>
using namespace std;

int main(){
	int n;
	int zeros = 0;

	cin>> n;

	do
	{
		int digit = n%10; 
			if(digit == 0) {zeros++;} 
				n=n/10; 
	}while(n>0);
	
	cout<<zeros;
}

