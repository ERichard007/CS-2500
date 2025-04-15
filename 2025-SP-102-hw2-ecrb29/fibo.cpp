#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<int, int> myDict;
int fiboMethod1(int n){
    myDict[n]+=1;
    if (n <= 1){
        return n;
    }
    else{
        return fiboMethod1(n-1) + fiboMethod1(n-2);
    }
}

int fibo2Count = 0;
vector<vector<int>> fiboMethod2(vector<vector<int>> S, vector<vector<int>> P){
    vector<vector<int>> Q = S;
    int allSameSize = S.size();
    int ct = 0;
    for (int m = 0; m < allSameSize; m++){
        for (int r = 0; r < allSameSize; r++){
            Q[m][r] = 0;
            for (int k = 0; k < allSameSize; k++){
                fibo2Count+=1;
                Q[m][r] += S[m][k] * P[k][r];
            }
        }
    }

    return Q;
}

int main(){
    int n;
    cin >> n;

    int fiboOfN = fiboMethod1(n);
    cout << fiboOfN << endl;

    int ct = 0;
    for (auto it = myDict.begin(); it != myDict.end(); it++){
        cout << "fibo(" << it->first << ") : "<< it->second << endl;
        if (it->second<=fiboOfN && it->second%n==0){ct+=1;}
    }
    cout << ct << endl;

    vector<vector<int>> fiboMatrix = {{0,1},{1,1}};
    vector<vector<int>> newMatrix;
    for (int i = 0; i < n-1; i++){
        newMatrix = fiboMethod2(fiboMatrix, fiboMatrix);
        fiboMatrix = newMatrix;
    }
    cout << fibo2Count << endl;

}