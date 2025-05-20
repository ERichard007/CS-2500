/*
Evan Richard
CS-2500
5/12/25
*/

#include <vector>
#include <iostream>
using namespace std;

int swaps = 0, foo = 0, bar = 0, foobar = 0;

void PrintArray(vector<int> array){
    cout << "*****" << endl;
    for (const int& num : array){
        cout << num << endl;
    }
    cout << "*****" << endl;
}

void FooBarCheck(vector<int>& array, const int index1, const int index2){
    long long product = static_cast<long long>(array[index1]) * static_cast<long long>(array[index2]);

    //cout << "PRODUCT OF " << array[index1] << " and " << array[index2] << ": " << product << " = ";
    
<<<<<<< HEAD
    if(product != 0)
    {
        if (product % 5 == 0){
            if (product % 7 == 0){
                foobar += 1;
                cout << "FOOBAR" << endl;
            }else{
                foo += 1;
                cout << "FOO" << endl;
            }
        }else if (product % 7 == 0)
        {
            bar += 1;
            cout << "BAR" << endl;
        }else{
            cout << "NEITHER" << endl;
        }
    }
}

void IntegerSwap(vector<int>& array, const int index1, const int index2){    
=======
    if (product % 5 == 0){
        if (product % 7 == 0){
            foobar += 1;
            //cout << "FOOBAR" << endl;
        }else{
            foo += 1;
            //out << "FOO" << endl;
        }
    }else if (product % 7 == 0)
    {
        bar += 1;
        //cout << "BAR" << endl;
    }else{
        //cout << "NEITHER" << endl;
    }
}

void IntegerSwap(vector<int>& array, const int index1, const int index2){
    FooBarCheck(array, index1, index2);
    
>>>>>>> 29e58f48a2622c09b7863a7ed903e40fe5d1423e
    int temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
    swaps += 1;
}

int HoarePartition(vector<int>& array, int l, int r){
    int p = array[l];
    int i = l;
    int j = r+1;

    do 
    {
        do{
            //cout << "moving from " << array[i] << " to " << array[i+1] << endl;
            i += 1;
<<<<<<< HEAD
        } while(array[i] < p && i < array.size()-1);
        } while(i < r && array[i] < p);

        //cout << array[i] << " failed the first while loop." << endl;
>>>>>>> 29e58f48a2622c09b7863a7ed903e40fe5d1423e

        do{
            //cout << "moving from " << array[j] << " to " << array[j-1] << endl;
            j -= 1;
        } while(array[j] > p);

        //cout << array[j] << " failed the second while loop!" << endl;
        //cout << "SWAPPING NOW!!!!!" << endl;
        IntegerSwap(array, i, j);
        
    } while (j > i);

    //cout << "***ITERATION OF SWAPPING FINNISHED***" << endl;

    IntegerSwap(array, i, j);
    IntegerSwap(array, l, j);
    
    return j;
}

void QuickSort(vector<int>& array, int l, int r){
    if (l < r){
        int s = HoarePartition(array, l, r);
        QuickSort(array, l, s-1);
        QuickSort(array, s+1, r);
    }
}

int main(){
    int input;
    cin >> input;

    vector<int> myArray;
    for (int i = 0; i < input; i++){
        int num;
        cin >> num;
        myArray.push_back(num);
    }

    QuickSort(myArray, 0, myArray.size()-1);

    cout << "***\n" << swaps << "\n" << foo << "\n" << bar << "\n" << foobar << "\n***" << endl;
=======
    cout << swaps << endl;
    cout << foo << endl;
    cout << bar << endl;
    cout << foobar << endl;
>>>>>>> 29e58f48a2622c09b7863a7ed903e40fe5d1423e
    //PrintArray(myArray);
}