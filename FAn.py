def FAn(Loc):
    from Reus import OceAmb
    if OceAmb[1]>=1 and OceAmb[3]==4:
        FAn2(Loc)
    elif OceAmb[1]>=1 and OceAmb[3]>=2:
        FAn1(Loc)
    else:
        FAn0(Loc)

def FAn0(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Chicken'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[0][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Frog'
        Range[Loc]=1
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[0][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Kangaroo_Rat'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=1
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Marten'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=1
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Mackarel'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=0
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=2
        Aspects[7][Loc]=1
    else:
        print "Animals cannot survive here!"

def FAn1(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Chicken'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=2
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Frog'
        Range[Loc]=1
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=2
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Kangaroo_Rat'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=2
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Marten'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=2
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Mackarel'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=4
        Aspects[7][Loc]=1
    else:
        print "Animals cannot survive here!"

def FAn2(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Chicken'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=4
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Frog'
        Range[Loc]=1
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=4
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Kangaroo_Rat'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=4
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Marten'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=4
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Mackarel'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Base[0][Loc]=8
        Aspects[7][Loc]=2
    else:
        print "Animals cannot survive here!"