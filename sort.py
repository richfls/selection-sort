import random
sort = []
for j in range(0,30):
    sort.append(random.randrange(100,200))
print(sort)

def s():
    swap = 0
    for j in range(len(sort)):
        smol = sort[j]
        for i in range(len(sort)-j):
            if sort[i+j] < smol:
                smol = sort[i+j]
                swap = i+j

        temp = sort[j]
        sort[j] = smol
        sort[swap] = temp

    print(sort)
  
s()
