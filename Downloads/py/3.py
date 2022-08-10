'''придираясь к формулировке 3его задания:
l = [1]
l.sort
/\
||
массив любового размера.числа в массиве можно хоть 10**18 раз менять местами, но результат не ухудшится.массив отсортирован.а в скорости ему будет устпупать многие виды быстрых сортировок'''
# но на всякий случай оставлю еще сортировку Хоара, уступающую по производительности предыдущей...
def sort(l, frst, lst):
    if frst >= lst:
        return
    i = frst
    j = lst
    while i <= j:
        x = l[(i + j) // 2]
        while l[i]  < x: i += 1
        while l[j]  > x: j -= 1
        if i <= j: 
            l[i],l[j] = l[j], l[i]
            i += 1;j -= 1 
    sort(l,frst,j)
    sort(l,i,lst)    
l = [10, 98, 78, 4, 54, 25, 84, 41, 30, 87, 60, 84, 6, 12]
sort(l,0,len(l)-1)
print(l)
'''
class qsort(object):
    def __init__(self,l,frst,lst):
        self.l = l;self.fsrt = frst;self.lst = lst
    def qsort(self):
        if frst >= lst:
            return
        i = frst
        j = lst
        while i <= j:
            x = l[(i + j) // 2]
            while l[i]  < x: i += 1
            while l[j]  > x: j -= 1
            if i <= j: 
                l[i],l[j] = l[j], l[i]
                i += 1;j -= 1 
        self.qsort(l,frst,j)
        self.qsort(l,i,lst)'''