from typing import Any
import pygame
from constantes import*
from auxiliar import*


class Bala(pygame.sprite.Sprite):

    def __init__(self,x,y,direccion,tipo) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.tipo = tipo
        self.direccion = direccion
        self.image = self.direccion_bala()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)



    def obtener_bala(self):

        match self.tipo:

            case "escopeta":
                
                imagen = pygame.image.load(r"{0}\shotgun bullet.png".format(PAHT_PROYECTILES)).convert_alpha()

                self.speed = 8

            case "pistola":

                self.speed = 12

            case "plasma":

                self.speed = 17

            case "metralleta":

                self.speed = 16

            case "bfg":

                self.speed = 1
        

        return imagen

    def direccion_bala(self):

        imagen = self.obtener_bala()

        if self.direccion == DIRECCION_R:

            imagen = pygame.transform.flip(imagen,True,False)

        return imagen
    
    def update(self):
        
        if self.direccion == DIRECCION_R:

            self.rect.x += self.speed

        else:

            self.rect.x -= self.speed

        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.kill()

        