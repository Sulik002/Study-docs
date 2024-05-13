f = open("22.txt")
time = {}

for i in f:
    line = i.split()
    if line[2] == '0':
        time[line[0]] = int(line[1])
    else: continue
f.close()

f = open("22.txt")
for i in f:
    line = i.split()
    if line[2] == '0':
        continue
    else:
        zav = []
        timezav = []
        if len(line) == 4:
            timezav.append(time[line[3]])
        timezav.append(time[line[2]])

        time[line[0]] = max(timezav) + int(line[1])
print(max(time.values()))