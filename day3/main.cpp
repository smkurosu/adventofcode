#include <iostream>
#include <fstream> 
#include <string>

using std::getline;
using std::cout;
using std::endl;
using std::string;

int main(int argc, char *argv[]){
  if (argc < 2) {
    std::cerr << "Pass in test case." << endl; 
  }
  string filename = argv[1];
  cout << "Running against test: " << filename << endl;
  
  std::ifstream fin;
  fin.open(filename);
  if (!fin.is_open()){
    cout << "Error opening file\n";
    exit(0);
  }
  string map;
  int trees = 0;
  int place = 0;
  while(fin >> map){
    place = place % map.size();
    if (map[place] == '#') { 
      ++trees;
      map[place] = 'X';
    }
    else{
      map[place] = 'O';
    }
    cout << map << endl;
    place += 3;
    }
    cout << "Number of trees: " << trees << endl;
  return 0;
}