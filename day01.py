#DATA = 'data/day01/testdata'
DATA = 'data/day01/realdata'

### Read data in splitting each into a list inside a bigger list
### Sum over each list
### Find max value

f = open(DATA, 'r')

data = [ line.strip() for line in f]

calories = []
total = 0
for x in data:
    if x != '':
        total = total + int(x)
    else:
        calories.append(int(total))
        total = 0

print(max(calories))
calories.sort(reverse=True)

print(sum(calories[0:3]))

#######################################################################
print('OK to go!')
