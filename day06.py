#DATA = 'data/day06/testdata'
DATA = 'data/day06/realdata'

f = open(DATA, 'r')

data = [ line.strip() for line in f]

transmission = data[0]
signal_size  = len(transmission)

for x in range(3,signal_size):
    packet = [transmission[x-3],transmission[x-2],transmission[x-1],transmission[x]]
    if (len(packet) == len(set(packet))):
        print('This one', packet, x+1)
        break

for x in range(13,signal_size):
    packet = [transmission[x-13],transmission[x-12],transmission[x-11],transmission[x-10],
              transmission[x- 9],transmission[x- 8],transmission[x- 7],transmission[x- 6],
              transmission[x- 5],transmission[x- 4],transmission[x- 3],transmission[x- 2],
              transmission[x- 1],transmission[x]
    ]
    if (len(packet) == len(set(packet))):
        print('This other one', packet, x+1)
        break
#######################################################################
print('OK to go!')
