def lgnumfind(l):
    lgsofar = -99999999999999
    l = l.split()
    for y in l:
        y = int(y)
        if y > lgsofar:
            lgsofar = y
    #print("largest", lgsofar)
    return lgsofar
l = input("please enter numbers seprated by a space:")
x = lgnumfind(l)
print (x)
