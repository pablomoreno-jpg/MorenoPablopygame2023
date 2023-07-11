import pygame
from constantes import*



def imprimir_texto(superfice,mensaje,x,y,tamaño_mensaje_x = 0,tamaño_mensaje_y = 0):

    escalar_x = tamaño_mensaje_x / 2
    escalar_y = tamaño_mensaje_y / 2

    superfice.blit(mensaje, (x - escalar_x, y - escalar_y))




class Auxliar:


    @staticmethod
    def load_sprisheet(directorio:str,columnas:int,filas:int,step = 1,direcciones = False,) -> list:

        lista = []

        imagen_superficie = pygame.image.load(directorio)
        

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
    

    @staticmethod
    def elegir_background(nombre_nivel:str):

        fondo = pygame.image.load(FONDOS_NIVLES[nombre_nivel])
        fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        return fondo
    
    @staticmethod
    def generar_texto(fuente:str,tamaño:float,contenido:str,color:tuple):

        fuente = pygame.font.SysFont(fuente,tamaño)
        return fuente.render(contenido,True,color)
    
