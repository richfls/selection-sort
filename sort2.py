import random
randomlist = [random.randrange(50) for i in range(10)]
def seletionsort(rlist):
     for small in range(len(rlist)):
         for current in range(len(rlist)):
            if rlist[small] < rlist[current]:
                temp = rlist[small]
                rlist[small] = rlist[current]
                rlist[current] = temp
print(randomlist)
seletionsort(randomlist)
print(randomlist)
