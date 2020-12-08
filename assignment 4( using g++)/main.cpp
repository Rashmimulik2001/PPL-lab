#include<iostream>
using namespace std;

void swapNumbers(int &x, int &y){
   int temp;
   temp = x;
   x = y;
   y = temp;
}

int main(){
   int a, b;
   cout << "Enter a value for a : " ;
   cin >> a ;
   cout << "Enter a value for b : " ; 
   cin >> b ;
   cout << "Before swap, value of a " << a <<"\n";
   cout << "Before swap, value of b " << b <<"\n";
  
   swapNumbers(a, b);

   cout << "After swap, value of a " << a <<"\n";
   cout << "After swap, value of b " << b <<"\n";

   return 0;
   }