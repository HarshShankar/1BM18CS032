
#include <bits/stdc++.h> 
using namespace std; 
 
string secondMostRepeated(vector<string> seq) 
{ 

	unordered_map<string, int> word; 
	for (int i = 0; i < seq.size(); i++) 
		word[seq[i]]++; 
	unordered_map<string, int>::iterator it;

	int first_max = INT_MIN, sec_largest = INT_MIN; 
	for (it = word.begin(); it != word.end(); it++) { 
		if (it->second > first_max) { 
			sec_largest = first_max; 
			first_max = it->second; 
		} 

		else if (it->second > sec_largest && 
				it->second != first_max) 
			sec_largest = it->second; 
	} 

	for (it = word.begin(); it != word.end(); it++) 
		if (it->second == sec_largest) 
			return it->first;
	return "Number of sequences are inadequate";
} 

int main() { 
  int n;
  vector<string> seq;
  cout << "Enter length of  the array \n";
  cin >> n;
  cout << "Enter sequences \n";
  for (int i = 0; i < n; ++i) {
    string str;
    cin >> str;
    seq.push_back(str);
  }
    cout << "Second most occuring sequence: " << secondMostRepeated(seq) << "\n"; 
    return 0; 
}