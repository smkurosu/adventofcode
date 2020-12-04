#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using std::fstream;
using std::string;
using std::cout;
using std::endl;

int part1(string code, char target){
  int num = 0;
  for (int i = 0; i < code.size(); ++i){
        if (code[i] == target){
          ++num;
        }
  }
  return num;
}

bool part2(string code, int pos1, int pos2, char target){

  if(code[pos1-1] == target && code[pos2-1] != target){
    return true;
  }
  else if(code[pos1-1] != target && code[pos2-1] == target){
    return true;
  }
  else{
    return false;
  }
}


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
  int oldpolicy = 0;
  int newpolicy = 0;
  int total = 0;
  while(getline(fin, min, '-')){
    getline(fin, max, ' ');
    getline(fin, target,':');
    getline(fin, code);
    ++total;
    code.erase(std::remove_if(code.begin(), code.end(), isspace), code.end());
    int counter = part1(code, target[0]);
    if(counter < std::stoi(min) || counter > std::stoi(max)) {
      ++oldpolicy;
    }

    if (part2(code, std::stoi(min), std::stoi(max), target[0])){
      ++newpolicy;
    }
  }
  cout << "[ Part 1 ]Number of valid passwords: " << total -oldpolicy << endl;
  cout << "[ Part 2 ] Valid passwords with new rule: " << newpolicy;
  return 0;
}
