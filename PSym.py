def Blueberry(Loc):
    global World, Sym
    if World[0][Loc+1] in ('Apple Tree', 'Dandelion', 'Strawberry') or World[0][Loc-1] in ('Apple Tree', 'Dandelion', 'Strawberry'):
        if World[1][Loc]==2:
            Sym[0][Loc]=40
        elif World[1][Loc]==1:
            Sym[0][Loc]=20
        else:
            Sym[0][Loc]=10
    else:
        Sym[0][Loc]=0
                
def Elderberry(Loc):
    global World, Sym
    if World[2][Loc+1]==2 or World[2][Loc-1]==2:
        if World[1][Loc]==2:
            Sym[0][Loc]=30
            Sym[5][Loc]=12
        elif World[1][Loc]==1:
            Sym[0][Loc]=15
            Sym[5][Loc]=6
        else:
            Sym[0][Loc]=7
            Sym[5][Loc]=3
    else:
        Sym[0][Loc]=Sym[5][Loc]=0
        
def Withered_Shrub(Loc):
    global World, Sym
    if World[2][Loc+1]==1 or World[2][Loc-1]==1:
        if World[1][Loc]==2:
            Sym[5][Loc]=18
        elif World[1][Loc]==1:
            Sym[5][Loc]=9
        else:
            Sym[5][Loc]=5
    else:
        Sym[5][Loc]=0
    
def Kumquat(Loc):
    global World, Sym
    if World[2][Loc+1]==0 or World[2][Loc-1]==0:
        if World[1][Loc]==2:
            Sym[0][Loc]=20
            Sym[3][Loc]=14
        elif World[1][Loc]==1:
            Sym[0][Loc]=10
            Sym[3][Loc]=7
        else:
            Sym[0][Loc]=8
            Sym[3][Loc]=3
    else:
        Sym[0][Loc]=Sym[3][Loc]=0

def Dandelion(Loc):
    global World, Sym
    if World[2][Loc+1]==0 or World[2][Loc-1]==0:
        if World[1][Loc]==2:
            Sym[2][Loc]=28
            Sym[5][Loc]=16
        elif World[1][Loc]==1:
            Sym[2][Loc]=16
            Sym[5][Loc]=8
        else:
            Sym[2][Loc]=8
            Sym[5][Loc]=4
    else:
        Sym[2][Loc]=Sym[5][Loc]=0
        
def Peppermint(Loc):
    global World, Sym
    if World[2][Loc+1]==1 and World[2][Loc-1]==1:
        if World[1][Loc]==2:
            Sym[2][Loc]=56
        elif World[1][Loc]==1:
            Sym[2][Loc]=28
        else:
            Sym[2][Loc]=14
    elif Worl[2][Loc+1]==1 or World[2][Loc-1]==1:
        if World[1][Loc]==2:
            Sym[2][Loc]=28
        elif World[1][Loc]==1:
            Sym[2][Loc]=14
        else:
            Sym[2][Loc]=7
    else:
        Sym[2][Loc]=0
        
def Ginger(Loc):
    global World, Sym
    if World[2][Loc+1]==2 or World[2][Loc-1]==2:
        if World[1][Loc]==2:
            Sym[2][Loc]=40
            Sym[5][Loc]=16
        elif World[1][Loc]==1:
            Sym[2][Loc]=20
            Sym[5][Loc]=9
        else:
            Sym[2][Loc]=10
            Sym[5][Loc]=5
    else:
        Sym[2][Loc]=Sym[5][Loc]=0