def Oce(Loc):
    from Reus import OCEAN, OCEANDEPTH, Terrain, PaintTerrain
    from Variables import Length
    import numpy
    Chk = 0
    for a in OCEAN:  # Check if there's an mountain within range, switches to Demountainer if there is
        if Loc+a >= Length:
            L = Loc+a-Length
        else:
            L = Loc+a
        if Terrain[0][L] == 1:
            Chk = 1
    if Chk == 0:  # Oceaner
        i = 0
        while i < len(OCEAN):
            if Loc+OCEAN[i] >= Length:
                L = Loc+OCEAN[i]-Length
            else:
                L = Loc+OCEAN[i]
            Terrain[0][L] = -1
            PaintTerrain[2][2*L] = min(OCEANDEPTH[i], PaintTerrain[2][2*L]-PaintTerrain[1][2*L])+PaintTerrain[1][2*L]
            i += 1
    if Chk == 1:  # DeMountainer
        i = 0
        while i < len(OCEAN):
            if Loc+OCEAN[i] >= Length:
                L = Loc+OCEAN[i]-Length
            else:
                L = Loc+OCEAN[i]
            Terrain[0][L] = 0
            PaintTerrain[2][2*L] = PaintTerrain[1][2*L]
            PaintTerrain[2][2*L-1] = PaintTerrain[1][2*L-1]
            PaintTerrain[2][2*L+1] = PaintTerrain[1][2*L+1]
            i = i+1
    i = 0
    while i < len(OCEAN):
        if Loc+OCEAN[i]+10 > Length:
            DF = 2*(Loc+OCEAN[i]-Length)
        else:
            DF = 2*(Loc+OCEAN[i])
        MeanAbove = [PaintTerrain[2][DF+2]-PaintTerrain[1][DF+2], PaintTerrain[2][DF]-PaintTerrain[1][DF]]  # smooths terrain
        PaintTerrain[2][DF+1] = numpy.mean(MeanAbove)+PaintTerrain[1][DF+1]
        MeanBelow = [PaintTerrain[2][DF-2]-PaintTerrain[1][DF-2], PaintTerrain[2][DF]-PaintTerrain[1][DF]]
        PaintTerrain[2][DF-1] = numpy.mean(MeanBelow)+PaintTerrain[1][DF-1]
        if Terrain[0][Loc+OCEAN[i]+1] == 1:
            PaintTerrain[2][DF+1] = PaintTerrain[1][DF+1]
        if Terrain[0][Loc+OCEAN[i]-1] == 1:
            PaintTerrain[2][DF-1] = PaintTerrain[1][DF-1]
        i += 1


def Mou(Loc):
    from Reus import MOUNT, MOUNTAINHEIGHT, Terrain, PaintTerrain
    from Variables import Length
    import numpy
    Chk = 0
    for a in MOUNT:  # Check if there's an ocean within range, switches to DeOceaner if there is
        if Loc+a >= Length:
            L = Loc+a-Length
        else:
            L = Loc+a
        if Terrain[0][L] == -1:
            Chk = 1
    if Chk == 0:  # Mountaner
        i = 0
        while i < len(MOUNT):
            if Loc+MOUNT[i] >= Length:
                L = Loc+MOUNT[i]-Length
            else:
                L = Loc+MOUNT[i]
            Terrain[0][L] = 1
            if Terrain[1][L] != -1:  # If was not previously set to be swamp becomes forest
                Terrain[1][L] = 1
            PaintTerrain[2][2*L] = max(MOUNTAINHEIGHT[i], PaintTerrain[2][2*L]-PaintTerrain[1][2*L])+PaintTerrain[1][2*L]
            i += 1
    elif Chk == 1:  # DeOceaner
        i = 0
        while i < len(MOUNT):
            if Loc+MOUNT[i] >= Length:
                L = Loc+MOUNT[i]-Length
            else:
                L = Loc+MOUNT[i]
            Terrain[0][L] = 0
            PaintTerrain[2][2*L] = PaintTerrain[1][2*L]
            PaintTerrain[2][2*L-1] = PaintTerrain[1][2*L-1]
            PaintTerrain[2][2*L+1] = PaintTerrain[1][2*L+1]
            i += 1
    i = 0
    while i < len(MOUNT):
        if Loc+MOUNT[i]+10 > Length:
            DF = 2*(Loc+MOUNT[i]-Length)
        else:
            DF = 2*(Loc+MOUNT[i])
        MeanAbove = [PaintTerrain[2][DF+2]-PaintTerrain[1][DF+2], PaintTerrain[2][DF]-PaintTerrain[1][DF]]  # Smooths
        PaintTerrain[2][DF+1] = numpy.mean(MeanAbove)+PaintTerrain[1][DF+1]
        MeanBelow = [PaintTerrain[2][DF-2]-PaintTerrain[1][DF-2], PaintTerrain[2][DF]-PaintTerrain[1][DF]]
        PaintTerrain[2][DF-1] = numpy.mean(MeanBelow)+PaintTerrain[1][DF-1]
        if Terrain[0][Loc+MOUNT[i]+1] == -1:
            PaintTerrain[2][DF+1] = PaintTerrain[1][DF+1]
        if Terrain[0][Loc+MOUNT[i]-1] == -1:
            PaintTerrain[2][DF-1] = PaintTerrain[1][DF-1]
        i += 1


def For(Loc):
    from Reus import TERRAINW, Terrain
    from Variables import Length
    for a in TERRAINW:
        if Loc+a >= Length:
            L = Loc+a-Length
        else:
            L = Loc+a
        if Terrain[2][L] == 1 and Terrain[0][L] == 0:
            Terrain[1][L] = 1


def Swa(Loc):
    from Reus import TERRAINW, Terrain
    from Variables import Length
    for a in TERRAINW:
        if Loc+a >= Length:
            L = Loc+a-Length
        else:
            L = Loc+a
        if Terrain[2][L] == 1 and Terrain[0][L] == 0:
            Terrain[1][L] = -1
