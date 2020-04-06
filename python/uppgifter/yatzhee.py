import random



def roll():
  number = []
  dices = range(5)
  for n in dices:
    dice = random.randrange(1, 7)
    number.append(dice)
  print(number)
  return number

def pair():
  pair = roll()

  is_pair = []
  for number in myList:
    if number in seen:
        print("repeat")
    else:
        seen.append(number)
  return n




if __name__ == "__main__":
    roll()




