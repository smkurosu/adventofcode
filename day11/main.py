import sys
import copy

baseMap = []
aisleLen = 0
numAisles = 0

def openFile(file: str):
  global baseMap
  global aisleLen
  global numAisles
  with open(file) as reader: 
    location = 0
    for line in reader: 
      aisle = []
      numAisles += 1
      for pos in line.strip():
        aisle.append(pos)
        location += 1
      baseMap.append(aisle)
    aisleLen = int(location / numAisles)

  print("number of aisles: ",numAisles)
  print("Aisle length: ", aisleLen)
  # printMap(baseMap)

def printMap(map):
  counter = 0
  for i in map: 
    str1 = ""
    print(str1.join(i))
    counter += i.count("#")
  print("Number of occupied seats: ", counter, "\n")

def printResults(map):
  counter = 0
  for i in map: 
    counter += i.count("#")
  print("Number of occupied seats: ", counter, "\n")

def seatStatus(state, adj, status, row, col):
  """
  Parameter: tuple (position, 'L')
  """
  global numAisles
  global aisleLen
  global baseMap
  numOccupied = 0
  # Base case
  # if adj == 0:
  #   return False
  # Seat in front: 
  if (row+1)< numAisles and baseMap[row+1][col]==status:
    numOccupied += 1
  # Seat behind
  if (row-1) >= 0 and baseMap[row-1][col] == status:
    numOccupied += 1
  # Seat lft : check if it is a lft edge. If not, check diagnol
  if (col-1)>= 0 and baseMap[row][col-1] == status:
    numOccupied += 1
    # Seat diagnol: back lft
  if col-1 >= 0 and row-1 >= 0 and baseMap[row-1][col-1] ==status:
    numOccupied += 1
  # Seat Diagnol: front lft
  if row + 1 < numAisles and col -1 >= 0 and baseMap[row+1][col-1]==status:
    numOccupied +=1
  # Seat rgt: check if it is not a rgt edge
  if col+1<aisleLen and baseMap[row][col+1] ==status:
    numOccupied += 1
  # Seat Diagnol: back rgt  
  if row-1 >= 0 and col +1 <aisleLen and baseMap[row-1][col+1] ==status:
    numOccupied += 1
# Seat Diagnol: front rgt
  if row+1 < numAisles and col+1 < aisleLen and baseMap[row+1][col+1]==status:
    numOccupied += 1
  # if status =='#':
  #   print("Recursing ... ")
  #   seatStatus(state, adj -1, status)
  # print(baseMap[row][col], numOccupied)
  return numOccupied

  
def applyRules(p2: bool):
  global baseMap
  updateMap = []
  changed = False
  aisle, seat = 0,0
  while aisle < numAisles:
    mapper = []
    seat = 0
    while seat < aisleLen:
      # Floor: ignore
      if not p2 and baseMap[aisle][seat] == 'L' and seatStatus(seat, 1, "#", aisle, seat) == 0:
        mapper.append("#")
        changed = True
      elif p2 and baseMap[aisle][seat]=='#' and seatStatus(seat,1,"#",aisle,seat) >= 5: 
        mapper.append("L")
        changed = True
      elif not p2 and baseMap[aisle][seat]== '#' and seatStatus(seat, 1, "#", aisle, seat) >= 4: 
        mapper.append("L")
        changed = True
      else:
        mapper.append(baseMap[aisle][seat])
      seat += 1
    aisle += 1
    updateMap.append(mapper)
  # printMap(updateMap)
  baseMap = copy.deepcopy(updateMap)
  return changed
   
def main():
  global baseMap
  filename = sys.argv[1]
  part2 = False
  if sys.argv[2] == "part2": 
    print("Running part 2 ...")
    part2 = True
  else:
    print("Running part 1 ...")
  print("Filename: ", filename)
  openFile(filename)
  print("Applying rules ...")
  while applyRules(part2): 
    print("Not stabilized")
  print("Stabilized!")
  printResults(baseMap)

  

        


if __name__=="__main__":
  main()

