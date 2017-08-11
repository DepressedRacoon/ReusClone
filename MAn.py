def MAn(Loc):
    from Reus import SwaAmb
    if SwaAmb[2]>=1 and SwaAmb[1]>=1 and SwaAmb[3]==4:
        MAn2(Loc)
    elif SwaAmb[2]>=1 and SwaAmb[3]>=2:
        MAn1(Loc)
    else:
        MAn0(Loc)

def MAn0(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Stoat'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Poison_Dart_Frog'
        Range[Loc]=1
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Desert_Tortoise'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Monal'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=1
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Clownfish'
        Range[Loc]=2
        World[1][Loc]=0
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=1
    else:
        print "Animals cannot survive here!"

def MAn1(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Stoat'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        Base[1][Loc]=2
        NaturaBase[Loc]=0
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Poison_Dart_Frog'
        Range[Loc]=1
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Desert_Tortoise'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Monal'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=2
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Clownfish'
        Range[Loc]=2
        World[1][Loc]=1
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=2
    else:
        print "Animals cannot survive here!"

def MAn2(Loc):
    from Reus import World, Range, Aspects, Base, TerrainType, Resource, NaturaBase
    global World, Range, Base, Aspects, Resource, NaturaBase
    if TerrainType[Loc]=='F':
        Resource[Loc]='Stoat'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='S':
        Resource[Loc]='Poison_Dart_Frog'
        Range[Loc]=1
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='D':
        Resource[Loc]='Desert_Tortoise'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='M':
        Resource[Loc]='Monal'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=4
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    elif TerrainType[Loc]=='O':
        Resource[Loc]='Clownfish'
        Range[Loc]=2
        World[1][Loc]=2
        World[2][Loc]=2
        Base[:,Loc]=0
        NaturaBase[Loc]=0
        Base[1][Loc]=8
        Aspects[:,Loc]=0
        Aspects[7][Loc]=3
    else:
        print "Animals cannot survive here!"