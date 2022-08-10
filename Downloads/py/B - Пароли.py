'''заранее заданы критерии безопасности паролей
даны n-ое количество паролей
в зависимости от подходящий критерий, задать для каждого пароля свою буквы'''

#r = open('input.txt')
#w = open('output.txt','w')
l1 = list('QWERTYUIOPASDFGHJKLZXCVBNM')
l2 = list('qwertyuiopasdfghjklzxcvbnm')
l3 = list('1234567890')
#for i in range(int(r.readline())):
for i in range(int(input())):#
    #l = list(r.readline())
    ans = [0,0,0,0]
    s = input()
    l = list(s)
    for i in l:
        if i in l1:
            ans[0] = 1
        elif i in l3:
            ans[2] = 1
        elif i in l2:
            ans[1] = 1
        else:
            ans[3] = -100
            break
    ln = len(l)
    sm = sum(ans)
    if ln > 12 and sm == 3:
        q = 'H'
    elif ln > 8 and sm >= 2:
        q = 'M'
    elif ln > 4 and sm >= 1:
        q = 'W'
    else:
        q = 'I'
    #w.write(q)
    print(q)#