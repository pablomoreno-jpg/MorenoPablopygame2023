from typing import Any
import pygame
from constantes import*
from auxiliar import*


class Bala(pygame.sprite.Sprite):

    def __init__(self,x,y,direccion,tipo,velocidad) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.tipo = tipo
        self.direccion = direccion
        self.image = self.direccion_bala()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = velocidad

    def direccion_bala(self):

        imagen = pygame.image.load(r"{0}\shotgun bullet.png".format(PAHT_PROYECTILES)).convert_alpha()

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

        