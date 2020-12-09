import sys
import copy

def partOne(cmd: str, val: int, direction: str, acc: int, location: int):
  """
  Returns accumulator and location
  """
  if cmd == "acc":
    if direction == "+":
      acc += val
      location += 1
      return acc, location
    else: 
      acc -= val
      location +=1
      return acc, location
  elif cmd == "nop":
    location +=1
    return acc, location
  elif cmd == "jmp":
    if direction == "+":
      location += val
      return acc, location
    else: 
      location -= val
      return acc, location

def main(): 
  part1 = False
  part2 = False
  file = open(sys.argv[1], mode='r')
  if sys.argv[2] == "part2":
    part2 = True
  else: 
    part1 = True
  rules = file.readlines()
  location = 0
  acc = 0 
  testingChange = False
  tracker = [False]*len(rules)
  cpytracker = [False]*len(rules)
  cpylocation = 0
  revert = True

  while not tracker[location]:
    if len(rules) -1 == location: 
      break
    rule = rules[location]
    rule.strip()
    cmd = rule[0:3]
    direction = rule[4]
    val = int(rule[5:])
    tracker[location] = True
    if part2:
      if (cmd == "nop" or cmd == "jmp") and not testingChange and not revert:
        cpytracker = copy.deepcopy(tracker)
        cpylocation = location
        cpyacc = acc
        if cmd == "nop":
          print("Changing to jmp!")
          cmd = "jmp"
        elif cmd == "jmp":
          cmd = "nop"
          print("Changing to nop!")
        testingChange = True
        acc, location = partOne(cmd, val, direction, acc, location)
      # if reverted back
      else:
        revert = False
        # update next location
        acc, location = partOne(cmd, val, direction, acc, location)

    if tracker[location] and part2:
      print("About to fail ... reverting")
      tracker = copy.deepcopy(cpytracker)
      location = cpylocation
      acc = cpyacc
      testingChange = False
      tracker[location]=False
      revert = True
    if part1:
      acc, location = partOne(cmd, val, direction, acc, location)
  print("Accumulator: ", acc)


  file.close()


if __name__=="__main__":
  main()
