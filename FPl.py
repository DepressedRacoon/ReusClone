def FPl(Loc):
    from Reus import ForAmb
    if ForAmb[0] >= 2 and ForAmb[3] == 4:
        FPl2(Loc)
    elif ForAmb[0] >= 1 and ForAmb[3] >= 2:
        FPl1(Loc)
    else:
        FPl0(Loc)


def FPl0(Loc):
    from Reus import World, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] == 'F':
        Resource[Loc] = 'Blueberry'
        World[1][Loc] = 0
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 5
        NaturaBase[Loc] = 1
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Elderberry'
        World[1][Loc] = 0
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 5
        NaturaBase[Loc] = 2
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    elif TerrainType[Loc] == 'D':
        Resource[Loc] = 'Withered_Shrub'
        World[1][Loc] = 0
        World[2][Loc] = 0
        Base[:, Loc] = 0
        NaturaBase[Loc] = 1
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    elif TerrainType[Loc] == 'M':
        Resource[Loc] = 'Kumquat'
        World[1][Loc] = 0
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 5
        NaturaBase[Loc] = 1
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    else:
        print "Plants cannot grow here!"


def FPl1(Loc):
    from Reus import World, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] == 'F':
        Resource[Loc] = 'Blueberry'
        World[1][Loc] = 1
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 10
        NaturaBase[Loc] = 1
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Elderberry'
        World[1][Loc] = 1
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 10
        NaturaBase[Loc] = 4
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    elif TerrainType[Loc] == 'D':
        Resource[Loc] = 'Withered_Shrub'
        World[1][Loc] = 1
        World[2][Loc] = 0
        Base[:, Loc] = 0
        NaturaBase[Loc] = 5
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    elif TerrainType[Loc] == 'M':
        Resource[Loc] = 'Kumquat'
        World[1][Loc] = 1
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 10
        NaturaBase[Loc] = 2
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    else:
        print "Plants cannot grow here!"


def FPl2(Loc):
    from Reus import World, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] == 'F':
        Resource[Loc] = 'Blueberry'
        World[1][Loc] = 2
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 20
        NaturaBase[Loc] = 2
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 3
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Elderberry'
        World[1][Loc] = 2
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 20
        NaturaBase[Loc] = 8
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 3
    elif TerrainType[Loc] == 'D':
        Resource[Loc] = 'Withered_Shrub'
        World[1][Loc] = 2
        World[2][Loc] = 0
        Base[:, Loc] = 0
        NaturaBase[Loc] = 10
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 3
    elif TerrainType[Loc] == 'M':
        Resource[Loc] = 'Kumquat'
        World[1][Loc] = 0
        World[2][Loc] = 0
        Base[:, Loc] = 0
        Base[0][Loc] = 20
        NaturaBase[Loc] = 4
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    else:
        print "Plants cannot grow here!"
