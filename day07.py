#DATA = 'data/day07/testdata'
DATA = 'data/day07/realdata'

f = open(DATA, 'r')

data = list(line.strip() for line in f)
data.reverse()

### Functions I need:
### check if first char is $, else ignore
### sum of int of the first bit
### check if string is command or dir/file
### Eventual outcome: dict = {dirname: total size}

def get_file_size(my_string):
    file_properties = my_string.split(' ')
    file_size = int(file_properties[0])
    return file_size

def find_line_type(my_string):
    line_type = 'file'
    if (my_string[0] == "$"):
        line_type = 'command'
    elif (my_string[0] == 'd'):
        line_type = 'directory'
    return line_type

def get_dir_size(my_dict, my_string):
    dir_properties = my_string.split(' ')
    dir_size = my_dict[dir_properties[1]]
    return dir_size

def add_directory_size(dir_dict, my_string, dir_size):
    #### input: dictionary, string, current_size
    #### return dictionary, current_size   
    dir_properties = my_string.split(' ')
    if (my_string == '$ ls'):
        pass
    elif (my_string == '$ cd ..'):
        pass
    else:
        dir_dict[dir_properties[-1]] = dir_size
        dir_size = 0

    return dir_dict, dir_size

directory_sizes = {}
dir_size = 0
for line in data:
    line_type = find_line_type(line)
    if (line_type == 'file'):
        dir_size = dir_size + get_file_size(line)
    elif (line_type == 'directory'):
        dir_size = dir_size + get_dir_size(directory_sizes, line)
        #print(line, dir_size)
    elif (line_type == 'command'):
        directory_sizes, dir_size = add_directory_size(directory_sizes, line, dir_size)
    else:
        print('Error, wrong type detected')

count = 0
for key in directory_sizes:
    print(key, directory_sizes[key])
    if directory_sizes[key] < 1000000:
        count = count + directory_sizes[key]

print('Answer is:', count)



#######################################################################
print('OK to go!')
