import pygame
import csv
import random
from constantes import*
from jugador import*
from plataforma import*
from enemigos import*
from auxiliar import*
from items import*


LISTA_ENEMIOS = ["imp","soldado 1","soldado 2","super demonio"]
LISTA_ITEMS = ["escudo","escudo pequeño","escudo","plasma","botiquin pequeño","botiquin"]

def terminador_partida(player:Jugador,segundos:int,minutos:int,superficie) -> bool:

    jugando = True

    if player.vivo == False:

        texto = "YOU DIED"

        texto = Auxliar.generar_texto(PAHT_FONT,150,texto,ROJO)

        imprimir_texto(superficie,texto,ANCHO_VENTANA/2,ALTO_VENTANA/2,350,150)

        if player.frame == len(player.animacion) - 1:
            
            jugando = False
            player.puntaje -= 100

    elif player.vivo == True and minutos == 0 and segundos == 0:

        texto = "YOU WIN!!!"

        texto = Auxliar.generar_texto(PAHT_FONT,150,texto,VERDE)

        imprimir_texto(superficie,texto,ANCHO_VENTANA/2,ALTO_VENTANA/2,350,150)
        
        if player.frame == len(player.animacion) - 1:
            
            jugando = False

    return jugando

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
        self.item_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.columnas = columnas_nivel
        self.filas = filas_nivel
        self.nivel = nivel
        self.jugador_cargador = False
        self.bloques_cargados = False
    

    def prosesar_data(self):
        
        jugador = None
        data = leer_csv(self.nivel,self.columnas,self.filas)

        for y, fila, in enumerate(data):
            
            for x, bloque in enumerate(fila):

                if bloque >= 0 and bloque < 288:
                        
                        if bloque == JUGADOR :

                            if self.jugador_cargador == False:

                                self.jugador_cargador = True
                                jugador = Jugador(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE, velocidad=6,framerate_animacion= 200, framerate_moviemiento= 18)

                        elif bloque == ITEM:

                            item_random = random.choice(LISTA_ITEMS)
                            item = Items(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,item_tipo=item_random)

                            self.item_group.add(item)

                        elif bloque == ENEMIGO:
                            
                            enemigo_random = random.choice(LISTA_ENEMIOS)
                            enemigo = Enemigo(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,velocidad=4,framerate_animacion= 200, framerate_moviemiento= 18,tipo_enemigo= enemigo_random)
                            
                            self.enemy_group.add(enemigo)

                        elif bloque in LISTA_TRAMPAS:
                            

                                bloque = Plataforma(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,tamaño=TAM_BLOQUE,path=BLOQUES,image_indec=bloque,columnas=24,filas=12)
                                

                                self.lista_trampas.append(bloque)


                        else:


                            bloque = Plataforma(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,tamaño=TAM_BLOQUE,path=BLOQUES,image_indec=bloque,columnas=24,filas=12)

                            self.lista_solidos.append(bloque)

                        pass
                    
        return jugador

    def volver_a_cargar_items(self):

        data = leer_csv(self.nivel,self.columnas,self.filas)

        for y, fila, in enumerate(data):
        
            for x, bloque in enumerate(fila):

                if bloque >= 0 and bloque < 288:

                    if bloque == ITEM:
                        
                        item_random = random.choice(LISTA_ITEMS)
                        item = Items(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,item_tipo=item_random)

                        self.item_group.add(item)

    def volver_a_cargar_enemigo(self):

        data = leer_csv(self.nivel,self.columnas,self.filas)

        for y, fila, in enumerate(data):
        
            for x, bloque in enumerate(fila):

                if bloque == ENEMIGO:
                    
                    enemigo_random = random.choice(LISTA_ENEMIOS)
                    enemigo = Enemigo(x= x*TAM_BLOQUE,y=y*TAM_BLOQUE,velocidad=4,framerate_animacion= 200, framerate_moviemiento= 18,tipo_enemigo= enemigo_random)
                    
                    self.enemy_group.add(enemigo)


    def draw(self,screen):
        
        for bloque in self.lista_solidos:

            bloque.draw(screen)

        for bloque in self.lista_trampas:

            bloque.draw(screen)