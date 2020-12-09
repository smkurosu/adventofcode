import sys

def partOne(file: str):
  location = 0
  acc = 0 
  file = open(file, mode='r')
  rules = file.readlines()
  print(rules)
  tracker = [False] * len(rules) 
  while not tracker[location]:
    rule = rules[location]
    rule.strip()
    cmd = rule[0:3]
    direction = rule[4]
    val = int(rule[5:])
    print(cmd, direction, val)
    tracker[location] = True
    if cmd == "acc":
      if direction == "+":
        acc += val
        location += 1
      else: 
        acc -= val
        location += 1
    elif cmd == "nop":
      location += 1
    elif cmd == "jmp":
      if direction == "+":
        location += val
      else: 
        location -= val
  file.close()
  print("[Part 1] Accumulator: ", acc)
  
def main(): 
  partOne(sys.argv[1])


if __name__=="__main__":
  main()
