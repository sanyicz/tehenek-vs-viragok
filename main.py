from random import *
from tkinter import *
from time import *
from rectangle_overlap import *
from classes import *

start = time()

n, nT, nV, nK = 100, 10, 10, 5 #mező mérete, tehenek, virágok és kerítések száma

foglalt = [(0,0)]*(nT+nV) #a már vmilyen objektum (tehén vagy virág) által elfoglalt helyek koordinátái
foglaltK = [(0,0,0,0)]*nK #a már meglévő kerítések koordinátái

#tehenek, virágok és kerítések elhelyezése
T = placeT(nT,n,foglalt)
V = placeV(nT,nV,n,foglalt)
K = placeK(nK,n,foglaltK)
#K = [Kerites(6, 40, 15, 82), Kerites(64, 6, 77, 59), Kerites(27, 15, 39, 23), Kerites(41, 25, 57, 51), Kerites(59, 62, 85, 74)] #5 kerítés 100x100-as mezőre

#megnézzük, melyik tehén hány virágot ér el
T_get_VK(T,V,K)

#futásidő számolása
print('%0.2f' % (time() - start))

#kirajzoltatás
ablak = Tk()
can = Canvas(ablak, width=4*n, height=4*n)
can.pack()
kirajzol(T,V,K,can)
