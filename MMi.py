def MMi(Loc):
    from Reus import MouAmb
    if MouAmb[2]>=2 and MouAmb[3]==4:
        MMi2(Loc)
    elif MouAmb[2]>=1 and MouAmb[3]>=2:
        MMi1(Loc)
    else:
        MMi0(Loc)

def MMi0(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='D':
        Resource[Loc]='Quartz'
        World[1][Loc]=0
        World[2][Loc]=1
        Base[:,Loc]=0
        Base[1][Loc]=10
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc] in ('S','F','M'):
        Resource[Loc]='Agate'
        World[1][Loc]=0
        World[2][Loc]=1
        Base[:,Loc]=0
        Base[1][Loc]=8
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    else:
        print "Minerals cannot go here!"

def MMi1(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='D':
        Resource[Loc]='Quartz'
        World[1][Loc]=1
        World[2][Loc]=1
        Base[:,Loc]=0
        Base[1][Loc]=15
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc] in ('S','F','M'):
        Resource[Loc]='Agate'
        World[1][Loc]=1
        World[2][Loc]=1
        Base[:,Loc]=0
        Base[1][Loc]=15
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    else:
        print "Minerals cannot go here!"

def MMi2(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='D':
        Resource[Loc]='Quartz'
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        Base[1][Loc]=20
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc] in ('S','F','M'):
        Resource[Loc]='Agate'
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        Base[1][Loc]=20
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    else:
        print "Minerals cannot go here!"