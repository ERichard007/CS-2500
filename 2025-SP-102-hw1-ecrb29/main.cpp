#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

void towerOfHanoi(vector<int>& diskOrder, int n, int& timesRun){
	timesRun += 1;
	if (n > 1) {
		towerOfHanoi(diskOrder, n-1, timesRun);
		towerOfHanoi(diskOrder, n-1, timesRun);
	}else{
		return;
	}
}

int main(){
	int numDisks;
	vector<int> diskOrder;
	int diskOfInterest;

	cin >> numDisks;

	string line;
	cin.ignore();
	getline(cin, line);
	stringstream ss(line);
	int num;

	while (ss >> num){
		diskOrder.push_back(num);
	}
	
	cin >> diskOfInterest;
	
	int run = 0;
	towerOfHanoi(diskOrder, numDisks, run);
	
	cout << "Run: " << run << endl;
	
	return -1;
}
