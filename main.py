import os
import shutil
import sys
import simplekml
import math
from polycircles import polycircles

sys.path.insert(0, 'H:\Meu Drive\Python\Dev_FTTh\Objetos_Globais')

from ponto import Poste



postes=Poste.extrair_postes('Entrada/Postes.kmz')
maior = 0

kml = simplekml.Kml()

for c in postes:
    clientes = c.casa+c.comercio+c.predio
    if clientes > maior:
        maior = clientes

for c in postes:
    clientes = c.casa + c.comercio + c.predio
    opacidade = (clientes/maior)
    if clientes >0:
        polycircle = polycircles.Polycircle(latitude=c.coordenada[0],
                                            longitude=c.coordenada[1],
                                            radius=clientes*5,
                                            number_of_vertices=36)

        pol = kml.newpolygon(name=f"",outerboundaryis=polycircle.to_kml())
        pol.style.polystyle.color = "CC0000FF"
        pol.style.linestyle.width = 0
kml.save('Saída/mapa.kmz')




try:
    shutil.rmtree(f'{os.getcwd()}\TEMP')
except FileNotFoundError:
    pass
