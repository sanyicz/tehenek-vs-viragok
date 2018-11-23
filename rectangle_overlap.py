def atlap(rectA, rectB):
    '''megnézi, hogy A és B téglalapok átlapolódnak-e
    a téglalapokat bal felső és jobb alsó csúcsuk x,y koordinátájával kell megadni'''
    A, B = [], [] #a téglalapok rácspontjainak halmaza
    for i in range(rectA[0],rectA[2]+1):
        for j in range(rectA[1],rectA[3]+1):
            A.append((i,j))
    for i in range(rectB[0],rectB[2]+1):
        for j in range(rectB[1],rectB[3]+1):
            B.append((i,j))

    #átlapolódás vizsgálata
    atlap = False #alapból nincs átfedés
    for i in A:
        if i in B:
            atlap = True #ha egy pont is közös, van átfedés
    return atlap

if __name__=='__main__':
    #két téglalap definiálása
    #bal felső és jobb alsó csúcsuk x,y koordinátájával
    rectA = [1,1,5,4]
    rectB = [5,4,9,5]
    #átfedést vizsgáló függvény hívása
    print(atlap(rectA,rectB))
