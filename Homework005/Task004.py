line = 'ttt h jj ituee'
new_line = ''
for j in range(len(line)):
    counter = line.count(line[j])
    if line[j] not in new_line:
        new_line+=str(counter) + line[j]

print(new_line)



