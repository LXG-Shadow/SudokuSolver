shudu = []
for i in range(0,9,1) :
    a = input()
    shudu = shudu + [[int(b) for b in a[0:17:2]]]

shudu1=shudu[:]

def gntptrow(shudu,r) :
    ptrow = []
    for i in range(1,10,1) :
        if i in shudu[r][:] :
            pass
        else :
            ptrow.append(i)
    return set(ptrow)

def gntptline(shudu,l) :
    ptline = [i for i in range(1,10,1)]
    for i in range(0,9,1) :
        if shudu[i][l] in ptline :
            ptline.remove(shudu[i][l])
    return set(ptline)

def add(shudu,r1,r2,l1,l2) :
    bck = [i for i in range(1,10,1)]
    for i in range(r1,r2) :
        for s in range(l1,l2) :
            if shudu[i][s] in bck :
                bck.remove(shudu[i][s])
    return bck

def gntptsqr(shudu,r,l) :
    #print(r,l)
    ptsqr = []
    if r >= 0 and r <= 2 :
        if l >= 0 and l <= 2 :
           ptsqr = add(shudu,0,3,0,3)
        elif l >= 3 and l<=5 :
           ptsqr = add(shudu,0,3,3,6)
        else :
            ptsqr = add(shudu,0,3,6,9)
    elif r >= 3 and r <= 5 :
        if l >= 0 and l <= 2 :
           ptsqr = add(shudu,3,6,0,3)
        elif l >= 3 and l<=5 :
           ptsqr = add(shudu,3,6,3,6)
        else :
            ptsqr = add(shudu,3,6,6,9)
    else :
        if l >= 0 and l <= 2 :
           ptsqr = add(shudu,6,9,0,3)
        elif l >= 3 and l<=5 :
           ptsqr = add(shudu,6,9,3,6)
        else :
            ptsqr = add(shudu,6,9,6,9)
    return set(ptsqr)

def solver(shudu,x,y) :
    if x > 8 :
        for i in range(0,9,1):
            print(shudu[i][:])
        print('')
        return
    elif y > 8 :
        solver(shudu, x+1, 0)
    else :
        if shudu[x][y] == 0 :
            pt = list(gntptline(shudu,y) & gntptrow(shudu,x) & gntptsqr(shudu,x,y))
            #print(x,y,shudu)
            if len(pt) != 0 :
                for i in pt :
                    shudu[x][y] = i
                    solver(shudu,x,y+1)
                    shudu[x][y] = 0
            else :
                return None
        else :
            solver(shudu,x,y+1)
    return 'Done'

print(solver(shudu,0,0))