#include <fstream>
#include <iostream>
#include <string>
#include <vector> 

using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;
using std::vector;

int sum2020(vector<int>report) {
  for(int i = 0; i < report.size(); ++i){
    for(int j= i+ 1; j < report.size(); ++j){
      if(report[j] + report[i] == 2020) {
        return report[j] * report[i];
      }
    }
  }
  return 0;
}

int main(){
  vector<int>report;
  std::ifstream fin;
  fin.open("input.txt");
  if (!fin.is_open()){
    cout << "Error opening file\n";
    exit(0);
  }
  string input;
  int counter = 0;
  while(getline(fin, input)){
    report.push_back(std::stoi(input));
  }
  cout << sum2020(report);
  return 0;
}