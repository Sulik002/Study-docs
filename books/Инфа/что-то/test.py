listok = []
for n in range(2024, 10**10, 2024):
    n = str(n)
    if n[0] == '1' and n[2:6] == '2157' and n[-1] == '4':
        listok.append(int(n))
listok = sorted(listok)
for i in range(len(listok)):
    print(str(listok[i]) + '|' + str(listok[i] // 2024))


