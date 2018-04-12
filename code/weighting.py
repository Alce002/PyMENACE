import random
import math


def sigm(x, N):
    y=1/(1+math.e**(-0.1*x+math.log(N-1)))  #-0.2 scaling, 2=N-1 where N is number of available moves
    return y


def invertsigm(y, N):
    try:
        x=-10*(math.log(1-y)-math.log(y)-math.log(N-1))  #See earlier comment, -5* corresponds to division by -0.2, scaling factor
        return x
    except Exception:
        print(N, y)
        raise(Exception)


def PickMove(position):
    if len(position) == 1:
        return position[0][0]
    l=[]
    print(position)
    for n in range(len(position)):
        l.append(sigm(position[n][1],len(position)))
    k=random.random()

    a1=1
    a2=1

    counter=0
    for n in l:

        a2-=n
        print(a1, k, a2)
        if a1>=k>a2:
            print(l)
            return position[counter][0]
        a1=a2
        counter+=1
    return -1, l


def WeightAdj(index,tup,wl,posList):
    if len(posList[index]) == 1:
        return
    testList=list(posList[index])
    X=0
    O=0
    tomove=0
    for n in index:
        if n=='X':
            X+=1
        elif n=='O':
            O+=1
    if X==O:
        tomove='X'
    else:
        tomove='O'
    for n in range(len(testList)):
            if tup in testList[n]:
                movenum=n
                break
    oldW=testList[movenum][1]
    if wl!=1:
        if wl==tomove:
            if sigm(testList[movenum][1],len(testList))<0.9999999:
                testList[movenum][1]+=1

        else:
            if sigm(testList[movenum][1],len(testList))>0.0000001:
                testList[movenum][1]-=1
        if len(testList) > 1:
            fract=(1-sigm(testList[movenum][1],len(testList))/(1-sigm(oldW,len(posList[index]))))
            for n in range(len(testList)):
                if tup in testList[n]:
                    pass
                else:
                    y=sigm(testList[n][1],len(testList))


                    testList[n][1]=invertsigm(y*fract,len(testList))
        sumtest=0
        for n in testList:
            sumtest+=sigm(n[1], len(testList))
        if abs(1-sumtest)<0.0000000001:
            posList[index]=testList


if __name__ == '__main__':
    posExamp=[[(1,1),0],[(2,0),0],[(1,2),0]]
    posList=[posExamp]
    count0=0
    count1=0
    count2=0
    for n in range (100):
        a=PickMove(posExamp)
        if a==0:
            count0+=1
        if a==1:
            count1+=1
        if a==2:
            count2+=1
    print(count0,count1,count2)
    a=2,0
    print(posExamp)
    for _ in range(20):
        WeightAdj(0,a,0,posList)
    print(posExamp)
    count0=0
    count1=0
    count2=0
    for n in range (100):
        a=PickMove(posExamp)
        if a==0:
            count0+=1
        if a==1:
            count1+=1
        if a==2:
            count2+=1
    print(count0,count1,count2)
