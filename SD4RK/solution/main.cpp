#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main()
{
    string key = "";
    cout << "Keygen for SD4RK's keygenme\n" << "---\n";

    srand(time(nullptr));

    // first 0 - 5 must be between 0x21 (!) and 0x3F (?)
    
    for (int i = 0 ; i < 6 ; i++) {
        key.push_back(0x21 + rand()/(RAND_MAX/(0x3F - 0x21)));
    }

    for (int i = 0 ; i < 3 ; i++) {
        key.push_back(87 + rand()/(RAND_MAX/(126 - 87)));
    }

    key.push_back('@');

    for (int i = 0 ; i < 3 ; i++) {
        key.push_back(36);
    }

    for (int i = 0 ; i < 2 ; i++) {
        key.push_back(80 + rand()/(RAND_MAX/(95 - 80)));
    }   

    // last ch can be anything, is not checked. But we still use 
    key.push_back('M');

    cout << key.c_str() << '\n';   
    return 0;
}
