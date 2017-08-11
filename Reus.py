import numpy, random, math, matplotlib.pyplot as plt
from Variables import Length, Turns, OCEANWIDTH, MOUNTAINWIDTH, TERRAINWIDTH, SHOW_WORLD_BETWEEN_GIANTS, SL

'''print "The world is young and empty, fill it with the help of the four giants:"
print "The Ocean Giant moves first and can hydrate land by placing oceans- it can also place animals that will satiate the hunger of your people."
print "The Forest Giant moves next, it can grow forests on hydrated land and place nourishing fruit trees."
print "Next comes the Mountain Giant, which can raise mountains to form rain shadows in which deserts grow. It can also place two kinds of minerals."
print "Finally comes the Swamp Giant, which can cause swamps on hydrated land and let loose both herbs and exotic animals."
print "Unlike Reus this game is turn-based- you have",Turns,"turns for now! Tell each giant what to do with a 3 letter code and a location, the world is",Length,"tiles around."
print "To begin with all natural sources are available, as well as the Leaf Aspect (adds Tech and Natura to Plants) and the Growth Aspect (which only adds Food to Plants)."
print "When villages settle, they will try to build a project- this provides powerful bonuses but is also a challenge! 1st level projects last 5 turns, 2nd 10, 3rd 15, 4th 20."
print "Greed growth occurs when in a turn a village grows by more than 20+Awe (unlike in Reus the growth all occurs at the end of a turn ie. all at once)."
print "Enough danger will stop greed growth, but too much danger will either destroy a natural source causing Danger or destroy the village! Enough greed will cause wars and even revolts against the Giants!"'''

'''Set up world'''
Theta=numpy.arange(0,math.pi*2,math.pi*2/Length) #For mapping resources
HalfTheta=numpy.arange(0,math.pi*2,math.pi/Length) #For drawing world

World=numpy.zeros((3,Length))
Terrain=numpy.zeros((3,Length))
TerrainType=['U']*Length
Resource=['Empty']*Length
WHERE=numpy.zeros((7,2*Length)) #For choosing where to paint terrain
PaintTerrain=numpy.zeros((3,2*Length)) #Height map; random noise[0], smoothed noise base [1], base+adjustments [2]
Sym=numpy.zeros((7,Length)) #Food, Wealth, Tech, Awe, Danger, Natura, Range
Natura=NaturaBase=NaturaHere=Range=[0]*Length
Total=Base=numpy.zeros((5,Length)) #F,W,T,A,D
Aspects=numpy.zeros((8,Length)) #Food, Wealth, Tech, Awe,Danger, Natura, Allowed, Have
Animal=numpy.zeros((5,Length)) #Food, Wealth, Tech, Awe, Danger,

RANDCORE=[]
RED=[]
YELLOW=[]
WHITE=[]
RandTwist=int(random.uniform(0,math.pi/4.0))*-1**(int(random.uniform(0,Length/4.0)))
RandTurn=int(random.uniform(0,math.pi/4.0))*-1**(int(random.uniform(0,Length/4.0)))
i=0
while i<2*Length:
    RANDCORE.append(Length*random.uniform(0.6,0.7)/15.0)
    i=i+1


i=0
while i<2*Length: #Gen random noise
    PaintTerrain[0][i]=Length/10.0+(random.uniform(-1,1)*Length/250.0)
    i=i+1

i=0 #smoothed base terrain lumps
while i<2*Length:
    if i+1==2*Length:
        j=-1
    elif i+2==2*Length:
        j=-2
    else:
        j=i
    PaintTerrain[1][i]=PaintTerrain[2][i]=(PaintTerrain[0][j-2]+PaintTerrain[0][j-1]+PaintTerrain[0][j]+PaintTerrain[0][j+1]+PaintTerrain[0][j+2])/5.0
    '''RED.append((RANDCORE[j-2]+RANDCORE[j-1]+RANDCORE[j]+RANDCORE[j+1]+RANDCORE[j+2])/5.0)
    if i+RandTurn+10>=Length:
        j=i-Length+RandTurn
    else:
        j=i+RandTurn
    if i+RandTwist+10>=Length:
        k=i-Length+RandTwist
    else:
        k=i+RandTwist
    YELLOW.append((random.uniform(0.6,0.7)*(RANDCORE[j-2]+RANDCORE[j-1]+RANDCORE[j]+RANDCORE[j+1]+RANDCORE[j+2])/5.0))
    WHITE.append((random.uniform(0.6,0.7)*(random.uniform(0.6,0.7)*(RANDCORE[k-2]+RANDCORE[k-1]+RANDCORE[k]+RANDCORE[k+1]+RANDCORE[k+2])/5.0)))'''
    i=i+1

#RED.append(RED[0])
#YELLOW.append(YELLOW[0])
#WHITE.append(WHITE[0])


OCEAND=range(1,OCEANWIDTH+1) #Create shape profile for Ocean, Desert, Terrain
OCEAND.append(OCEANWIDTH)
OCEANTEST=range(OCEANWIDTH,0,-1)
for a in OCEANTEST:
    OCEAND.append(a)
OCEANDEPTH=[]
for a in OCEAND:
    OCEANDEPTH.append(-1.2+1.0/a)
OCEAN=range(-OCEANWIDTH,OCEANWIDTH+1)

MOUNTAINH=range(1,MOUNTAINWIDTH+1)
MOUNTAINH.append(MOUNTAINWIDTH+1)
MOUNTAINTEST=range(MOUNTAINWIDTH,0,-1)
for a in MOUNTAINTEST:
    MOUNTAINH.append(a)
MOUNTAINHEIGHT=[]
for a in MOUNTAINH:
    MOUNTAINHEIGHT.append(a*Length/(50.0*(MOUNTAINWIDTH+1.0)))
MOUNT=range(-MOUNTAINWIDTH,MOUNTAINWIDTH+1)

TERRAINW=range(0,TERRAINWIDTH+1)
TERRAINH=range(-TERRAINWIDTH,0)
for a in TERRAINH:
    TERRAINW.append(a)



'''GIANT ABILITY FUNCTIONS'''



OceAbiGui=['Ocean/DeMountain = 1','Domestic Animals = 2', 'Growth Aspect (P) = 3', 'LOCKED (A)', 'LOCKED (M)','SKIP = 0'] #GUI guides
ForAbiGui=['Forest = 1','Fruit Plants = 2', 'Leaf Aspect (P) = 3', 'LOCKED (P)', 'LOCKED (A)','SKIP =0']
MouAbiGui=['Mountain/DeOcean = 1','Precious Minerals = 2', 'Advanced Minerals = 3', 'LOCKED (A)', 'LOCKED (M)', 'LOCKED (M)','SKIP = 0']
SwaAbiGui=['Swamp = 1','Herbs = 2', 'Exotic Animals = 3', 'LOCKED (P)', 'LOCKED (A)', 'LOCKED (M)','SKIP = 0']


OceAmb=[0,0,0,0] #F,S,D, Sum
ForAmb=[0,0,0,0]
MouAmb=[0,0,0,0]
SwaAmb=[0,0,0,0]

'''TERRAIN FUNCTIONS'''



'''SOURCE FUNCTIONS'''



''' ASPECT FUNCTIONS '''
'''
def GrAs():
def HeAs():
def CrAs():

def LeAs():                   TO BE ADDED
def FrAs():
def HuAs():

def ExAs():
def NoAs():
def SeAs():

def ToAs():
def PrAs():
def ReAs():   '''








''' GAME RUN FUNCTION '''


OceAbi=['Ter.Oce','FAn.FAn'] #Lookup tables for abilities
ForAbi=['Ter.For','FPl.FPl']
MouAbi=['Ter.Mou','MMi.MMi','TMi.TMi']
SwaAbi=['Ter.Swa','TPl.TPl','MAn.MAn']

randturn=random.random()
Q=-1**int(randturn*4)

def PLOT():
    global randturn
    ax=plt.subplot(projection='polar')
    plt.xticks([])
    plt.yticks([])
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),0,color='#996633')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0])+SL/2.0,where=numpy.append(WHERE[5],WHERE[5][0]),color='#21a615')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0])+SL/2.0,where=numpy.append(WHERE[4],WHERE[4][0]),color='#72ab6d')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0])+SL/2.0,where=numpy.append(WHERE[2],WHERE[2][0]),color='#cfc53e')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0])+SL/2.0,where=numpy.append(WHERE[6],WHERE[6][0]),color='#91abd8')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0])+SL/2.0,where=numpy.append(WHERE[3],WHERE[3][0]),color='#8a95a8')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),numpy.append(PaintTerrain[1],PaintTerrain[1][0]),where=numpy.append(WHERE[0],WHERE[0][0]),color='#807f7e')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0]),numpy.append(PaintTerrain[2],PaintTerrain[2][0]),Length/10.0-SL,where=numpy.append(WHERE[1],WHERE[1][0]),color='#213fed')
    '''ax.fill_between(numpy.append(HalfTheta,HalfTheta[0])+randturn,RED,0,color='r')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0])+randturn,YELLOW,0,color='y')
    ax.fill_between(numpy.append(HalfTheta,HalfTheta[0])+randturn,WHITE,0,color='w')'''
    plt.show()
    randturn+=Q*(random.uniform(0,1)*math.pi)

import Terrainfunctions as Ter
import FAn, FPl, MAn, MMi, TPl, TMi
import SweepsChecks as SC


SC.TerrainSweep()
N=0
while N<Turns:
    PLOT()
    print "What should the Ocean Giant do?",OceAbiGui
    OceTask=int(input())
    if OceTask!=0:
        print "Where?"
        OceLoc=int(input())
        eval(OceAbi[OceTask-1])(OceLoc)
        SC.HydroSweep()
        SC.TerrainSweep()
        if SHOW_WORLD_BETWEEN_GIANTS==1:
            PLOT()
    print "What should the Forest Giant do?",ForAbiGui
    ForTask=int(input())
    if ForTask!=0:
        print "Where?"
        ForLoc=int(input())
        eval(ForAbi[ForTask-1])(ForLoc)
        SC.TerrainSweep()
        if SHOW_WORLD_BETWEEN_GIANTS==1:
            PLOT()
    print "What should the Mountain Giant do?",MouAbiGui
    MouTask=int(input())
    if MouTask!=0:
        print "Where?"
        MouLoc=int(input())
        eval(MouAbi[MouTask-1])(MouLoc)
        SC.HydroSweep()
        SC.TerrainSweep()
        if SHOW_WORLD_BETWEEN_GIANTS==1:
            PLOT()
    print "What should the Swamp Giant do?",SwaAbiGui
    SwaTask=int(input())
    if SwaTask!=0:
        print "Where?"
        SwaLoc=int(input())
        eval(SwaAbi[SwaTask-1])(SwaLoc)
        SC.TerrainSweep()
        if SHOW_WORLD_BETWEEN_GIANTS==1:
            PLOT()
    N+=1
