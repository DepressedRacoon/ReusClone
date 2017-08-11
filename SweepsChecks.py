def NaturaCheck(Loc):
    from Reus import World, Natura, Resource
    from Variables import Length
    global NaturaHere
    R = 2
    if Resource[Loc] == 'Gingko' or (Resource[Loc] == 'Tea Plant' and ((World[1][Loc] == 1 and Natura[Loc] >= 25) or (World[1][Loc] == 0 and Natura[Loc] >= 15))):
        R = 3
    L = range(-R, R+1)
    for a in L:
        if a+L > Length:
            DF = a+L-Length
        else:
            DF = a+L
        if Natura[DF] < NaturaHere:
            Natura[DF] = NaturaHere


def NaturaSweep():
    from Reus import NaturaBase, Aspects, Sym
    from Variables import Length
    H = 0
    Natura = [0]*Length
    while H < Length:
        NaturaHere = NaturaBase[H]+Aspects[5][H]+Sym[6][H]
        NaturaCheck(H)
        H = H+1
    return Natura


def HydroCheck(Loc):  # Work out hydration of every tile by looping world twice in each direction
    from Variables import Water, Desert
    from Reus import Terrain
    global Watercheck, Waterfier, Desertifier, Bump
    if Terrain[0][Loc] == 1:
        Desertifier = Desert
        Waterfier = 0
        if Terrain[1][Loc] != -1:
            Terrain[1][Loc] = 1
    elif Terrain[0][Loc] == -1:
        Desertifier = 0
        if Bump == 1:
            Waterfier = 0
        Waterfier += 1
        Watercheck = 0
        Bump = -1
    else:
        if Watercheck < Waterfier+Water and Waterfier > 0:
            Terrain[2][Loc] = 1
            Watercheck += 1
        elif Desertifier > 0:
            if Terrain[1][Loc] != -1:
                Terrain[1][Loc] = 1
            Desertifier -= 1
        Bump = 1


def HydroSweep():
    from Variables import Length
    from Reus import Terrain
    global Watercheck, Waterfier, Desertifier, Bump
    i = 0
    while i < Length:  # Dries world out to check if any tiles have become unhydrated
        Terrain[2][i] = 0
        i = i+1
    i = 0
    K = (2*Length)-1
    Desertifier = 0
    Waterfier = 0
    Watercheck = 0
    Bump = 0
    while i < Length:
        HydroCheck(i)
        i = i+1
    while i < K:
        HydroCheck(i-Length)
        i = i+1
    i = -1
    Desertifier = 0
    Waterfier = 0
    Watercheck = 0
    Bump = 0
    while i >= -Length:
        HydroCheck(i)
        i -= 1
    while i > -K:
        HydroCheck(i+Length)
        i -= 1
    return Terrain


def TerrainSweep():
    from Variables import Length
    import numpy
    WHERE = numpy.zeros((7, Length*2))
    H = 0
    while H < Length:
        TerrainCheck(H)
        H += 1
    HERE = numpy.append(WHERE, WHERE[:, 0])
    return HERE


def TerrainCheck(Loc):
    from Reus import TerrainType, Terrain
    global WHERE
    if Terrain[0][Loc] == 1:
        TerrainType[Loc] = 'M'
        WHERE[0][2*Loc-1] = WHERE[0][2*Loc] = WHERE[0][2*Loc+1] = 1
    elif Terrain[0][Loc] == -1:
        TerrainType[Loc] = 'O'
        WHERE[1][2*Loc-1] = WHERE[1][2*Loc] = WHERE[1][2*Loc+1] = 1
    else:
        if Terrain[2][Loc] == 0:
            if Terrain[1][Loc] != 0:
                TerrainType[Loc] = 'D'
                WHERE[2][2*Loc-1] = WHERE[2][2*Loc] = WHERE[2][2*Loc+1] = 1
            else:
                TerrainType[Loc] = 'U'
                WHERE[3][2*Loc-1] = WHERE[3][2*Loc] = WHERE[3][2*Loc+1] = 1
        else:
            if Terrain[1][Loc] == -1:
                TerrainType[Loc] = 'S'
                WHERE[4][2*Loc-1] = WHERE[4][2*Loc] = WHERE[4][2*Loc+1] = 1
            elif Terrain[1][Loc] == 1:
                TerrainType[Loc] = 'F'
                WHERE[5][2*Loc-1] = WHERE[5][2*Loc] = WHERE[5][2*Loc+1] = 1
            else:
                TerrainType[Loc] = 'H'
                WHERE[6][2*Loc-1] = WHERE[6][2*Loc] = WHERE[6][2*Loc+1] = 1


def AnimalCheck(Loc):
    from Reus import World, Range, Base, Sym, Aspects
    from Variables import Length
    global Animal
    if World[2][Loc] == 2:
        R = range(-Range[Loc], Range[Loc]+1)
        R.remove(0)
        for a in R:
            if a+Loc >= Length:
                DF = a+Loc-Length
            else:
                DF = a+Loc
            Animal[0][DF] += Base[0][Loc] + Sym[0][Loc] + Aspects[0][Loc]  # f
            Animal[1][DF] += Base[1][Loc] + Sym[1][Loc] + Aspects[1][Loc]  # w
            Animal[2][DF] += Base[2][Loc] + Sym[2][Loc] + Aspects[2][Loc]  # t
            Animal[3][DF] += Base[3][Loc] + Sym[3][Loc]                    # a
            Animal[4][DF] += Base[4][Loc] + Sym[4][Loc] + Aspects[4][Loc]  # d


def AnimalSweep():
    import numpy
    from Variables import Length
    Animal = numpy.zeros((5, Length))
    H = 0
    while H < Length:
        AnimalCheck(H)
        H = H+1
    return Animal


def ResourceCheck(Loc):
    from Reus import Total, Base, Animal, Sym, Aspect
    Total[0] = Base[0][Loc]+Animal[0][Loc]+Sym[0][Loc]+Aspect[0][Loc]
    Total[1] = Base[1][Loc]+Animal[1][Loc]+Sym[1][Loc]+Aspect[1][Loc]
    Total[2] = Base[2][Loc]+Animal[2][Loc]+Sym[2][Loc]+Aspect[2][Loc]
    Total[3] = Base[3][Loc]+Animal[3][Loc]+Sym[3][Loc]+Aspect[3][Loc]
    Total[4] = Base[4][Loc]+Animal[4][Loc]+Sym[4][Loc]+Aspect[4][Loc]


def ResourceSweep():
    import numpy
    from Variables import Length
    H = 0
    Total = numpy.zeros((5, Length))
    while H < Length:
        ResourceCheck(H)
        H += 1
    return Total
