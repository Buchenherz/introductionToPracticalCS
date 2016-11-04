#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(){
	int n = 0;
	int i = 2;
	int base = 0;
	printf("Choose number: ");
	scanf("%d\n",&n);
	printf("Choose base: ");
	scanf("%d\n",&base);
	while(i <= n){
		if(pow(base,i)==n){
			printf("The desired number is %d\n.",i);
			return EXIT_SUCCESS;
		} else {
			i++;
		}
	}
	printf("We could not find a possible solution.");
	return EXIT_SUCCESS;
}