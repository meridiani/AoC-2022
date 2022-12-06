import sys
#DATA1 = 'data/day05/cheattestdata1'
#DATA2 = 'data/day05/cheattestdata2'
DATA1 = 'data/day05/cheatrealdata1'
DATA2 = 'data/day05/cheatrealdata2'
#DATA = 'data/day05/realdata'

f1 = open(DATA1, 'r')
crates = [ line.strip().replace('[','').replace(']','').replace(',','') for line in f1]

f2 = open(DATA2, 'r')
instructions = [ line.replace('move','').replace('from','').replace('to','').strip().split('  ') for line in f2]

number_of_crates = len(crates)

stacks ={}
for x in range(1, number_of_crates + 1):
    stacks[str(x)] = crates[x-1]

### We have the data as follows:
#{1: 'ZN', 2: 'MCD', 3: 'P'}
# move from to
#[['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']]
#######################################################################
###
### Now...
### We need to iterate over the instructions
### 

def move_crates_9000(move_amount, from_stack, to_stack):
    for x in range(-1,(-1-move_amount),-1):
        to_stack = to_stack + from_stack[x]
    from_stack = from_stack[:-(move_amount)]
    
    return from_stack, to_stack


def move_crates_9001(move_amount, from_stack, to_stack):
    to_stack   = to_stack + from_stack[-(move_amount):]
    from_stack = from_stack[:-(move_amount)]
    
    return from_stack, to_stack

for x in instructions:
#    print(stacks)
#    print('move', x[0], 'Stack 1', stacks[x[1]], 'Stack 2', stacks[x[2]])
    # take the two specified stacks and swaps the contents
    stacks[x[1]], stacks[x[2]] = move_crates_9001(int(x[0]), stacks[x[1]], stacks[x[2]])
#    print(stacks)

#######################################################################
answer = ''
for key in stacks:
    answer = answer + stacks[key][-1]

print('Answer is: ', answer)

#######################################################################
print('OK to go!')
#DATA = 'data/day05/testdata'
#
#f = open(DATA, 'r')
#
#data = ''
#for line in f:
#    data = data + line
#
#data = data.split('\n\n')
#crates = data[0].
#
#print(data[0])
#
#sys.exit()

