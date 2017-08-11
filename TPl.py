def TPl(Loc):
    from Reus import SwaAmb
    if SwaAmb[1]>=1 and SwaAmb[2]>=1 and SwaAmb[3]==4:
        TPl2(Loc)
    elif SwaAmb[1]>=1 and SwaAmb[3]>=2:
        TPl1(Loc)
    else:
        TPl0(Loc)

def TPl0(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='F':
        Resource[Loc]='Dandelion'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=5
        NaturaBase[Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Peppermint'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=7
        NaturaBase[Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Withered_Shrub'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        NaturaBase[Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Ginger'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=5
        NaturaBase[Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    else:
        print "Plants cannot grow here!"

def TPl1(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='F':
        Resource[Loc]='Dandelion'
        World[1][Loc]=1
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=10
        NaturaBase[Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Peppermint'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=12
        NaturaBase[Loc]=3
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Withered_Shrub'
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        NaturaBase[Loc]=5
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Ginger'
        World[1][Loc]=1
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=10
        NaturaBase[Loc]=6
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    else:
        print "Plants cannot grow here!"

def TPl2(Loc):
    from Reus import World, Aspects, Base, TerrainType, NaturaBase, Resource
    global World, Base, Aspects, NaturaBase, Resource
    if TerrainType[Loc]=='F':
        Resource[Loc]='Dandelion'
        World[1][Loc]=2
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=20
        NaturaBase[Loc]=8
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Peppermint'
        World[1][Loc]=2
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=24
        NaturaBase[Loc]=6
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Withered_Shrub'
        World[1][Loc]=2
        World[2][Loc]=0
        Base[:,Loc]=0
        NaturaBase[Loc]=10
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Ginger'
        World[1][Loc]=2
        World[2][Loc]=0
        Base[:,Loc]=0
        Base[2][Loc]=20
        NaturaBase[Loc]=12
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    else:
        print "Plants cannot grow here!"