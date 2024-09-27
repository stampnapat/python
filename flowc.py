a = (input()).split()
l = [int(i) for i in a ]



if l[0] > l[1] :
    l[1] , l[0] = l[0] , l[1]
    if l[3] > l[1] :
        if l[2] > l[3] :
            l[2] -= l[0]
            l[3] = l[0] + l[1] + l[2]
            
    else :
        l[3] = l[0] + l[1] + l[2]
else :
    if l[0] >= l[1] and l[2] > l[0] :
        l[3] += l[0]
    else :
        if l[3] > l[2] :
            l[1] += 2
        else :
            l[1] *= 2

l = [str(i) for i in l]
print(' '.join(l))
