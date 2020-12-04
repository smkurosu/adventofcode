#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using std::fstream;
using std::string;
using std::cout;
using std::endl;

int main(){
   std::ifstream fin;
  fin.open("input.txt");
  if (!fin.is_open()){
    cout << "Error opening file\n";
    exit(0);
  }

  string min, max;
  string target;
  string code; 
  int invalid = 0;
  int total = 0;
  while(getline(fin, min, '-')){
    getline(fin, max, ' ');
    getline(fin, target,':');
    getline(fin, code);
    ++total;
    code.erase(std::remove_if(code.begin(), code.end(), isspace), code.end());
    bool badcode = false;
    int counter = 0;
    for (int i = 0; i < code.size(); ++i){
      if (code[i] == target[0]){
        ++counter;
      }
    }
    if(counter < std::stoi(min) || counter > std::stoi(max)) {
      ++invalid;
    }
  }
  cout << "Number of valid passwords: " << total -invalid;
  return 0;
}
