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

def printMap(map): 
  global baseMap
  liner = ""
  for i in baseMap: 
    if i[0] % 10 == 0:
      print(liner)
      liner = ""
    liner = liner + i[1].strip()

def seatStatus(state, adjacent, status):
  """
  Parameter: tuple (position, 'L')
  """
  global numAisles
  global aisleLength
  global baseMap
  # Base case
  if adjacent == 0:
    return False
  # Seat in front 
  if state+(aisleLength*adjacent)<numAisles and \
    baseMap[state+(aisleLength*adjacent)][1]==status:
    return True
  # Seat behind
  if state-(aisleLength*adjacent) >= 0 and \
    baseMap[state-(aisleLength*adjacent)][1] == status:
    return True
  # Seat left 
  if state-adjacent >= 0 and baseMap[state-adjacent][1] == status:
    return True
  # Seat Right
  if state+ adjacent < aisleLength and baseMap[state+adjacent][1] ==status:
    return True
  # Seat diagnol: back right
  if state-aisleLength-adjacent >= 0 and \
    baseMap[state-aisleLength-adjacent][1] ==status:
    return True
  # Seat Diagnol: back left  
  if state- aisleLength + adjacent >= 0 and \
    baseMap[state-aisleLength+adjacent][1] ==status:
    return True
  # Seat Diagnol: front right
  if state+ aisleLength-adjacent< numAisles and \
    baseMap[state+ aisleLength-adjacent][1] ==status:
    return True
  # Seat Diagnol: front left
  if state+aisleLength+adjacent< numAisles and \
    baseMap[state+aisleLength+adjacent][1]==status:
    return True
  if status =='#':
    print("Recursing ... ")
    seatStatus(state, adjacent -1, status)
  return False

  
def applyRules():
  global baseMap
  updateMap = []
  changed = False
  for seat in baseMap: 
    # Floor: ignore
    if seat[1] == "L" and seatStatus(seat[0], 1, "L"):
      updateMap.append((seat[0],"#"))
      changed = True
    elif seat[1] == "#" and seatStatus(seat[0], 4, "#"): 
      updateMap.append((seat[0],"L"))
      changed = True
    else: 
      updateMap.append(seat)
  printMap(updateMap)
  baseMap = updateMap
  return changed
   
def main():
  filename = sys.argv[1]
  print("Reading in file ...")
  openFile(filename)
  print("Applying rules ...")
  while applyRules(): 
    print("Not stabilized")
  print("Stabilized!")
  

        


if __name__=="__main__":
  main()

