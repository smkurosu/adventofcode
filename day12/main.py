import sys 

def readFile(file):
  NS= 0
  EW = 0
  x = 1
  with open(file) as reader: 
    for direction in reader:
      direction.strip()
      compass = direction[0]
      miles = int(direction[1:])
      if compass == "N":
        NS += miles 
      elif compass == "E":
        EW += miles
      elif compass == "S":
        NS -= miles
      elif compass == "W":
        EW -= miles
      elif compass == "F":
        if x == 0:
          NS += miles
        elif x == 1: 
          EW += miles
        elif x == 2: 
          NS -= miles
        else: 
          EW -= miles
      else: 
        x = switchDirection(miles, compass, x)
  print("Manhattan distance: ", abs(NS)+abs(EW))    

def switchDirection(angle, side, y) -> int:

  if side == "L":
    return (y-int(angle/90))%4
  else:
    return (y+int(angle/90))%4

  
  
def main():
  file = sys.argv[1]  
  readFile(file)

if __name__=="__main__":
  main()
  