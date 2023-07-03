import pygame
from constantes import*

class Auxliar:


    @staticmethod
    def load_sprisheet(directorio:str,columnas:int,filas:int,step = 1,direcciones = False) -> list:

        lista = []

        imagen_superficie = pygame.image.load(r"{0}{1}".format(PHAT_RECURSOS,directorio))
        
        fotograma_ancho = int(imagen_superficie.get_width() / columnas)
        fotograma_alto = int(imagen_superficie.get_height() / filas)

        for fila in range(filas):

            for columna in range(0,columnas,step):

                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                superficie_fotograma = imagen_superficie.subsurface(x,y,fotograma_ancho,fotograma_alto)

                if direcciones:
                    superficie_fotograma = pygame.transform.flip(superficie_fotograma,True,False)

                lista.append(superficie_fotograma)


        return lista
