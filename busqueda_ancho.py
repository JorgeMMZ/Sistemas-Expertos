# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:05:25 2024

@author: Ghost
"""

import pandas as pd

V = ['casa','san_jacinto','gdl_centro','plaza_patria','oxxo_PN','zapopan_centro','DQ_terranova','juarez','mezquitan','ceti','parada_51c']
grafo = pd.DataFrame(index=V, columns=V)
grafo.loc['casa', 'san_jacinto'] = 6
grafo.loc['casa', 'parada_51c'] = 4
grafo.loc['san_jacinto', 'gdl_centro'] = 8
grafo.loc['san_jacinto', 'juarez'] = 10
grafo.loc['san_jacinto', 'casa'] = 6
grafo.loc['gdl_centro', 'san_jacinto'] = 8
grafo.loc['gdl_centro', 'plaza_patria'] = 10
grafo.loc['gdl_centro', 'zapopan_centro'] = 12
grafo.loc['plaza_patria', 'gdl_centro'] = 10
grafo.loc['plaza_patria', 'DQ_terranova'] = 15
grafo.loc['plaza_patria', 'ceti'] = 25
grafo.loc['DQ_terranova', 'ceti'] = 6
grafo.loc['DQ_terranova', 'plaza_patria'] = 15
grafo.loc['juarez', 'mezquitan'] = 6
grafo.loc['juarez', 'san_jacinto'] = 10
grafo.loc['mezquitan', 'juarez'] = 6
grafo.loc['mezquitan', 'oxxo_PN'] = 30
grafo.loc['oxxo_PN', 'ceti'] = 5
grafo.loc['oxxo_PN', 'zapopan_centro'] = 20
grafo.loc['oxxo_PN', 'mezquitan'] = 30
grafo.loc['zapopan_centro', 'gdl_centro'] = 12
grafo.loc['zapopan_centro', 'oxxo_PN'] = 20
grafo.loc['DQ_terranova', 'ceti'] = 4
grafo.loc['DQ_terranova', 'plaza_patria'] = 15
grafo.loc['ceti', 'DQ_terranova'] = 4
grafo.loc['ceti', 'oxxo_PN'] = 5
grafo.loc['ceti', 'plaza_patria'] = 30
grafo.loc['ceti', 'parada_51c'] = 100
grafo.loc['parada_51c', 'ceti'] = 100
#grafo=grafo.fillna(0)#llena nan con 0
grafo.to_json("grafo.json",orient='split')
#grafo.to_json('grafo.json') sale error con esta linea sabe porque
v1='casa' #este nodo se cambia para que de distinta Ep

S=[v1]
Vp=[v1]
Ep=[]
s=[]
d=V.copy()
d.remove(v1)
while True:
    for x in S:

        #escribir en consola: grafo['a']>0
        v=[y for y in d if y in grafo.loc[grafo[x]>0,x]]
        _=[(Ep.append((x,y)),Vp.append(y),d.remove(y),s.append(y)) for y in v]
        #escribir en consola: Ep , x
        
    if s==[]:
        break
    S=s.copy()
    s=[]
    
print("Árbol de expansión a lo ancho:", Ep)