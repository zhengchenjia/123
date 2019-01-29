'''values = []
l = []

for i in range(len(values)):
    if i == 0:
        l = l.append(value[0])
    else:
        for ii in range(len(l)):
            if value[i] < l[ii]:
                l[ii+1] = l[ii]
            else:
                l[ii+1] = value[i]
                break'''

values = [80,70,50,69,78,90,100,65,88,70]

l = [80]
def insert(value):
    for i in range(1,len(values)):
        temp = value[i]
        position = i

        for j in range(i-1,-1,-1)
            if value[j] > temp:
                value[j+1] = value[j]
                pos = j
            else:
                pos = j+1

                break
    value[pos]=temp
def quick(value):
    if len(value) < 2:
        return value
    mark = value[0]
    small = [x for x in value if x < mark]
    equal = [x for x in value if x = mark]
    big = [x for x in value if x > mark]
    return quick(small) + equal + quick(big)




    

















