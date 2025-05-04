/*
Evan Richard
CS-2500
4/15/25
*/

#include <iostream>
#include <vector>
using namespace std;

//Just a helper function for testing
void printMyArray(vector<int> myArray){
    cout << "\n***ARRAY***" << endl;
    for (const int& num : myArray){
        cout << num << " ";
    }
    cout << "\n***********" << endl;
}

void BubbleSort(vector<int> array){
    int keyC = 0, arrayS = 0;
    for (int i = 0; i < array.size(); i++){
        for (int j = 0; j < array.size() - 1 - i; j++){
            keyC += 1;
            if (array[j+1] < array[j]){
                arrayS += 1;
                int temp = array[j+1];
                array[j+1] = array[j];
                array[j] = temp;
            }
        }
    }
    cout << keyC << "\n" << arrayS << endl;
    //printMyArray(array);
}

void SelectionSort(vector<int> array){
    int keyC = 0, arrayA = 0;
    for (int i = 0; i < array.size() - 1; i++){
        int min = i;
        for (int j = i + 1; j < array.size(); j++){
            keyC += 1;
            if (array[j] < array[min]){
                min = j;
            }
        }
        arrayA += 1;
        int temp = array[i];
        array[i] = array[min];
        array[min] = temp;
    }

    cout << keyC << "\n" << arrayA << endl;
    //printMyArray(array);
}

void InsertionSort(vector<int> array){
    int keyC = 0, arrayA = 0;
    for (int i = 1; i < array.size(); i++){
        int v = array[i];
        int j = i - 1;
        while (j >= 0){
            keyC += 1;
            if (array[j] > v){
                arrayA += 1;
                array[j + 1] = array[j];
                j -= 1;
            }else{
                break;
            }
        }
        array[j + 1] = v;
        arrayA += 1;
    }

    cout << keyC << "\n" << arrayA << endl;
    //printMyArray(array);
}

int comparisons = 0;
void MergeSort(vector<int>& array){
    if (array.size() > 1){
        vector<int> firstHalf;
        for (int i = 0; i < array.size()/2; i++){
            firstHalf.push_back(array[i]);
        }

        vector<int> secondHalf;
        for (int i = array.size()/2; i < array.size(); i++){
            secondHalf.push_back(array[i]);
        }

        MergeSort(firstHalf);
        MergeSort(secondHalf);

        int i = 0, j = 0, k = 0;
        while (i < firstHalf.size() && j < secondHalf.size()){
            comparisons += 1;
            if (firstHalf[i] < secondHalf[j]){
                array[k] = firstHalf[i];
                i += 1;
            }else{
                array[k] = secondHalf[j];
                j += 1;
            }
            k += 1;
        }

        while (i < firstHalf.size()) {
            array[k++] = firstHalf[i++];
        }
        
        while (j < secondHalf.size()) {
            array[k++] = secondHalf[j++];
        }
    }

    //printMyArray(array);
}

int main(){
    int n;
    cin >> n;

    vector<int> myArray;
    for (int i = 0; i < n; i++){
        int num;
        cin >> num;
        myArray.push_back(num);
    }

    printMyArray(myArray);

    BubbleSort(myArray);
    SelectionSort(myArray);
    InsertionSort(myArray);
    MergeSort(myArray);

    cout << comparisons << endl;
    return -1;
}