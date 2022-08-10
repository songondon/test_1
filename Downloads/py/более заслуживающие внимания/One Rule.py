'''классификатор, реализующий алгоритм one rule
не читаемо, но работает'''
n, n2 = map(int,input().split())
k = list(map(str,input().split()))
d = [dict() for i in range(n2)]
for i in range(n):
    l = list(map(str,input().split()))
    for i in range(n2):
        if l[i] not in d[i]:
            d[i][l[i]] = [0,0]
        d[i][l[i]][int(l[-1])] += 1
acc = []
d2 = d
for d in d2:
    l = list(d.values())
    yy, nn, yn,ny = 0, 0,0,0
    for i in l:
        if max(i) == i[1]:
            yy += i[1]
            yn += i[0]
        else:
            ny += i[1]
            nn += i[0]
    acc.append((yy+nn)/(yy+yn+ nn+ ny))
z = k.index(k[acc.index(max(acc))])
for i in range(int(input())):
    l = list(map(str,input().split()))
    if max(d2[z][l[z]]) == d2[z][l[z]][1]:
        print(1)
    else:
        print(0)
    # а говорил что не смогу, женя