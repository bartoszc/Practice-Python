with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

names_l = all_text.split('\n')
di = {}
for name in names_l:
    if name in di.keys():
        di[name] += 1
    else:
        di[name] = 1
print(di)

with open('Training_01.txt') as open_f:
    text = open_f.read()

counter_dict = {}
with open('Training_01.txt') as f:
    line = f.readline()
    while line:
        line = line[3:-26]
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

print(len(counter_dict))
