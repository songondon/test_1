'''честно: я в душе не знаю от какой задачи этот простенький код
но нашел и переписал его с вацапа, где он был отправлен с едким коментарием адрессату, попросившему у меня списать, адрессат по совместительству умнейший олимпиадник из тех что знаю'''
for i in range(int(input())):
    l = []
    a = 10**15
    ans = 0
    n = int(input())
    for k in list(map(int,input().split())):
        ans += 1
        a = min(a,k)
        if a >= ans:
            continue
        l.append(ans-1)
        ans = 1
        a = k
    l.append(ans)
    print(len(l))
    print(*l)
