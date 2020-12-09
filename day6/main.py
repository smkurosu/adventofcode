import sys 

def evalGroup(group:str):
  return len(set(group))

def parseFile(file: str) -> int:
  yes = 0
  with open(file) as reader:
    group = ""
    for line in reader:
      if line == "\n":
        yes = yes + evalGroup(group)
        group=""
      else:
        line = line.strip()
        group = group+line
    return yes + evalGroup(group)

def partTwo(filename: str):
  questions = {}
  numppl= 0
  answer = 0
  with open(filename) as reader:
    for line in reader:
      if line == "\n":
        answer = answer + yesses(questions, numppl)
        questions = {}
        numppl = 0
      else: 
        line = line.strip()
        for yes in line: 
          if yes in questions: 
            questions[yes] += 1
          else: 
            questions[yes] = 1
        numppl += 1
    answer = answer + (yesses(questions, numppl))

  print("[PART 2] Yes Number: ", answer)

def yesses(group, numppl) -> int: 
  unanimous = 0
  for key in group:
    if group[key] == numppl:
      unanimous +=1
  return unanimous

def main():
  filename = sys.argv[1]
  print("[PART 1] Yes Number: ", parseFile(filename))
  partTwo(sys.argv[1])


if __name__=="__main__":
  main()