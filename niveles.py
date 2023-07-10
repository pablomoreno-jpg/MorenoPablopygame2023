import pygame
import csv
import re
from constantes import*
from jugador import*
from plataforma import*
from enemigos import*
from auxiliar import*
from items import*


def leer_csv(nombre:str,columnas,filas)-> list:

    archivo_leido = []

    #creo una lista de listas caragada con -1
    for fila in range(filas):

        r = [-1] * columnas

        archivo_leido.append(r) 

    with open(nombre,"r",newline='') as archivo:
        
        leer = csv.reader(archivo, delimiter=';')

        

        for x, linea in enumerate(leer):

            for y, num_bloque in enumerate(linea): 

                archivo_leido[x][y] = int(num_bloque)

    return archivo_leido


class Nivel():
    
    def __init__(self,nivel,columnas_nivel,filas_nivel) -> None:
        
        self.lista_solidos = []
        self.lista_trampas = []
        self.lista_lava = []
        self.columnas = columnas_nivel
        self.filas = filas_nivel
        self.nivel = nivel
    

    def prosesar_data(self):
        
        data = leer_csv(self.nivel,self.columnas,self.filas)

        for y, fila, in enumerate(data):
            
            for x, columna in enumerate(fila):

                if columna >= 0 and columna < 288 and type(columna) == int:
                        
                        if columna == 6:

                            #jugador

                            pass

                        elif columna == 7:
                            
                            #item

                            pass
                        
                        elif columna == 12:

                            #enemigo
                            pass
                        
                        elif columna in LISTA_TRAMPAS:

                            bloque = Plataforma(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,tamaño=TAM_BLOQUE,path=BLOQUES,image_indec=columna,columnas=24,filas=12)

                            self.lista_trampas.append(bloque)


                        else:


                            bloque = Plataforma(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,tamaño=TAM_BLOQUE,path=BLOQUES,image_indec=columna,columnas=24,filas=12)


                            self.lista_solidos.append(bloque)

                        pass
                    
            
    def draw(self,screen):
        
        for bloque in self.lista_solidos:

            bloque.draw(screen)

        for bloque in self.lista_trampas:

            bloque.draw(screen)