import pygame
import csv
from constantes import*
from jugador import*
from plataforma import*
from enemigos import*
from auxiliar import*


def leer_csv(nombre:str)-> list:

    nivel = []

    with open(nombre,"r",newline= "") as archivo:
        
        leer = csv.reader(archivo, delimiter=',')

        for x, fila in enumerate(leer):

            for y, columna in enumerate(fila):

                nivel[x][y] = int(columna)
        
    return nivel


# class Niveles(pygame.sprite.Sprite):

#     def __init__(self,path_niveles,screen) -> None:
#         super().__init__()
#         self.lista_niveles = leer_csv(path_niveles)
#         self.screen = screen
#         self.paht_bloque = ""
#         self.bloque = None

#     def buscar_path(self,color_bloque:str):

#         if color_bloque == "azul":

#             self.paht_bloque = r"{0}{1}".format(PHAT_RECURSOS,PAHT_BLOQUES_AZUL)
        
#         elif color_bloque == "amarillo":

#             self.paht_bloque =r"{0}{1}".format(PHAT_RECURSOS,PAHT_BLOQUES_AMARILLO)

#     def cargar_bloque(self,numero_bloque,nombre_bloque,pos_x,pos_y):
          
#         #21 * 8

#         self.buscar_path(nombre_bloque)

#         if numero_bloque < 0:


#             pass


#     def crear_nivel(self):

#         for y in range(-ALTO_VENTANA // TAM_BLOQUE ,ALTO_VENTANA*2// TAM_BLOQUE):

#             for x in range(-ANCHO_VENTANA // TAM_BLOQUE ,ANCHO_VENTANA*2// TAM_BLOQUE):

                


#                 pass


#     def draw_level(slef,screan):
#         pass   