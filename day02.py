#DATA = 'data/day02/testdata'
DATA = 'data/day02/realdata'


### I think there are only 9 combos:
### AX, AY, AZ, BX, BY, BZ, CX, CY, CZ
### So first of all I should have a dictionary of the values mayeb?

# AX = rock rocks        = 1 + 3 
# AY = paper rock        = 2 + 6
# AZ = scissors rock     = 3 + 0
# BX = rock paper        = 1 + 0
# BY = paper paper       = 2 + 3
# BZ = scissors paper    = 3 + 6
# CX = rock scissors     = 1 + 6
# CY = paper scissors    = 2 + 0
# CZ = scissors scissors = 3 + 3
outcomes = {
  "A X": 4,
  "A Y": 8,
  "A Z": 3,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 7,
  "C Y": 2,
  "C Z": 6,
}

# AX rock lose scissors
# AY rock draw rock
# AZ rock win
# BX paper lose
# BY paper draw paper
# BZ paper win
# CX scissors lose
# CY scissors draw scissors
# CZ scissors win


outcomes2 = {
  "A X": 3,
  "A Y": 4,
  "A Z": 8,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 2,
  "C Y": 6,
  "C Z": 7,
}

f = open(DATA, 'r')

data = [ line.strip() for line in f]

score = 0
score2 = 0
for line in data:
    if line in outcomes:
        print(line, outcomes[line])
        score = score + outcomes[line]
    else:
        print('Something is wrong')
for line in data:
    if line in outcomes2:
        print(line, outcomes2[line])
        score2 = score2 + outcomes2[line]
    else:
        print('Something is wrong')
print("Score is ", score)
print("Score2 is ", score2)
#######################################################################
print('OK to go!')
