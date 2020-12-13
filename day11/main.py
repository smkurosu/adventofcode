import sys

baseMap = []
aisleLength = 0
numAisles = 0

def openFile(file: str):
  global baseMap
  global aisleLength
  global numAisles
  with open(file) as reader: 
    location = 0

    for line in reader: 
      numAisles += 1
      for pos in line.strip():
        baseMap.append((location, pos))
        location += 1
    aisleLength = int(location / numAisles)

  print(numAisles)
  print(aisleLength)
  print(baseMap)

def emptySeat(state):
  """
  Parameter: tuple (position, 'L')
  """
  global numAisles
  global aisleLength
  global baseMap
  # Seat in front 
  if state + aisleLength < numAisles and baseMap[state + aisleLength][1] == "L":
    return True
  # Seat behind
  if state - aisleLength >= 0 and baseMap[state - aisleLength][1] == "L":
    return True
  # Seat left 
  if state- 1 >= 0 and baseMap[state-1][1] == "L":
    return True
  # Seat Right
  if state+ 1 < aisleLength and baseMap[state+ 1][1] == "L":
    return True
  # Seat diagnol: back right
  if state- aisleLength - 1 >= 0 and baseMap[state-aisleLength-1][1] == "L":
    return True
  # Seat Diagnol: back left  
  if state- aisleLength + 1 >= 0 and baseMap[state-aisleLength+1][1] == "L":
    return True
  # Seat Diagnol: front right
  if state+ aisleLength - 1 < numAisles and baseMap[state+aisleLength-1][1] == "L":
    return True
  # Seat Diagnol: front left
  if state+ aisleLength + 1 < numAisles and baseMap[state+aisleLength+1][1] == "L":
    return True
  return False

def occupiedSeat(): 
  global baseMap
  global numAisles
  global aisleLength

  
def applyRules():
  global baseMap
  updateMap = []
  for seat in baseMap: 
    # Floor: ignore
    if seat[1] == "L" and emptySeat(seat[0]):
      updateMap.append((seat[0],"#"))
    elif seat[1] == "#" and occupiedSeat(seat[0]): 
      updateMap.append((seat[0],"L"))
    else: 
      updateMap.append(seat)
  print(updateMap)
   
def main():
  
  filename = sys.argv[1]
  print("Reading in file ...")
  openFile(filename)
  print("Applying rules ...")
  applyRules()
  

        


if __name__=="__main__":
  main()

