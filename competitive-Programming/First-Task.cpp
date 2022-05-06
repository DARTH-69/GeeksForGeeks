#include <iostream>
using namespace std;

int main(){
    char str[20]="A String";
    char *pc= str;
    cout<<"The Letter on the index zero -> "<<str[0]<<endl;
    cout<<"The ponter position and the letter t-> "<<*pc<<' '<<pc[3]<<endl;
    pc+=2;
    cout<<*pc<<' '<<pc[2]<<' '<<pc[5];
    return 0;
}
