l = []
int1 = l.append(int(input('')))
int2 = l.append(int(input('')))
int3 = l.append(int(input('')))
int4 = l.append(int(input('')))
int5 = l.append(int(input('')))
# l.sort()


for i in range(len(l)) :
    for j in range(0,(len(l))-1-i) :
        if l[j] < l[j+1] :
            l[j] , l[j+1] = l[j] , l[j+1]
print(l[2])
