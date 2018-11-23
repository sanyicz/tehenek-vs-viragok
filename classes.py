from random import *
from tkinter import *
from time import *
from rectangle_overlap import *

class Tehen:
    '''a teheneket két koordináta, 'T' betű + sorszám és az elérhető virágok száma jellemzi'''
    def __init__(self, x, y, c=1, v=0): #a teheneket két koordináta, 'T' betű + sorszám és az elérhető virágok száma jellemzi
        self.x, self.y = x, y
        self.c = 'T' + str(c)
        self.v = v
    def kiir(self): #kiírja az adott tehén adatait
        print(self.c, ' helye: ', self.x, ', ', self.y, sep='')
    def rajzol(self, can):
        can.create_oval(4*self.x-2, 4*self.y-2, 4*self.x+2, 4*self.y+2, fill='white')

class Virag:
    '''a virágokat két koordináta és a 'V' betű + sorszám jellemzi'''
    def __init__(self, x, y, c=1): #a virágokat két koordináta és a 'V' betű + sorszám jellemzi
        self.x, self.y = x, y
        self.c = 'V' + str(c)
    def kiir(self): #kiírja az adott virág adatait
        print(self.c, ' helye: ', self.x, ', ', self.y, sep='')
    def rajzol(self, can):
        can.create_oval(4*self.x-2, 4*self.y-2, 4*self.x+2, 4*self.y+2, fill='yellow')

class Kerites:
    '''a kerítéseket kétszer két koordináta (bal felső és jobb alsó csúcs) és a 'K' betű + sorszám jellemzi'''
    def __init__(self, x1, y1, x2, y2, c=1): #a kerítéseket kétszer két koordináta (bal felső és jobb alsó csúcs) és a 'K' betű + sorszám jellemzi
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.c = 'K' + str(c)
    def kiir(self): #kiírja az adott kerítés adatait
        print(self.c, ' helye: ', (self.x1, self.y1), ', ', (self.x2, self.y2), sep='')
    def rajzol(self, can):
        can.create_rectangle(4*self.x1-2, 4*self.y1-2, 4*self.x2+2, 4*self.y2+2, width=2)

def placeT(nT,n,foglalt):
    '''nT db tehenet helyez el n*n-es mezőn véletlenszeűen'''
    T = []
    for i in range(nT): #nT db tehenet kell véletlenszerűen elhelyezni, de nem lehet egy helyen kettő
        while 1:
            Ti = Tehen(randrange(1,n+1),randrange(1,n+1),i+1)
            if (Ti.x, Ti.y) not in foglalt:
                foglalt[i] = (Ti.x, Ti.y)
                T.append(Ti)
                T[i].kiir()
                break
    return T

def placeV(nT,nV,n,foglalt):
    '''nV db virágot helyez el n*n-es mezőn véletlenszeűen'''
    V = []
    for i in range(nV): #nV db virágot kell véletlenszerűen elhelyezni, de nem lehet egy helyen több virág vagy több tehén
        while 1:
            Vi = Virag(randrange(1,n+1),randrange(1,n+1),i+1)
            if (Vi.x, Vi.y) not in foglalt:
                foglalt[nT+i] = (Vi.x, Vi.y)
                V.append(Vi)
                V[i].kiir()
                break
    return V

def placeK(nK,n,foglaltK):
    '''nK db kerítést helyez el n*n-es mezőn véletlenszeűen'''
    K = []
    for i in range(nK): #nK db kerítést kell véletlenszerűen elhelyezni, de sehogy nem érintkezhetnek
        while 1:
            Ki = Kerites(randrange(1,n+1),randrange(1,n+1),randrange(1,n+1),randrange(1,n+1),i+1) #sehogy nem érintkezhetnek
            Ker = (Ki.x1, Ki.y1, Ki.x2, Ki.y2)
            overlap = False
            if Ki.x1<Ki.x2 and Ki.y1<Ki.y2:
                for j in foglaltK:
                    if atlap(Ker,j) == True:
                        overlap = True
                #print(overlap)
                if overlap == False:
                    foglaltK[i] = Ker
                    K.append(Ki)
                    K[i].kiir()
                    break
    return K

def TVK(T,V,K):
    '''megnézi, hogy adott virát adott tehén általi elérhetőségét akadályozza-e legalább egy kerítés'''
    eler = False
    if T.x<=V.x and T.y<=V.y:
        if T.x>=K.x1 and T.y>=K.y1 and V.x<=K.x2 and V.y<=K.y2: #ha T és V egy kerítésen belül vannak
            #print(T.c, K.c, 'miatt', 'eléri', V.c)
            eler = True
        elif T.y<K.y1 and V.x>K.x2: #ha T a kerítés mellett menve eléri V-t
            #print(T.c, K.c, 'miatt', 'eléri', V.c)
            eler = True
        elif T.x<K.x1 and V.y>K.y2: #ha T a kerítés mellett menve eléri V-t
            #print(T.c, K.c, 'miatt', 'eléri', V.c)
            eler = True
        elif (T.x<K.x1 and V.x<K.x1) or (T.x>K.x2 and V.x>K.x2): #ha T és V a kerítés ugyanazon oldalán vannak x irányban
            #print(T.c, K.c, 'miatt', 'eléri', V.c)
            eler = True
        elif (T.y<K.y1 and V.y<K.y1) or (T.y>K.y2 and V.y>K.y2): #ha T és V a kerítés ugyanazon oldalán vannak y irányban
            #print(T.c, K.c, 'miatt', 'eléri', V.c)
            eler = True
        else:
            #print(T.c, K.c, 'miatt', 'nem éri el', V.c)
            eler = False
    else:
        #print(T.c, 'nem érheti el', V.c)
        eler = False
    return eler #ha eléri a virágot, adja vissza, h eléri, a True-kat számoljuk majd össze

def T_get_VK(T,V,K):
    '''minden tehén-virág párra megnézni, hogy akadályozza-e az elérést akár csak egy kerítés is'''
    TgetV = [0]*len(T)
    for i in range(len(T)):
        for j in range(len(V)):
            TV = []
            for k in range(len(K)):
                TV.append(TVK(T[i], V[j], K[k]))
            #print(TV)
            if not False in TV:
                TgetV[i] += 1
    print(TgetV)

def kirajzol(T,V,K,can):
    '''kirajzol minden tehenet, virágot és kerítést'''
    for t in T:
        t.rajzol(can)
    for v in V:
        v.rajzol(can)
    for k in K:
        k.rajzol(can)
