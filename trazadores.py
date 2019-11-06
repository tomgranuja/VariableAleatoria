#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import itertools
import numpy as np
import pandas as pd
import random

def ruta_points(dirs=['d','d','r']):
    rotation = {
        'd': np.array([[0,1],[-1,0]]),
        'r': np.identity(2),
        'i': np.array([[0, -1],[1,0]])
    }
    d = np.array([[1,0]])
    r_keys = [d[0].lower() for d in dirs]
    for r in r_keys:
        new_d = rotation[r].dot(d[-1])
        d = np.vstack((d, new_d))
    return d.cumsum(axis=0)

def cuadras(dirs=['d','d','r']):
    xf = ruta_points(dirs)[-1]
    return int(np.abs(xf).sum())

def rutas(n=3, con_cuadras=False):
    assert isinstance(n, int), f'No se trata de un número entero: {n}'
    assert 0 <= n <= 11, f'Número {n} fuera de rango.'
    
    cases = ['derecha','recto','izquierda']
    #cases = ['D', 'R', 'I']
    cols = [f'esquina{i+1}' for i in range(n)]
    e=pd.DataFrame(list(itertools.product(cases, repeat=n)),columns=cols)
    if con_cuadras:
        e['cuadras'] = e.apply(cuadras, axis=1)
    return e

def por_cuadras(e):
    s = e.groupby(e.cuadras).size()
    r = pd.DataFrame(s, columns=['caminos posibles'])
    return r.reset_index(level=0)


if __name__ == '__main__':
    pass
