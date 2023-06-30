import pygame
from constantes import *
from auxiliar import*

class Enemigo:

    def __init__(self,velocidad) -> None:
    
        self.caminar_r = []
        self.caminar_l = [] 
        self.quieto_r = []
        self.quieto_l = []
        self.muerte_r = []
        self.muerte_l = []
        self.speed = velocidad

        self.frame = 0
        self.animacio = self.quieto_r
        self.tiempo_trasncurrido = 0
        self.rect = self.imagen.get_rect()
        self.imagen = self.animacio[self.frame]
        
    
    def uptade(self,delta_ms):

        self.tiempo_trasncurrido += delta_ms

        if self.tiempo_trasncurrido >= 30:

            self.tiempo_trasncurrido = 0

            if self.frame < len(self.animacio) -1:

                self.frame += 1

    def draw(self,screen):

        self.imagen = self.animacio[self.frame]

        screen.blit(screen,self.rect)
    
