import sys
import re

def scanner(name: str):
  byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False
  valid = 0
  with open(name) as reader:
    for line in reader:
      if "\n" == line[0]:
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
          valid += 1
        byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False,False
      else:
        for i in line.split(' '): 
          param = i.split(':')[0]
          if param == "byr":
            byr = True
          elif param == "iyr":
            iyr = True
          elif param == "eyr":
            eyr = True
          elif param == "hgt":
            hgt = True
          elif param == "hcl":
            hcl = True
          elif param == "ecl":
            ecl = True
          elif param == "pid": 
            pid = True
  print("Valid passports:",valid)

def checkHairString(check: str) -> bool:
  pattern = r'[^\.a-f0-9]'
   #Other than a-f and 0-9
  if re.search(pattern, check):
      return False
  # Only a-f and 0-9
  else:
      return True



def betterScanner(filename: str):
  byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False
  eclList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  valid = 0
  with open(filename) as reader:
    for line in reader:
      if "\n" == line[0]:
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
          valid += 1
        byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False,False
      else:
        for i in line.split(' '):
          key = i.split(':')[0] 
          val = i.split(':')[1].strip()
          if key == "byr" and len(val) == 4 and int(val)>=1920 and int(val)<=2002:
            # print(key, " ", val)
            byr = True
          elif key == "iyr" and  len(val) == 4 and int(val)<=2020 and int(val) >= 2010:
            iyr = True
          elif key == "eyr" and  len(val) == 4 and int(val) <= 2030 and int(val) >= 2020:
            eyr = True
          elif key == "hgt":
            if val[-2:] == "cm":
              if int(val[:-2]) <= 193 and int(val[:-2]) >= 150:
                hgt= True
            elif val[-2:] == "in":
              if int(val[:-2]) <= 76 and int(val[:-2]) >= 59:
                hgt = True
          elif key == "hcl" and val[0] == '#' and len(val[1:]) == 6:
              if checkHairString(val[1:]):
                hcl = True
          elif key == "ecl" and val in eclList:
            ecl = True
          elif key == "pid" and val.isnumeric() and len(val) == 9:
            pid = True
  print("[PART 2] Valid Passport: ", valid)
           
            
def main():
  # Run [python3] [main.py] [filename.txt] [part1/part2]
  if sys.argv[2] == "part1":
    scanner(sys.argv[1])
  else:
    betterScanner(sys.argv[1])


  

if __name__=="__main__":
  main()