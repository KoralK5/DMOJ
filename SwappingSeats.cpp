#include <iostream>
#include <string.h>
#include <cmath>
using namespace std;

int main() {
	string books;
	cin>>books;

	int l=0; int m=0; int s=0;
	for (int i=0; i<books.length(); i++){
		l += (books[i] == 'L'); m += (books[i] == 'M'); s += (books[i] == 'S');
	}

	string lp = books.substr(0,l);
	string mp = books.substr(l,l+m);
	string sp = books.substr(l+m,l+m+s);

	int arr[] = {0,0,0,0,0,0};
	for (int i=0; i<books.length(); i++){
		if (i < l){
			arr[0] += (books[i] == 'M');
			arr[1] += (books[i] == 'S');
		}
		else if (l < i < l+m){
			arr[2] += (books[i] == 'L');
			arr[3] += (books[i] == 'S');
		}
		else {
			arr[4] += (books[i] == 'L');
			arr[5] += (books[i] == 'M');
		}
	}

	int n1; int n2; int n3;
	if (arr[0] < arr[2]){n1 = arr[0];} else {n1 = arr[2];}
	if (arr[1] < arr[4]){n2 = arr[1];} else {n2 = arr[4];}
	if (arr[3] < arr[5]){n3 = arr[3];} else {n3 = arr[5];}
	
	cout<<n1+n2+n3+fabs(arr[0]-arr[2])+fabs(arr[1]-arr[4]);
}
