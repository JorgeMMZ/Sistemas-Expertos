# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:00:32 2024

@author: Ghost
"""

import pandas as pd

V = ('casa','san_jacinto','gdl_centro','plaza_patria','oxxo_PN','zapopan_centro','DQ_terranova','juarez','mezquitan','ceti','parada_51c')
grafoa = pd.DataFrame(index=V, columns=V)
grafoa.loc['casa', 'san_jacinto'] = 6
grafoa.loc['casa', 'parada_51c'] = 4
grafoa.loc['san_jacinto', 'gdl_centro'] = 8
grafoa.loc['san_jacinto', 'juarez'] = 10
grafoa.loc['san_jacinto', 'casa'] = 6
grafoa.loc['gdl_centro', 'san_jacinto'] = 8
grafoa.loc['gdl_centro', 'plaza_patria'] = 10
grafoa.loc['gdl_centro', 'zapopan_centro'] = 12
grafoa.loc['plaza_patria', 'gdl_centro'] = 10
grafoa.loc['plaza_patria', 'DQ_terranova'] = 15
grafoa.loc['plaza_patria', 'ceti'] = 25
grafoa.loc['DQ_terranova', 'ceti'] = 6
grafoa.loc['DQ_terranova', 'plaza_patria'] = 15
grafoa.loc['juarez', 'mezquitan'] = 6
grafoa.loc['juarez', 'san_jacinto'] = 10
grafoa.loc['mezquitan', 'juarez'] = 6
grafoa.loc['mezquitan', 'oxxo_PN'] = 30
grafoa.loc['oxxo_PN', 'ceti'] = 5
grafoa.loc['oxxo_PN', 'zapopan_centro'] = 20
grafoa.loc['oxxo_PN', 'mezquitan'] = 30
grafoa.loc['zapopan_centro', 'gdl_centro'] = 12
grafoa.loc['zapopan_centro', 'oxxo_PN'] = 20
grafoa.loc['DQ_terranova', 'ceti'] = 4
grafoa.loc['DQ_terranova', 'plaza_patria'] = 15
grafoa.loc['ceti', 'DQ_terranova'] = 4
grafoa.loc['ceti', 'oxxo_PN'] = 5
grafoa.loc['ceti', 'plaza_patria'] = 30
grafoa.loc['ceti', 'parada_51c'] = 100
grafoa.loc['parada_51c', 'ceti'] = 100
# grafoa = grafoa.fillna(0)  # Llenar los valores NaN con 0
# grafoa.to_json("grafoa.json",orient='split')

def Prof(grafoa, nodo_inicial):
    visitados = set()
    arbol_expansion = []

    def explorar(nodo, visitados, arbol_expansion):
        visitados.add(nodo)
        for vecino in grafoa.columns[(grafoa.loc[nodo] > 0)]:
            if vecino not in visitados:
                arbol_expansion.append((nodo, vecino))
                explorar(vecino, visitados, arbol_expansion)

    explorar(nodo_inicial, visitados, arbol_expansion)
    return arbol_expansion

arbol_expansion = Prof(grafoa, 'casa') # nodo principal, cambiar para que cumpla el algoritmo en cualquier nodo
print("Árbol de expansión por profundidad:", arbol_expansion)