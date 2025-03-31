#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

void moveAndCheckDivisibility(vector<vector<int>>& diskOrder, int start, int end, int diskOfInterest, int& diskMove, int& divisibleTimes){
	int currDisk = diskOrder[start].back();
	diskOrder[start].pop_back();
	diskOrder[end].push_back(currDisk);

	if (currDisk == diskOfInterest){
		diskMove++;
	}

	for (const vector<int>& peg : diskOrder){
		int sum = 0;
		if (!peg.empty()){
			for (const int& num : peg){
				sum += num;
			}
			if (sum % 7 == 0){
				divisibleTimes++;
				return;
			}
		}
	}
}

void towerOfHanoi(vector<vector<int>>& diskOrder, int start, int aux, int end, int numDisks, int diskOfInterest, int& timesRun, int& diskMove, int& divisibleTimes){
	timesRun += 1;
	if (numDisks > 1) {
		towerOfHanoi(diskOrder, start, end, aux, numDisks-1, diskOfInterest, timesRun, diskMove, divisibleTimes);
		moveAndCheckDivisibility(diskOrder, start, end, diskOfInterest, diskMove, divisibleTimes);
		towerOfHanoi(diskOrder, aux, start, end, numDisks-1, diskOfInterest, timesRun, diskMove, divisibleTimes);
	}else{
		moveAndCheckDivisibility(diskOrder, start, end, diskOfInterest, diskMove, divisibleTimes);
		return;
	}
}

int main(){
	int runTimes = 0, diskMoves = 0, divisibleTimes = 0; 
	int numDisks;
	vector<vector<int>> diskOrder(3);
	int diskOfInterest;

	cin >> numDisks;

	string line;
	cin.ignore();
	getline(cin, line);
	stringstream ss(line);
	int num;

	int initialSum = 0;
	while (ss >> num){
		diskOrder[0].push_back(num);
		initialSum += num;
	}
	
	if (initialSum % 7 == 0) {divisibleTimes++;}

	cin >> diskOfInterest;
	
	towerOfHanoi(diskOrder, 0, 1, 2, numDisks, diskOfInterest, runTimes, diskMoves, divisibleTimes);
	
	cout << runTimes << endl;
	cout << diskMoves << endl;
	cout << divisibleTimes << endl;
	
	return -1;
}
