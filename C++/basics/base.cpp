#include<iostream>
using namespace std;
template <class T>

class Fun
{
    public:
        static int x;
        Fun(){
            x +=1;
        }
};

template<class T>
int Fun<T>::x = 0;
int main()
{
    Fun<int> a, b;
    Fun<double> c;
    cout << a.x << b.x << c.x;
    return 0;
}