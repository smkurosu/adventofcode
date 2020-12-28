import math 
import sys

def upper(val:int):
  return math.ceil(val/2)

def lower(val: int):
  return math.floor(val/2)

def calcSeatId(line, row, col):
  if line[6] == "F":
    if line[9] == "L":
      return row[0]*8+col[0]
    else:
      return row[0]*8+col[1]
  else: 
    if line[9] == "L":
      return row[1]*8+col[0]
    else:
      return row[1]*8+col[1]

 
def readFile(file):
  highestSeatID= 0
  with open(file) as reader: 
    for line in reader:
      row = (0,127)
      col = (0,7)
      line.strip()
      for seat in line:
        if seat == "F":
          row = (row[0], lower(row[0]+row[1]))
        elif seat == "B":
          row = (upper(row[0]+row[1]), row[1])
        elif seat == "L":
          col = (col[0], lower(col[0]+col[1]))
        else:
          col = (upper(col[0]+col[1]), col[1])

      if calcSeatId(line,row,col) > highestSeatID: 
        highestSeatID = calcSeatId(line,row,col)
  print("Highest seat ID: ",highestSeatID)

def main():
  filename = sys.argv[1]
  readFile(filename)

if __name__=="__main__":
  main()
      
      
          

