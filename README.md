# ReusClone
Repository for my recreation of Reus in Python

Wiki for Reus Game http://wiki.reusgame.com
All creative credits to Abbey Games, this is purely a personal project to see if I 'can'.

Differently from Reus Proper, this is intended to be turn based; each Giant acts in turn (or is skipped) 
Ocean>Forest>Mountain>Swamp

Reus.py is script that is originally run, pulling variables from Variables.py to create the world.
When entering the loop that is the run-time game, Giants exercise functions from either TerrainFunctions or TPl etc.

TerrainFunctions allow for changing of the terrain. World originally starts off as flat (Terrain[0][N]=0), Non-Hydrated (Terrain[2][N]=0) and un-biomed (Terrain[1][N]=0) and therefore all "Unhydrated Wasteland" (TerrainType[N]='U').
Unhydrated Wasteland that is Hydrated becomes Hydrated Wasteland, which can then become Swamp or Forest. Dehydrated Swamp or Forest become Desert (Desert is set by changing Unhydrated Wasteland to Forest as the default behaviour of hydrating Desert makes it into Forest). Unhydrated Wasteland cannot be turned into Forest or Swamp directly, only by hydrating Desert. Oceans (Terrain[0][N]=-1) create hydration for Water(Default 4)+Oceanwidth tiles eo either side of them, unless they hit a mountain, Moutains (Terrain[0][N]=1) cause Deserts or Forests to form for Desert(Default 14) tiles to either side of them, again stopping if they hit an ocean.

Placing an ocean where there is a mount instead removes the mountain for a range, as does vice versa.

SweepsChecks enables checking for Hydration, Natura, Animal resources placed on tiles, Terrain Type (for plotting, with PaintTerrain and HalfTheta allowing for plotting in-between points to allow continuous lines) and Total count of resources on a tile, necessary for when villages claim tiles.

T(ech)Pl(ants), M(oney)Mi(nerals), F(ood)An(imals) and equivalents ought to place resources on appropriate tiles, or announce that the resource cannot be placed on that tile.



