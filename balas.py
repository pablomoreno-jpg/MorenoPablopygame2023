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

            case "default":
                
                imagen = Auxliar.load_sprisheet(r"\proyectiles\bullet.png",columnas=1,filas=3)[0]

                imagen = pygame.transform.scale2x(imagen)

                self.speed = 12

            case "plasma":
                
                imagen = Auxliar.load_sprisheet(r"\proyectiles\bullet.png",columnas=1,filas=3)[2]

                self.speed = 17

            case "rocket":
                
                imagen = Auxliar.load_sprisheet(r"\proyectiles\bullet.png",columnas=1,filas=3)[1]

                self.speed = 5


        return imagen

    def direccion_bala(self):

        imagen = self.obtener_bala()

        if self.direccion == DIRECCION_R:

            imagen = pygame.transform.flip(imagen,True,False)

        return imagen
    
    def update(self,player,enemigo=None):
        
        if self.direccion == DIRECCION_R:

            self.rect.x += self.speed

        else:

            self.rect.x -= self.speed

        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.kill()


        # if pygame.sprite.spritecollide(player, player.grupo_balas,False):
           
        #     if player.salud_maxima > 0:

        #         player.salud_maxima -= 5 

        #         self.kill()


        