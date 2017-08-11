def TMi(Loc):
    from Reus import MouAmb
    if MouAmb[1] >= 1 and MouAmb[2] >= 1 and MouAmb[3] == 4:
        TMi2(Loc)
    elif MouAmb[1] >= 1 and MouAmb[3] >= 2:
        TMi1(Loc)
    else:
        TMi0(Loc)


def TMi0(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] in ('F', 'M', 'D'):
        Resource[Loc] = 'Stone'
        World[1][Loc] = 0
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 8
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Marble'
        World[1][Loc] = 0
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 10
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 1
    else:
        print "Minerals cannot go here!"


def TMi1(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] in ('F', 'M', 'D'):
        Resource[Loc] = 'Stone'
        World[1][Loc] = 1
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 15
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Marble'
        World[1][Loc] = 1
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 15
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 2
    else:
        print "Minerals cannot go here!"


def TMi2(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc] in ('F', 'M', 'D'):
        Resource[Loc] = 'Stone'
        World[1][Loc] = 2
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 20
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 3
    elif TerrainType[Loc] == 'S':
        Resource[Loc] = 'Marble'
        World[1][Loc] = 0
        World[2][Loc] = 1
        Base[:, Loc] = 0
        Base[2][Loc] = 20
        NaturaBase[Loc] = 0
        Aspects[:, Loc] = 0
        Aspects[7][Loc] = 3
    else:
        print "Minerals cannot go here!"
